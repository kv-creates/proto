from .skills import gap, learning_path
import json
def demo():
    resume="Final year CSE, Python, Java, SQL, HTML/CSS, Git, basic DSA"
    jd="Hiring: Python, FastAPI, Postgres, Docker, AWS, React, System Design, DSA"
    g=gap(resume,jd)
    g["roadmap"]=learning_path(g["missing"])
    print(json.dumps(g,indent=2))
if __name__=="__main__": demo()
