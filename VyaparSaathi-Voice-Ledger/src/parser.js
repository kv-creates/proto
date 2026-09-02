// Hindi/Marathi voice intent parser: "Ramesh ko 500 udhaar diya" -> transaction
export function parseVoice(text){
  const t=text.toLowerCase();
  let type="expense";
  if(/udhaar|diya|dena|loan/.test(t)) type="credit"; // receivable
  if(/liya|jama|received|mila/.test(t)) type="income";
  if(/kharcha|bhara|paid|diya/.test(t) && /saman|stock|rent|bijli/.test(t)) type="expense";
  // extract amount: 500, 1,500, 2 hazar
  let amount=null;
  const m=t.match(/(\d+[\,\.]?\d*)/);
  if(m) amount=parseInt(m[1].replace(/[,\.]/g,''),10);
  const hazar=t.match(/(\d+)\s*hazar/);
  if(hazar) amount=parseInt(hazar[1],10)*1000;
  // name
  const nameMatch=t.match(/(ramesh|suresh|amit|sunita|kirana|ahuja|sharma|\b[a-z]{3,10})/);
  const name=nameMatch? nameMatch[1] : "unknown";
  return {raw:text, type, amount, party:name, lang: /hazar|udhaar|diya/.test(t)? "hi" : "en"};
}
export function ledgerEntry(parsed){
  return {id:Date.now(), date:new Date().toISOString().slice(0,10), ...parsed, status: parsed.amount? "ok":"need_amount"};
}
