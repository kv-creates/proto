import crypto from "crypto";
export function hashReport(report){
  const payload=JSON.stringify({photoHash: report.photoHash, geo: report.geo, issue: report.issue, ts: report.ts});
  return crypto.createHash("sha256").update(payload).digest("hex");
}
export function wardFromGeo(lat, lon){
  // naive Mumbai ward mock: 24 wards grid
  const ward = Math.floor((lat*10)%24)+1;
  return `ward-${String(ward).padStart(2,'0')}`;
}
export function quorum(verifies){
  // 3 peers verify => escalate
  const yes=verifies.filter(v=>v.vote==="yes").length;
  return {yes, total:verifies.length, quorumReached: yes>=3, status: yes>=3?"escalate_to_bmc": yes>=1?"pending": "rejected"};
}
