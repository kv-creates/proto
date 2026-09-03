import test from "node:test"; import assert from "node:assert"; import { match } from "../src/matcher.js";
test("m",()=> assert.ok(match({income:100000})[0].eligible));
