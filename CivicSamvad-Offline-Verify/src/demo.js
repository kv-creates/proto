import { createReport, verify } from "./store.js";
import { quorum } from "./hashing.js";
import fs from "fs";
try{fs.unlinkSync("reports.json")}catch{}
const r=createReport({issue:"pothole", geo:{lat:19.07,lon:72.87}, photoHash:"abc123"});
console.log("created", r);
verify(r.id, "peer1","yes"); verify(r.id,"peer2","yes"); verify(r.id,"peer3","yes");
const {load}=await import("./store.js");
const updated=load().find(x=>x.id===r.id);
console.log("quorum", quorum(updated.verifies));
