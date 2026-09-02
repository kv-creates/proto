// GTFS-mock graph + multi-criteria Dijkstra
// Modes: train, metro, bus, auto, walk
export const EMISSION = { train: 12, metro: 18, bus: 65, auto: 110, walk: 0 }; // gCO2 / passenger-km
export const COST_PER_KM = { train: 0.6, metro: 2.5, bus: 1.2, auto: 18, walk: 0 };
export const SPEED_KMH = { train: 38, metro: 32, bus: 18, auto: 22, walk: 4.5 };

export function buildMumbaiMock(){
  // nodes: Dadar, Bandra, Andheri, Churchgate, Thane, etc
  return {
    "Churchgate": [{to:"Dadar", mode:"train", dist:8}, {to:"Bandra", mode:"bus", dist:12}],
    "Dadar": [{to:"Bandra", mode:"train", dist:6}, {to:"Andheri", mode:"metro", dist:9}, {to:"Thane", mode:"train", dist:22}],
    "Bandra": [{to:"Andheri", mode:"auto", dist:7}, {to:"Dadar", mode:"bus", dist:6}],
    "Andheri": [{to:"Thane", mode:"bus", dist:28}, {to:"Ghatkopar", mode:"metro", dist:11}],
    "Thane": [{to:"Ghatkopar", mode:"train", dist:14}],
    "Ghatkopar": []
  };
}

export function paretoRoutes(graph, start, end){
  // brute small graph: enumerate paths up to 4 hops, compute metrics, pareto filter
  const paths=[];
  function dfs(node, path, modes, dist, visited){
    if(path.length>6) return;
    if(node===end){
      const time = dist.reduce((s,d,i)=> s + d/SPEED_KMH[modes[i]]*60, 0); // mins
      const carbon = dist.reduce((s,d,i)=> s + d*EMISSION[modes[i]], 0);
      const cost = dist.reduce((s,d,i)=> s + d*COST_PER_KM[modes[i]], 0);
      paths.push({path:[...path], modes:[...modes], dist:[...dist], time:Math.round(time), carbon:Math.round(carbon), cost:Math.round(cost)});
      return;
    }
    for(const e of graph[node]||[]){
      if(visited.has(e.to)) continue;
      visited.add(e.to);
      path.push(e.to); modes.push(e.mode); dist.push(e.dist);
      dfs(e.to, path, modes, dist, visited);
      path.pop(); modes.pop(); dist.pop();
      visited.delete(e.to);
    }
  }
  dfs(start,[start],[],[], new Set([start]));
  // pareto: keep if not dominated on all three (time, carbon, cost)
  const pareto=[];
  for(const p of paths){
    let dominated=false;
    for(const q of paths){
      if(q!==p && q.time<=p.time && q.carbon<=p.carbon && q.cost<=p.cost && (q.time<p.time||q.carbon<p.carbon||q.cost<p.cost)) {dominated=true;break;}
    }
    if(!dominated) pareto.push(p);
  }
  return pareto.sort((a,b)=> a.time-b.time);
}
