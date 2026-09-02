import Fastify from "fastify";
import { buildMumbaiMock, paretoRoutes } from "./graph.js";
const fastify=Fastify();
const graph=buildMumbaiMock();
fastify.get("/health", async()=>({status:"ok"}));
fastify.get("/routes", async(req)=> {
  const {from, to}=req.query;
  if(!from||!to) return {error:"?from=&to="};
  return paretoRoutes(graph, from, to);
});
fastify.listen({port:3000});
