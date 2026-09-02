# RozgarSetu-SkillGap-Mapper

> AI mapper that extracts skills from resume vs JD, quantifies gaps & generates personalized 30/60/90-day learning path.

![Stack](https://img.shields.io/badge/stack-Python%20spaCy%20React%20NLP-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Made for](https://img.shields.io/badge/made%20for-India%20%7C%20Bharat-orange)

### 🔥 Problem Statement
Tier 2/3 students don't know why they get rejected; generic courses waste time.

India-specific impact. Built to solve a real, measurable pain point — not a toy demo.

### 💡 Solution
AI mapper that extracts skills from resume vs JD, quantifies gaps & generates personalized 30/60/90-day learning path.

**Tech:** Skill NER (spaCy + custom lexicon 1200 skills), TF-IDF gap scoring, roadmap generator with YouTube/course links.

### 🏗️ Architecture
```
User -> Frontend (React/PWA/Leaflet) -> API (FastAPI/Flask/Node) -> Core Engine
                                                      -> Offline Store (IndexedDB/SQLite)
                                                      -> Sync Layer (SMS/MQTT/WebSocket)
                                                      -> Scoring/ML Module
```

### ✨ Key Features
- Offline-first where it matters (rural, low-connectivity)
- Explainable scoring / risk highlighting (no black-box)
- Hindi/Marathi aware where applicable
- Production-grade error handling, tests, Docker
- <100ms local inference path

### 🚀 Quick Start
```bash
# clone
git clone https://github.com/kv-creates/RozgarSetu-SkillGap-Mapper.git
cd RozgarSetu-SkillGap-Mapper

# python projects
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.main

# node projects
npm install
npm run dev   # or npm start
```

### 🧪 Tests
```bash
pytest -q
# or
npm test
```

### 📸 Demo
See `demo/` folder for sample inputs/outputs and `src/` for core logic.
Run `python -m src.main --demo` or `npm run demo` for a live demo in terminal.

### 🐳 Docker
```bash
docker build -t rozgarsetu-skillgap-mapper .
docker run -p 8000:8000 rozgarsetu-skillgap-mapper
```

### 🗺️ Roadmap
- [ ] Pilot with 10 real users & collect feedback
- [ ] Add regional language support expansion
- [ ] Deploy on BHIM/UPI/civic stack integration

### 🤝 Contributing
PRs welcome. Please run tests before submitting.

### 📄 License
MIT — see [LICENSE](./LICENSE)

---
Built with ❤️ by [kv-creates](https://github.com/kv-creates) for Bharat.
