from .forgery import ensemble
import pathlib
def demo():
    # create dummy image if not exists
    from PIL import Image
    p=pathlib.Path("demo/sample.jpg")
    p.parent.mkdir(exist_ok=True)
    if not p.exists():
        Image.new("RGB",(400,200),color=(240,240,240)).save(p,"JPEG")
    print(ensemble(str(p), ocr_text="B.Tech CGPA 9.9 University Topper 2023", qr_data="https://university.example/verify?id=123"))
if __name__=="__main__": demo()
