import test from "node:test"; import assert from "node:assert"; import { greedyPlacement } from "../src/optim.js";
test("p",()=> assert.equal(greedyPlacement([1,2]).length,1));
