# 🚨 Virtual Crisis Intelligence Platform
> **Autonomous Ingestion, Geospatial Mapping & Parametric Disaster Triage for Emergency Response**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Leaflet.js](https://img.shields.io/badge/Leaflet-1.9.4-199900?style=for-the-badge&logo=leaflet&logoColor=white)](https://leafletjs.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Google Gemini API](https://img.shields.io/badge/AI%20Engine-Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com/)

---

## ⚡ What We Built

It is an autonomous disaster intelligence dashboard designed for first responders, emergency operations centers (EOCs), and relief agencies (NDRF, FEMA, Red Cross). 

A coordinator inputs an unstructured incident scenario, and the engine dynamically generates:
* 🗺️ **Interactive Triage Map:** Centered geospatial map with colored severity zones (Red/Orange/Yellow) and an intensity heatmap.
* 📦 **Parametric Resource Needs:** AI-calculated requirements for blood units, temporary shelters, NDRF teams, and medevac airlifts.
* ⏱️ **NDMA Phase Timeline:** Interactive, checkable 3-tier action protocol (Immediate $\rightarrow$ Short-Term $\rightarrow$ Recovery).
* 📋 **Tactical SITREP & Regional Contacts:** Official timestamped situation report with regional emergency contact rosters.

> **Live Demo Flow:**  
> Type *"Flood in Assam, 3 districts affected, 50000 displaced"* $\rightarrow$ Click **Run AI Simulation** $\rightarrow$ Map auto-focuses to Assam coordinates, heatmap renders, and all operational metrics populate in under 3 seconds.

---

## 📌 Problem & Impact

* **The Bottleneck:** During the "Golden Hour" following a natural disaster, relief coordinators lose critical hours manually aggregating damage reports, extracting coordinates, and establishing communication trees.
* **The Reality:** The first 6 hours dictate survival rates, but conventional field assessment takes 24–72 hours.
* **The NEXUS Solution:** Replaces hours of manual triage with a single structured simulation engine. **This is decision infrastructure, not a chatbot.**

---

## 🏗️ System Architecture

    [ Unstructured Natural Language Feed / Scenario Input ]
                             │
                             ▼
    ┌────────────────────────────────────────────────────────┐
    │               Flask Ingestion Layer                    │
    │       (REST Endpoint: POST /api/generate)              │
    └────────────────────────┬───────────────────────────────┘
                             │
                             ▼
    ┌────────────────────────────────────────────────────────┐
    │               Gemini Intelligence Engine               │
    │   • Spatial Geocoding & Lat/Long Coordinate Deduction  │
    │   • Parametric Supply & Logistics Calculations         │
    │   • Strict JSON Schema Validation                      │
    └────────────────────────┬───────────────────────────────┘
                             │ (JSON Payload)
                             ▼
    ┌────────────────────────────────────────────────────────┐
    │            Interactive Front-End Dashboard             │
    │   • Leaflet.js Vector Map + CartoDB Dark Tiles         │
    │   • Dynamic Heatmap Gaussian Dispersion                │
    │   • NDMA Tactical Directives & State Contact Matrix    │
    └────────────────────────────────────────────────────────┘

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | HTML5, Vanilla JavaScript, CSS3 | Single-file, zero-build lightweight frontend |
| **Styling** | Bootstrap 5.3 (Dark Theme) + Custom CSS | High-contrast command center UI |
| **Mapping Engine**| Leaflet.js (CDN) + Leaflet.heat | Dynamic tile rendering and geospatial heatmap clustering[cite: 1] |
| **Backend** | Python 3 + Flask + Flask-CORS | REST API handling prompt orchestration & parsing[cite: 1] |
| **AI Intelligence**| Google Gemini API (`gemini-2.5-flash`) | Rapid spatial deduction and structured JSON triage generation |

---

## 📁 Repository Structure

    livecrisis_dashboard/
    ├── index.html              # Full dashboard frontend (Single file)
    ├── .gitignore              # Ignores .env and virtual environments
    ├── README.md               # Main project documentation
    └── backend/
        ├── app.py              # Flask backend server & AI prompt logic
        ├── requirements.txt    # Python dependencies
        ├── .env.example        # Environment variable template
        └── README.md           # Backend-specific instructions
[cite: 1]
### 1. Start the Flask Backend
```
 bash
cd backend
pip install -r requirements.txt

# Create your .env file with your Gemini API key
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

# Run the Flask API server
python app.py
# Server initializes on [http://127.0.0.1:5000](http://127.0.0.1:5000)
```
### 2. Start the Frontend Server (In a separate terminal)
```
# From the root directory:
python -m http.server 3000
# Open http://localhost:3000 in your browser
```



🎯 Key Features Breakdown
[x] Autonomous Geocoding: Infers exact latitude/longitude coordinates directly from regional place names[cite: 1].

[x] Dynamic Heatmap Generation: Generates synthetic geospatial dispersion patterns around the crisis epicenter[cite: 1].

[x] NDMA-Compliant Triage Directives: Categorizes operational procedures into standardized Immediate, Short-Term, and Recovery phases[cite: 1].

[x] High-Contrast Dark Command UI: Purpose-built for low-light Emergency Operations Centers (EOCs)[cite: 1].

[x] State-Specific Emergency Routing: Dynamically supplies verified state-level emergency dispatch numbers[cite: 1].
---


🔮 Roadmap / Future Scope
[ ] Satellite Raster Ingestion: Direct integration with Copernicus / Sentinel-2 open API for automated optical damage assessment[cite: 1].

[ ] Decentralized Mesh Sync: Offline sync using WebRTC/LoRaWAN for field coordinators in zero-connectivity zones[cite: 1].

[ ] Automated PDF SITREP Export: One-click dispatch brief generator for field commanders[cite: 1].

👥 Team
Built in an overnight sprint for the 2026 Open Innovation Hackathon[cite: 1].

Repository: github.com/tonyadhikary/livecrisis_dashboard

[cite: 1]
