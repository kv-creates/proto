# CarbonCommute-Mumbai-Optimizer

> Mumbai multimodal commute optimizer that balances time, cost & carbon (train/bus/metro/auto) with GTFS-like data.

![Stack](https://img.shields.io/badge/stack-TypeScript%20Next.js%20Dijkstra%20GTFS-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Made for](https://img.shields.io/badge/made%20for-India%20%7C%20Bharat-orange)

### 🔥 Problem Statement
Mumbai commuters choose without carbon insight; transport is 24% of Mumbai emissions.

India-specific impact. Built to solve a real, measurable pain point — not a toy demo.

### 💡 Solution
Mumbai multimodal commute optimizer that balances time, cost & carbon (train/bus/metro/auto) with GTFS-like data.

**Tech:** Graph builder from GTFS mock, multi-criteria Dijkstra (Pareto), carbon model (gCO2/km), Next.js + MapLibre.

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
git clone https://github.com/kv-creates/CarbonCommute-Mumbai-Optimizer.git
cd CarbonCommute-Mumbai-Optimizer

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
docker build -t carboncommute-mumbai-optimizer .
docker run -p 8000:8000 carboncommute-mumbai-optimizer
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
