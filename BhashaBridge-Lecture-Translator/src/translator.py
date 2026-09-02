# Mock streaming translator: en -> hi, mr, ta, te, kn, bn, gu, ml
TRANSLATIONS = {
  "photosynthesis": {"hi":"प्रकाश संश्लेषण","mr":"प्रकाशसंश्लेषण","ta":"ஒளிச்சேர்க்கை"},
  "hello": {"hi":"नमस्ते","mr":"नमस्कार","ta":"வணக்கம்","te":"హలో","kn":"ನಮಸ್ಕಾರ"},
  "today we will learn about": {"hi":"आज हम सीखेंगे","mr":"आज आपण शिकणार","ta":"இன்று நாம் கற்கப்போகிறோம்"},
}
SUPPORTED=["hi","mr","ta","te","kn","bn","gu","ml","en"]

def mock_transcribe(chunk_text: str) -> str:
    # In real: whisper streaming; here echo
    return chunk_text.strip()

def mock_translate(en_text: str, target: str) -> str:
    low=en_text.lower()
    for k, vals in TRANSLATIONS.items():
        if k in low:
            # replace first occurrence
            tr = vals.get(target, k)
            low = low.replace(k, tr)
    # prefix to show translation
    return f"[{target}] {low}"

def stream_process(chunks, target="hi"):
    out=[]
    for c in chunks:
        en=mock_transcribe(c)
        hi=mock_translate(en, target)
        out.append({"en":en, "translated":hi, "target":target})
    return out

def subtitle_vtt(segments):
    # segments: [{start,end,en,translated}]
    vtt="WEBVTT\n\n"
    for i,s in enumerate(segments):
        vtt+=f"{i+1}\n{s['start']} --> {s['end']}\n{s['en']}\n{s['translated']}\n\n"
    return vtt
