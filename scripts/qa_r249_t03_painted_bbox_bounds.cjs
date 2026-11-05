'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const window={};vm.runInNewContext(fs.readFileSync(__dirname+'/r245f70_t03_draft_geometry_registry.js','utf8'),{window,Error,Number,Math,Object,Array,Set,Map,String});
const keys='ABCDEFGHIJKLMNOPQRSTUVWXY'.split('');
// A complete synthetic catalog exercises the real 151-row coverage gate, without real glyph assets.
const rows=Array.from({length:151},(_,i)=>{const key=keys[i%keys.length],slot=String(Math.floor(i/keys.length)).padStart(2,'0');return {candidateInstanceId:`wb06/${key}/legacy-${slot}`,legacyInstanceId:`${key}-root-${slot}`,key,referenceShapeId:null,assetId:null,geometry:{x:10,y:10,width:20,height:20,anchor:'ink-center',ox:0,oy:0},paintedBBox:{x:10,y:10,width:20,height:20},inkBBoxCertified:false,sourceCertified:false,permanentIdApproved:false,status:'planning_only'};});
const catalog=()=>({schemaVersion:'T03-isolated-draft-1',coordinateSystem:'0 0 100 100',sourceCertified:false,permanentIDsApproved:0,records:rows});
let n=0;const accept=()=>{assert.equal(window.GlyphSpaceT03Registry.fromCatalog(catalog()).list().length,151);n++};
const reject=(bbox)=>{const old=rows[0].paintedBBox;rows[0].paintedBBox=bbox;assert.throws(()=>window.GlyphSpaceT03Registry.fromCatalog(catalog()),/invalid source painted bbox/);rows[0].paintedBBox=old;n++};
accept();reject({x:-1,y:10,width:20,height:20});reject({x:10,y:-1,width:20,height:20});reject({x:95,y:10,width:20,height:20});reject({x:10,y:95,width:20,height:20});accept();console.log(`R249 Root T03 paintedBBox bounds: ${n}/${n} PASS (synthetic Node VM; not source certification)`);

[executed on device: racknerd-cd91d33 (14f717ef-2473-48f7-b592-70729eb065b1)]