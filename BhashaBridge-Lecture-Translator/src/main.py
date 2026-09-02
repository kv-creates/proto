import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except: pass
from .translator import stream_process, subtitle_vtt
def demo():
    chunks=["Hello students","Today we will learn about photosynthesis","Water and sunlight make food"]
    res=stream_process(chunks, "hi")
    try:
        print(res)
        print(subtitle_vtt([{"start":"00:00:00.000","end":"00:00:03.000","en":r["en"],"translated":r["translated"]} for r in res]))
    except UnicodeEncodeError:
        import json
        print(json.dumps(res, ensure_ascii=True, indent=2))
if __name__=="__main__": demo()
