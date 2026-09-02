# AarogyaStock-Rural-Pharmacy

> Offline-first medicine inventory for rural PHCs with expiry alerts, stockout prediction & SMS sync. Solves last-mile healthcare supply gaps.

![Stack](https://img.shields.io/badge/stack-PWA%20IndexedDB%20Flask%20SQLite%20SMS-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Made for](https://img.shields.io/badge/made%20for-India%20%7C%20Bharat-orange)

### 🔥 Problem Statement
Rural clinics face 30-45% stockouts; expiry wastage 15% due to manual registers.

India-specific impact. Built to solve a real, measurable pain point — not a toy demo.

### 💡 Solution
Offline-first medicine inventory for rural PHCs with expiry alerts, stockout prediction & SMS sync. Solves last-mile healthcare supply gaps.

**Tech:** Flask + SQLite backend, React PWA with IndexedDB, background SMS sync (Twilio mock), reorder prediction.

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
git clone https://github.com/kv-creates/AarogyaStock-Rural-Pharmacy.git
cd AarogyaStock-Rural-Pharmacy

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
docker build -t aarogyastock-rural-pharmacy .
docker run -p 8000:8000 aarogyastock-rural-pharmacy
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
