import test from "node:test";
import assert from "node:assert";
import { parseVoice } from "../src/parser.js";
test("hindi amount",()=>{ const r=parseVoice("Ramesh ko 500 udhaar diya"); assert.equal(r.amount,500); assert.equal(r.type,"credit"); });
test("hazar",()=>{ const r=parseVoice("2 hazar liya"); assert.equal(r.amount,2000); });
