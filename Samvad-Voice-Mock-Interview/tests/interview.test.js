import test from "node:test"; import assert from "node:assert"; import { scoreAnswer } from "../src/interview.js";
test("s",()=> assert.equal(scoreAnswer("hi").overall,80));
