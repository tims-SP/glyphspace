#!/usr/bin/env python3
"""Verify the E/K unattributed physical-crop contract inside an R245F20 cumulative ZIP.
This is not source-shape certification. Usage: python scripts/r245f20_ek_crop_contract.py archive.zip
"""
import hashlib
import json
import sys
import zipfile

EXPECTED_JPEG = "df5eb1a8678eea5ae27b3bfbc6bcef17af8b8ef558696834214dcdffa86dcd49"
EXPECTED_REGISTRY = "cafa1c6eae872e1562109830faae5347094b41690c7bb63e5a4ce784a95e77bb"
GROUPS = {
    "E-ambiguous-invalid-01": ["legacy:E:1", "legacy:E:8"],
    "K-lower-left-03": ["K-physical-lower-left", "legacy:K:2", "legacy:K:3"],
    "K-lower-right-02": ["K-physical-lower-right", "legacy:K:4"],
    "K-upper-left-02": ["K-physical-upper-left", "legacy:K:0"],
}

def main(path):
    with zipfile.ZipFile(path) as archive:
        jpeg = archive.read("v036_round2/reference/2008_user_reference.jpg")
        raw_registry = archive.read("v036_round144/R144_25key_review_registry.json")
        contract = json.loads(archive.read("v036_r245f20/R245F20_EK_physical_conflicts.json"))
    assert hashlib.sha256(jpeg).hexdigest() == EXPECTED_JPEG
    assert hashlib.sha256(raw_registry).hexdigest() == EXPECTED_REGISTRY
    registry = json.loads(raw_registry)
    observations = {o["sourceObservationId"]: o for k in registry["keyReviews"] for o in k["observations"]}
    assert len(registry["keyReviews"]) == 25 and len(observations) == 170
    assert sum(len(k["reviewCases"]) for k in registry["keyReviews"]) == 52
    assert contract["formalCertification"] is False and contract["approvedPermanentIds"] == 0
    assert contract["sourceJPEG_SHA256"] == EXPECTED_JPEG and contract["registrySHA256"] == EXPECTED_REGISTRY
    assert len(contract["groups"]) == 4
    for group in contract["groups"]:
        ids = GROUPS[group["groupId"]]
        assert group["sourceObservationIds"] == ids
        assert group["identityStatus"] == "unresolved"
        assert group["historicalInvalid"] == group["groupId"].startswith("E-")
        assert all(observations[i]["nativeRect"] == group["nativeRect"] and observations[i]["rgbSHA256"] == group["rgbSHA256"] for i in ids)
        key = hashlib.sha256(json.dumps([group["key"], group["nativeRect"], group["rgbSHA256"]], separators=(",", ":")).encode()).hexdigest()
        assert group["physicalCropKey"] == key
    assert sum(map(len, GROUPS.values())) == 9
    print("PASS E/K physical crop contract: 4 groups, 9 unresolved observations, 0 approved IDs (NOT certification)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python scripts/r245f20_ek_crop_contract.py archive.zip")
    main(sys.argv[1])
