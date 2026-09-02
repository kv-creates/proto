import http from "http";
import { parseVoice, ledgerEntry } from "./parser.js";
import { add, balance, load } from "./ledger.js";
const server=http.createServer((req,res)=>{
  res.setHeader("Access-Control-Allow-Origin","*");
  res.setHeader("Content-Type","application/json");
  if(req.url==="/health"){ res.end(JSON.stringify({status:"ok"})); return}
  if(req.url==="/balance"){ res.end(JSON.stringify(balance())); return}
  if(req.url==="/ledger"){ res.end(JSON.stringify(load())); return}
  if(req.method==="POST" && req.url==="/voice"){
    let b=""; req.on("data",c=>b+=c); req.on("end",()=>{
      const {text}=JSON.parse(b||"{}");
      const p=parseVoice(text||"");
      const e=ledgerEntry(p);
      if(e.status==="ok") add(e);
      res.end(JSON.stringify(e));
    }); return
  }
  res.end(JSON.stringify({routes:["GET /health","GET /balance","POST /voice {text}"]}));
});
server.listen(3000,()=> console.log("VyaparSaathi http://localhost:3000"));
