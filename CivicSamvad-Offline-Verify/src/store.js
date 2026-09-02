import fs from "fs";
import path from "path";
import { hashReport, wardFromGeo } from "./hashing.js";
const DB=path.join(process.cwd(),"reports.json");
export function load(){ try{return JSON.parse(fs.readFileSync(DB,"utf-8"))}catch{return []}}
export function save(r){ fs.writeFileSync(DB, JSON.stringify(r,null,2))}
export function createReport({issue, geo, photoHash}){
  const ts=new Date().toISOString();
  const ward=wardFromGeo(geo.lat, geo.lon);
  const hash=hashReport({issue, geo, photoHash, ts});
  const rec={id:hash.slice(0,12), issue, geo, ward, photoHash, ts, hash, verifies:[] , syncStatus:"pending"};
  const all=load(); all.push(rec); save(all); return rec;
}
export function verify(id, voter, vote){
  const all=load(); const r=all.find(x=>x.id===id); if(!r) throw new Error("not found"); r.verifies.push({voter, vote, ts:new Date().toISOString()}); save(all); return r;
}
