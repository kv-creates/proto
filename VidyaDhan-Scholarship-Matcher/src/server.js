import http from "http"; const s=http.createServer((req,res)=>res.end(JSON.stringify({ok:true}))); s.listen(3000);
