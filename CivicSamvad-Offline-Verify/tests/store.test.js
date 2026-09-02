import test from "node:test";
import assert from "node:assert";
import fs from "fs";
import { createReport, verify, load } from "../src/store.js";
import { quorum } from "../src/hashing.js";
test("quorum 3 yes",()=>{
  try{fs.unlinkSync("reports.json")}catch{}
  const r=createReport({issue:"garbage", geo:{lat:19,lon:72}, photoHash:"h1"});
  verify(r.id,"a","yes"); verify(r.id,"b","yes"); verify(r.id,"c","yes");
  const q=quorum(load().find(x=>x.id===r.id).verifies);
  assert.equal(q.quorumReached,true);
})
