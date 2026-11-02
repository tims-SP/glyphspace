from pathlib import Path
import sys
root=Path(sys.argv[1])
src=root/'v036_r245f56/R245F56_T03_three_view_replica_source_guard_candidate.html'
dst=root/'v036_r245f67/R245F67_T03_replica_attribute_and_viewbox_guard_candidate.html'
dst.parent.mkdir(parents=True,exist_ok=True)
s=src.read_text()
old='''function validate(id){
 if(!source()||source().innerHTML!==symbolBaseline)throw Error('glyph symbol source mutated');'''
new='''// R245F67: freeze all rendering-relevant outer attributes and each SVG viewport.
// Only the preview-owned transform and planning-only binding annotations are mutable.
const svgBaseline=new Map([...document.querySelectorAll('#full .tile[data-key]')].map(tile=>
 [tile.dataset.key,tile.querySelector('svg').cloneNode(false)]));
function sameFrozenAttributes(node,reference,ignored=[]){
 if(!node||!reference)return false;
 const omit=new Set(ignored);
 const actual=[...node.attributes].filter(a=>!omit.has(a.name));
 const expected=[...reference.attributes].filter(a=>!omit.has(a.name));
 return actual.length===expected.length&&expected.every(a=>node.getAttribute(a.name)===a.value);
}
function validate(id){
 if(!source()||source().innerHTML!==symbolBaseline)throw Error('glyph symbol source mutated');'''
assert s.count(old)==1
s=s.replace(old,new)
old=''' const sourceAttrs=['data-root','data-root-id','data-root-index','data-x','data-y','data-glyph-size'];
 const reference=baseline.get(id).node;
 const replicaValid=n=>n.innerHTML===baseline.get(id).markup&&sourceAttrs.every(a=>n.getAttribute(a)===reference.getAttribute(a));'''
new=''' const reference=baseline.get(id).node;
 const replicaValid=n=>{
  if(n.innerHTML!==baseline.get(id).markup||!sameFrozenAttributes(n,reference,
    ['transform','data-candidate-instance-id','data-binding-status']))return false;
  // The draft identity is mutable only through the planning-only binder.
  if(n.hasAttribute('data-candidate-instance-id')||n.hasAttribute('data-binding-status')){
   const binding=window.GlyphSpaceT03Binding?.resolveLegacy(id);
   if(!binding||n.dataset.candidateInstanceId!==binding.candidateInstanceId||
      n.dataset.bindingStatus!=='planning_only')return false;
  }
  const tile=n.closest('.tile[data-key]'),svg=n.closest('svg');
  if(!tile||!svg||tile.dataset.key!==id.slice(0,1)||
     svg.getAttribute('viewBox')!=='0 0 100 100'||
     !sameFrozenAttributes(svg,svgBaseline.get(tile.dataset.key)))return false;
  return true;
 };'''
assert s.count(old)==1
s=s.replace(old,new)
dst.write_text(s)
print(dst, len(s))
