import test from "node:test"; import assert from "node:assert"; import { matchCompanions } from "../src/match.js";
test("m",()=> assert.equal(matchCompanions([{id:"r1"}],[{id:"v1"}]).length,1));
