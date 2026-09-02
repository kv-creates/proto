import argparse, json, pathlib, sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass
from .simplifier import analyze_document
def demo():
    p = pathlib.Path("demo/sample_agreement.txt")
    if p.exists():
        text = p.read_text(encoding="utf-8")
    else:
        text = """1. Licensee shall pay non-refundable deposit of Rs 50000. 2. Lock-in period 11 months, penalty 10% per month on early exit. 3. Owner may terminate without notice at sole discretion. 4. Tenant indemnify owner for all damages. 5. Jurisdiction Delhi."""
    res = analyze_document(text, to_hindi=False)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    print("\n--- Hindi mode ---")
    try:
        print(json.dumps(analyze_document(text, to_hindi=True), indent=2, ensure_ascii=False)[:1000])
    except UnicodeEncodeError:
        print(json.dumps(analyze_document(text, to_hindi=True), indent=2, ensure_ascii=True)[:1000])
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--serve", action="store_true")
    args = ap.parse_args()
    if args.serve:
        import uvicorn
        uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)
    else:
        demo()
