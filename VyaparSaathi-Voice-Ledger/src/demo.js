import { parseVoice, ledgerEntry } from "./parser.js";
import { balance } from "./ledger.js";
const samples=["Ramesh ko 500 udhaar diya","Sunita se 1200 liya","Bijli ka 800 bhara","2 hazar ka saman liya"];
for(const s of samples) console.log(s,"=>", ledgerEntry(parseVoice(s)));
console.log(balance());
