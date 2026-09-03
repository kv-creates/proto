import test from "node:test"; import assert from "node:assert"; import { chunkVideo, syncQueue } from "../src/cache.js";
test("chunk",()=>{assert.equal(chunkVideo(new Uint8Array(1024*1024),262144).length,4)});
test("queue",()=>{const q=syncQueue(); q.push({id:1}); assert.equal(q.size(),1);});
