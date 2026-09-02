import http from "http";
import { createReport, verify, load } from "./store.js";
import { quorum } from "./hashing.js";
const s=http.createServer((req,res)=>{
  res.setHeader("Access-Control-Allow-Origin","*");
  res.setHeader("Content-Type","application/json");
  if(req.url==="/health") return res.end(JSON.stringify({status:"ok"}));
  if(req.url==="/reports" && req.method==="GET") return res.end(JSON.stringify(load()));
  if(req.url==="/report" && req.method==="POST"){
    let b=""; req.on("data",c=>b+=c); req.on("end",()=>{ const j=JSON.parse(b||"{}"); const r=createReport(j); res.end(JSON.stringify(r)); }); return;
  }
  if(req.url.startsWith("/verify") && req.method==="POST"){
    let b=""; req.on("data",c=>b+=c); req.on("end",()=>{ const j=JSON.parse(b||"{}"); const r=verify(j.id, j.voter, j.vote); res.end(JSON.stringify({...r, quorum: quorum(r.verifies)})); }); return;
  }
  res.end(JSON.stringify({routes:["POST /report {issue,geo,photoHash}","POST /verify {id,voter,vote}","GET /reports"]}));
});
s.listen(3000, ()=> console.log("CivicSamvad http://localhost:3000"));
