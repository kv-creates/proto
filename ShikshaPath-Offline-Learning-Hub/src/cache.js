export function chunkVideo(bytes, chunk=262144){const out=[]; for(let i=0;i<bytes.length;i+=chunk) out.push(bytes.slice(i,i+chunk)); return out;}
export function syncQueue(){const q=[]; return {push:(i)=>q.push({...i}), pending:()=>q, ack:(id)=>{const n=q.findIndex(x=>x.id===id); if(n>=0) q.splice(n,1)}, size:()=>q.length};}
