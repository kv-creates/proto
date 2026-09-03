import http from "http"; import { chunkVideo } from "./cache.js";
const s=http.createServer((req,res)=>{res.setHeader("Content-Type","application/json"); if(req.url==="/health") return res.end(JSON.stringify({status:"ok"})); res.end(JSON.stringify({ok:true}));});
s.listen(3000,()=> console.log("ShikshaPath"));
