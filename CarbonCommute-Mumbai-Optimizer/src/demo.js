import { buildMumbaiMock, paretoRoutes } from "./graph.js";
const g=buildMumbaiMock();
console.log(JSON.stringify(paretoRoutes(g,"Churchgate","Ghatkopar"),null,2));
