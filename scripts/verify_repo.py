#!/usr/bin/env python3
"""Read-only repository integrity gate. Not a glyph, device, or migration certification."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
BASELINE = {
    "index.html": "fd7b9bdada44ab2d7452d71f99e77cfd7a7fe82eb9b29e3f0b41ab32fb758ddc",
    "preview/v0.36/index.html": "ea290abb3a92fbd1b74d9e1c5bfdefe7eac8471eead93f53802dfaed47711df4",
}
TASK_NAMES = [
    "基线冻结", "参考图清点", "语义与 ID 设计", "SVG 坐标内核",
    "存储与旧版迁移", "完整性补图", "轮廓一致性",
    "位置与碰撞", "校准工作台闭环", "学习视图与输入回归",
    "视觉和设备验收", "发布冻结",
]
KEYS = set("GFDSAHJKLMTREWQYUIOPNBVCX")
MANIFEST = "docs/SHA256SUMS.txt"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def files() -> set[str]:
    return {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.relative_to(ROOT).parts
        and "__pycache__" not in p.parts and not p.name.endswith(".pyc")
    }


def check_checksums() -> None:
    lines = (ROOT / MANIFEST).read_text(encoding="utf-8").splitlines()
    refs: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"([a-f0-9]{64})  (.+)", line)
        require(match is not None, "Malformed checksum line: " + line[:100])
        checksum, path = match.groups()
        require(path not in refs and path != MANIFEST, "Duplicate/self checksum: " + path)
        require(".." not in Path(path).parts and not Path(path).is_absolute(), "Unsafe checksum path: " + path)
        refs[path] = checksum

    expected = files() - {MANIFEST}
    require(set(refs) == expected, f"Checksum coverage mismatch: missing={expected - set(refs)}, extra={set(refs) - expected}")
    for rel, expected_sha in refs.items():
        require(digest(ROOT / rel) == expected_sha, "SHA256 mismatch: " + rel)
    for rel, expected_sha in BASELINE.items():
        require(digest(ROOT / rel) == expected_sha, "Protected HTML mutated: " + rel)


def table_rows(source: str, pattern: str) -> list[list[str]]:
    return [
        [col.strip() for col in line.split("|")[1:-1]]
        for line in source.splitlines()
        if re.match(pattern, line)
    ]


def check_tasks() -> None:
    data = json.loads((ROOT / "docs/tasks/t00-t11.json").read_text(encoding="utf-8"))
    original = (ROOT / "docs/history/V0.36-P0-original.md").read_text(encoding="utf-8")
    rows = table_rows(original, r"^\| T(?:0[0-9]|1[01]) \|")
    require(len(rows) == 12, f"Historical WBS count !=12: {len(rows)}")
    tasks = data["tasks"]
    require(len(tasks) == 12, "task ledger must have 12 entries")
    for idx, (row, task) in enumerate(zip(rows, tasks)):
        old_id, priority, title, action, _, exit_criterion = row
        task_id = f"T{idx:02d}"
        require(task["id"] == old_id == task_id, "WBS ID/order drift at " + task_id)
        require(task["title"] == title == TASK_NAMES[idx], "WBS title drift at " + task_id)
        require(task["priority"] == priority, "WBS priority drift at " + task_id)
        require(task["sourceAction"] == action, "WBS source action drift at " + task_id)
        require(task["sourceExitCriterion"] == exit_criterion, "WBS exit gate drift at " + task_id)
        require(task["accepted"] is False, "Cannot auto-certify task from docs: " + task_id)
        deps = task["dependencies"]
        require(isinstance(deps, list) and all(d in {f"T{j:02d}" for j in range(idx)} for d in deps),
                "Invalid or forward dependency: " + task_id)
    require("T03" in data["tasks"][4]["dependencies"], "T04 must depend on T03")
    require("T03" in data["tasks"][5]["dependencies"], "T05 must depend on T03")


def check_keys() -> None:
    original = (ROOT / "docs/history/V0.35-root-audit-original.md").read_text(encoding="utf-8")
    historical = table_rows(original, r"^\| [A-Z] \| \d+ \|")
    with (ROOT / "docs/tasks/25-key-audit.csv").open("r", encoding="utf-8", newline="") as fp:
        rows = list(csv.DictReader(fp))
    require(len(rows) == len(historical) == 25, "25-key audit row count mismatch")
    require(set(row["key"] for row in rows) == KEYS and len(KEYS) == 25, "Bad/duplicate key inventory")
    require(sum(int(row["legacyVisible"]) for row in rows) == 151, "Legacy visible count must be 151")
    require(sum(bool(row["related"]) for row in rows) == 5, "Related-only count must be 5")
    for row, old in zip(rows, historical):
        key, visible, related, risk, focus, state = old
        require(row["key"] == key and row["legacyVisible"] == visible, "Key/count drift: " + key)
        require(row["related"] == ("" if related == "—" else related), "Related identity drift: " + key)
        require(row["risk"] == risk and row["focus"] == focus, "Risk/issue drift: " + key)
        require(row["legacyReviewStatus"] == state, "Historical audit state drift: " + key)
        require(all(row[field] == "" for field in ("referenceShapeCount", "confirmedMissingCount", "unreadableCount")),
                "Unknown shape/missing counts must remain empty: " + key)
        require(all(row[field] == "unreviewed" for field in
                    ("existence", "outline", "position", "scale", "classification")),
                "An audit opinion is not a certification: " + key)
        require(row["accepted"].lower() == "false", "Key must not auto-certify: " + key)


def check_links() -> None:
    known = files()
    errors: list[str] = []
    link_rx = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]+\")?\)")
    for rel in sorted(x for x in known if x.endswith(".md")):
        content = (ROOT / rel).read_text(encoding="utf-8")
        for match in link_rx.finditer(content):
            href = match.group(1)
            if href.startswith("#"):
                continue
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href.startswith("/"):
                continue
            target = (ROOT / rel).parent / unquote(parsed.path)
            resolved = target.resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.is_file():
                errors.append(f"{rel}: broken local link {href}")
    require(not errors, "Broken links:\\n" + "\\n".join(errors))


def main() -> int:
    check_checksums()
    check_tasks()
    check_keys()
    check_links()
    print("PASS repository integrity: protected HTML=2, WBS=12, key matrix=25/151/5, "
          "checksums and relative documentation links verified.")
    print("NOTE: no T00-T11 formal acceptance, original glyph certification, real device, "
          "or production localStorage migration is asserted.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, OSError, ValueError, KeyError, csv.Error) as exc:
        print("FAIL repository integrity: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
