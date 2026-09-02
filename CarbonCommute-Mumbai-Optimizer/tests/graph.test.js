import test from "node:test";
import assert from "node:assert";
import { buildMumbaiMock, paretoRoutes, EMISSION } from "../src/graph.js";
test("train less than auto",()=> assert.ok(EMISSION.train < EMISSION.auto));
test("pareto not empty",()=>{
  const g=buildMumbaiMock();
  const r=paretoRoutes(g,"Churchgate","Ghatkopar");
  assert.ok(r.length>0);
});
