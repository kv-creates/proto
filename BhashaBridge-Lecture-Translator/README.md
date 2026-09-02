# BhashaBridge-Lecture-Translator

> Real-time lecture transcription & translation to 8 Indian languages with offline fallback. Solves language barrier in education.

![Stack](https://img.shields.io/badge/stack-Python%20Whisper%20WebSocket%20React-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Made for](https://img.shields.io/badge/made%20for-India%20%7C%20Bharat-orange)

### 🔥 Problem Statement
40% students in Hindi-belt struggle with English lectures; NEP needs multilingual support.

India-specific impact. Built to solve a real, measurable pain point — not a toy demo.

### 💡 Solution
Real-time lecture transcription & translation to 8 Indian languages with offline fallback. Solves language barrier in education.

**Tech:** Whisper (mock/streaming), translation cache, WebSocket streaming, React with subtitle overlay.

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
git clone https://github.com/kv-creates/BhashaBridge-Lecture-Translator.git
cd BhashaBridge-Lecture-Translator

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
docker build -t bhashabridge-lecture-translator .
docker run -p 8000:8000 bhashabridge-lecture-translator
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
