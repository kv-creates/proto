import test from "node:test"; import assert from "node:assert"; import { crdtMerge } from "../src/mesh.js";
test("m",()=> assert.equal(crdtMerge([{id:1}]).length,1));
