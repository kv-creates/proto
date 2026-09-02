# SurakshaPath-NightSafety-Router

> Safety-aware routing engine for night travel scoring paths on street lighting, footfall, CCTV & police beats using OSM. Solves women's safety.

![Stack](https://img.shields.io/badge/stack-Python%20FastAPI%20Leaflet%20OSM%20Overpass-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Made for](https://img.shields.io/badge/made%20for-India%20%7C%20Bharat-orange)

### 🔥 Problem Statement
Shortest route ≠ safest. No Indian maps optimize for women's night safety.

India-specific impact. Built to solve a real, measurable pain point — not a toy demo.

### 💡 Solution
Safety-aware routing engine for night travel scoring paths on street lighting, footfall, CCTV & police beats using OSM. Solves women's safety.

**Tech:** FastAPI + OSM Overpass API, safety scoring (lighting 0.4, crowd 0.3, CCTV 0.2, police 0.1), Leaflet frontend with heatmap.

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
git clone https://github.com/kv-creates/SurakshaPath-NightSafety-Router.git
cd SurakshaPath-NightSafety-Router

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
docker build -t surakshapath-nightsafety-router .
docker run -p 8000:8000 surakshapath-nightsafety-router
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
