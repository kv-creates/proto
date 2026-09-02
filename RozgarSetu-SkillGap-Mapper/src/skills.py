import re
from collections import Counter

SKILL_LEXICON = [
  "python","java","javascript","typescript","react","node","fastapi","flask","django","sql","postgres","mongodb","docker","kubernetes","aws","gcp","azure","git","linux","pandas","numpy","pytorch","tensorflow","scikit-learn","power bi","excel","tableau","communication","dsa","system design","oops","rest api","graphql","next.js","html","css"
]

def extract_skills(text: str):
    low=text.lower()
    found=[]
    for s in SKILL_LEXICON:
        if re.search(r"\b"+re.escape(s)+r"\b", low):
            found.append(s)
    return sorted(set(found))

def gap(resume_text: str, jd_text: str):
    r=set(extract_skills(resume_text))
    j=set(extract_skills(jd_text))
    matched=r & j
    missing=j - r
    extra=r - j
    coverage = len(matched)/len(j) if j else 1.0
    # simple TF-IDF weighting: rare skills weighted higher (mock: length)
    score = round(coverage*100,1)
    return {"resume_skills":sorted(r), "jd_skills":sorted(j), "matched":sorted(matched), "missing":sorted(missing), "extra":sorted(extra), "coverage":score}

ROADMAP = {
  "python": ["Python basics (Week 1-2) - Automate the Boring Stuff", "DSA in Python (Week 3-4)", "Build 2 projects (Week 5-6)"],
  "sql": ["SQL ZOO + Leetcode SQL 50", "Design e-commerce DB schema"],
  "react": ["React docs + 3 mini apps", "Next.js crash course", "Build portfolio site"],
  "aws": ["AWS CCP essentials", "Deploy a FastAPI on EC2"],
  "docker": ["Docker 101 - containerize your app", "Compose + multi-stage"],
  "dsa": ["Striver SDE sheet 30 days", "Mock interviews"],
  "system design": ["Grokking system design - 5 case studies"],
}

def learning_path(missing):
    plan=[]
    for s in missing:
        steps = ROADMAP.get(s, [f"Learn {s} - curated resources (search roadmap.sh/{s})"])
        plan.append({"skill":s, "weeks": 2 if s not in ["dsa","system design"] else 4, "steps": steps})
    # 30/60/90 day split
    days30=[p for p in plan[:2]]
    days60=plan[2:4]
    days90=plan[4:]
    return {"30_days":days30, "60_days":days60, "90_days":days90, "total_weeks": sum(p["weeks"] for p in plan)}

if __name__=="__main__":
    resume="Python, SQL, React, Git"
    jd="Python, SQL, AWS, Docker, React, System Design"
    print(gap(resume,jd))
    print(learning_path(gap(resume,jd)["missing"]))
