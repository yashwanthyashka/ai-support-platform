<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:6366f1,100:8b5cf6&height=200&section=header&text=Triage%20AI&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=AI-Powered%20Customer%20Support%20Automation&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&multiline=true&width=700&height=80&lines=Classify+%E2%86%92+Route+%E2%86%92+Auto-Resolve+%F0%9F%A4%96;Powered+by+LangChain+%2B+Gemini+%2B+FastAPI" alt="Typing SVG" />

<br/>

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20App-6366f1?style=for-the-badge&logoColor=white)](https://ai-support-platform-hn4y.onrender.com)
[![API Docs](https://img.shields.io/badge/📖%20API%20Docs-Swagger%20UI-0ea5e9?style=for-the-badge)](https://ai-support-platform-hn4y.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github)](https://github.com/yashwanthyashka/ai-support-platform)

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat-square&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.2.1-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=flat-square&logo=render&logoColor=white)

</div>

---

<div align="center">

## ⚡ What It Does

</div>

<table>
<tr>
<td width="33%" align="center">

### 🧠 Classify
AI reads every ticket and assigns **category**, **priority**, **sentiment**, and **confidence score** in under 2 seconds.

</td>
<td width="33%" align="center">

### 🎯 Route
Intelligent routing maps each ticket to the right team — Billing, Technical, Logistics, Account, or General Support.

</td>
<td width="33%" align="center">

### ✅ Resolve
Simple queries like password resets and refund policy questions are **auto-answered by AI** — zero human effort.

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║                    TriageAI AI PIPELINE                       ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   Customer  ──►  POST /api/v1/tickets/                           ║
║                        │                                        ║
║                        ▼                                        ║
║              ┌─────────────────┐                                ║
║              │   FastAPI        │  ← Validates request           ║
║              │   (main.py)      │    instantly                   ║
║              └────────┬────────┘                                ║
║                       │                                         ║
║            ┌──────────┴──────────┐                              ║
║            ▼                     ▼                              ║
║     ┌─────────────┐    ┌──────────────────┐                     ║
║     │ PostgreSQL  │    │ Background Task  │                     ║
║     │ (saves raw  │    │                  │                     ║
║     │  ticket)    │    │  LangChain +     │                     ║
║     └─────────────┘    │  Gemini 2.0      │                     ║
║                        │  Flash           │                     ║
║                        └────────┬─────────┘                     ║
║                                 │                               ║
║                    ┌────────────┴────────────┐                  ║
║                    ▼                         ▼                  ║
║             is_simple = true          is_simple = false         ║
║                    │                         │                  ║
║                    ▼                         ▼                  ║
║            AUTO RESOLVED              ASSIGNED TO TEAM          ║
║         (AI writes response)        (Billing / Tech / etc.)     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## ✨ Features

<details>
<summary><b>🤖 AI Classification Engine</b> — click to expand</summary>
<br/>

| Feature | Description |
|---|---|
| **Category Detection** | billing · refund · technical · bug · account · shipping · general · other |
| **Priority Scoring** | low · medium · high · urgent — rule-based on impact |
| **Sentiment Analysis** | positive · neutral · negative · angry |
| **Confidence Score** | 0.0 – 1.0 float for every AI decision |
| **Auto-Resolution** | Password resets, refund policy, contact info — fully AI-answered |
| **Cost** | ~$0.0001 per ticket using Gemini 2.0 Flash |

</details>

<details>
<summary><b>🎯 Smart Routing System</b> — click to expand</summary>
<br/>

| Category | Routed To | SLA |
|---|---|---|
| billing / refund | Billing & Payments Team | 4 hours |
| technical / bug | Technical Support Team | 2 hours |
| account | Account Management Team | 8 hours |
| shipping | Logistics & Shipping Team | 6 hours |
| general / other | General Support Team | 24 hours |
| **urgent** (any) | Senior Agent | **1 hour** |

</details>

<details>
<summary><b>📊 Live Dashboard</b> — click to expand</summary>
<br/>

- **4 stat cards** — Total, Open, Auto-Resolved, AI Confidence
- **By Category** — bar chart with live data
- **By Status** — open / assigned / auto_resolved / resolved
- **Ticket Table** — all 50 latest tickets with color-coded badges
- Zero framework — pure HTML/CSS/JS, no build step needed

</details>

---

## 🗂️ Project Structure

```
TriageAI/
│
├── 📁 backend/
│   ├── 🚀 main.py                ← FastAPI entry point
│   ├── ⚙️  config.py              ← Pydantic settings (.env reader)
│   ├── 🗄️  database.py            ← SQLAlchemy engine + session
│   ├── 📋 models.py              ← Ticket & Team DB models
│   ├── ✅ schemas.py             ← Request/response validation
│   ├── 🌱 seed.py                ← Seeds 5 default teams
│   │
│   ├── 📁 routers/
│   │   ├── 🎫 tickets.py         ← All ticket endpoints + background AI
│   │   └── 👥 teams.py           ← Team CRUD endpoints
│   │
│   └── 📁 services/
│       ├── 🧠 classifier.py      ← LangChain + Gemini brain
│       └── 🗺️  router_service.py  ← Category → Team mapping
│
├── 📁 frontend/
│   └── 🖥️  index.html            ← Full dashboard UI
│
├── 📄 .env.example
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.11+
python --version

# PostgreSQL running
pg_isready
```

### 1️⃣ Clone & Setup

```bash
git clone https://github.com/yashwanthyashka/ai-support-platform.git
cd ai-support-platform/backend

python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 2️⃣ Configure Environment

```bash
cp ../.env.example .env
```

Edit `.env`:

```env
DATABASE_URL=postgresql+psycopg://postgres:yourpassword@localhost:5432/ai_support_db
GEMINI_API_KEY=your-gemini-key-from-aistudio.google.com
APP_SECRET_KEY=any-random-secret
APP_ENV=development
APP_PORT=8000
```

### 3️⃣ Initialize Database

```bash
# Create DB
psql -U postgres -c "CREATE DATABASE ai_support_db;"

# Seed default teams
python seed.py
# ✅ Teams seeded successfully.
```

### 4️⃣ Run

```bash
python main.py
```

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

---

## 🌐 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/tickets/` | Submit ticket → triggers AI pipeline |
| `GET` | `/api/v1/tickets/` | List tickets (filter by status/category/priority) |
| `GET` | `/api/v1/tickets/{id}` | Get single ticket |
| `PATCH` | `/api/v1/tickets/{id}` | Update ticket status / agent / notes |
| `DELETE` | `/api/v1/tickets/{id}` | Delete ticket |
| `GET` | `/api/v1/tickets/stats/dashboard` | Live dashboard stats |
| `GET` | `/api/v1/teams/` | List all teams |
| `POST` | `/api/v1/teams/` | Create a team |
| `GET` | `/health` | Health check |

### Example Request

```bash
curl -X POST https://ai-support-platform-hn4y.onrender.com/api/v1/tickets/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Yashwanth Kumar",
    "customer_email": "yash@example.com",
    "subject": "I was charged twice for my subscription",
    "body": "Hi, I noticed two charges of $49 on my card this month. Please refund one."
  }'
```

### Example Response

```json
{
  "id": 1,
  "category": "billing",
  "sub_category": "duplicate charge",
  "priority": "high",
  "sentiment": "negative",
  "confidence": 0.96,
  "assigned_team": "Billing & Payments Team",
  "status": "assigned",
  "is_auto_resolved": false,
  "auto_response": null
}
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|---|---|---|
| **Framework** | FastAPI 0.111 | Async REST API, auto-docs |
| **AI Orchestration** | LangChain 0.2 | Prompt pipeline + output parsing |
| **LLM** | Gemini 2.0 Flash | Classification + auto-responses |
| **Database** | PostgreSQL 15+ | Ticket & team persistence |
| **ORM** | SQLAlchemy 2.0 | DB models + query builder |
| **Validation** | Pydantic v2 | Request/response schemas |
| **Server** | Uvicorn | ASGI server |
| **DB Driver** | psycopg3 | PostgreSQL Python driver |

</div>

---

## 📈 Performance

<div align="center">

| Metric | Value |
|---|---|
| 💰 Cost per ticket | ~$0.0001 |
| ⚡ API response time | < 1 second |
| 🤖 AI analysis time | 10–20 seconds (background) |
| 📦 Auto-resolve rate | ~30% of tickets |
| 🎯 Classification accuracy | ~95% confidence |

</div>

---

## 🌍 Deployment

Deployed free on:

- **Backend** → [Render.com](https://render.com) (free tier)
- **Database** → [Neon.tech](https://neon.tech) (free PostgreSQL)
- **AI** → [Google Gemini](https://aistudio.google.com) (1500 free requests/day)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8b5cf6,50:6366f1,100:0ea5e9&height=120&section=footer&animation=fadeIn" width="100%"/>

**Built by [Yashwanth](https://github.com/yashwanthyashka)**

⭐ Star this repo if it helped you

[![GitHub stars](https://img.shields.io/github/stars/yashwanthyashka/ai-support-platform?style=social)](https://github.com/yashwanthyashka/ai-support-platform)

</div>
