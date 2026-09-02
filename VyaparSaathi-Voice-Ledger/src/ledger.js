import fs from "fs";
import path from "path";
const DB=path.join(process.cwd(),"ledger.json");
export function load(){ try{return JSON.parse(fs.readFileSync(DB,"utf-8"))}catch{return []}}
export function save(entries){ fs.writeFileSync(DB, JSON.stringify(entries,null,2))}
export function add(entry){ const e=load(); e.push(entry); save(e); return entry}
export function balance(){
  const e=load();
  let credit=0, debit=0;
  for(const r of e){ if(r.type==="credit") credit+=r.amount||0; if(r.type==="expense") debit+=r.amount||0; if(r.type==="income") credit+=r.amount||0; }
  return {credit, debit, net:credit-debit, count:e.length}
}
