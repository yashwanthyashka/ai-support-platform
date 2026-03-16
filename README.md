<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:020817,30:0f172a,60:1e1b4b,100:312e81&height=280&section=header&text=TriageAI&fontSize=90&fontColor=a5b4fc&fontAlignY=42&desc=AI-Powered%20Customer%20Support%20Automation&descAlignY=62&descSize=20&animation=fadeIn&stroke=6366f1&strokeWidth=2" width="100%"/>

</div>

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Syne&weight=700&size=24&duration=2800&pause=1200&color=818CF8&center=true&vCenter=true&multiline=false&width=680&height=60&lines=Classify+%E2%86%92+Route+%E2%86%92+Auto-Resolve+in+%3C1s+%E2%9A%A1;LangChain+%2B+Gemini+2.0+Flash+%2B+FastAPI+%F0%9F%A4%96;~%240.0001+per+ticket+%C2%B7+95%25+Accuracy+%F0%9F%8E%AF;Built+for+Scale.+Designed+for+Speed.+%F0%9F%9A%80" alt="Typing SVG" />

</div>

<br/>

<div align="center">

[![Live Demo](https://img.shields.io/badge/%E2%9A%A1%20Live%20Demo-Visit%20App-818cf8?style=for-the-badge&labelColor=1e1b4b&logoColor=white)](https://ai-support-platform-hn4y.onrender.com)&nbsp;&nbsp;
[![API Docs](https://img.shields.io/badge/%F0%9F%93%96%20Swagger%20UI-API%20Docs-6366f1?style=for-the-badge&labelColor=1e1b4b)](https://ai-support-platform-hn4y.onrender.com/docs)&nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/%E2%98%85%20Source%20Code-GitHub-a5b4fc?style=for-the-badge&labelColor=1e1b4b&logo=github)](https://github.com/yashwanthyashka/ai-support-platform)

</div>

<br/>

<div align="center">

![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI_0.111-009688?style=flat-square&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain_0.2-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-4285F4?style=flat-square&logo=google&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on_Render-46E3B7?style=flat-square&logo=render&logoColor=black)

</div>

---

<br/>

<div align="center">

```
                              ╭──────────────────────────────────────────────────────────────────────╮
                              │                                                                      │
                              │        ████████╗██████╗ ██╗ █████╗  ██████╗ ███████╗                 │
                              │           ██╔══╝██╔══██╗██║██╔══██╗██╔════╝ ██╔════╝                 │
                              │           ██║   ██████╔╝██║███████║██║  ███╗█████╗                   │
                              │           ██║   ██╔══██╗██║██╔══██║██║   ██║██╔══╝                   │
                              │           ██║   ██║  ██║██║██║  ██║╚██████╔╝███████╗                 │
                              │           ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝                 │
                              │                                                                      │
                              │     A  I   ·   S  U  P  P  O  R  T   ·   P  L  A  T  F  O  R  M      │
                              │                                                                      │
                              ╰──────────────────────────────────────────────────────────────────────╯
```

</div>

<br/>

---

## ✦ What It Does

<br/>

<div align="center">

|  | CLASSIFY | ROUTE | RESOLVE |
|:---:|:---:|:---:|:---:|
| **Icon** | 🧠 | 🎯 | ✅ |
| **What** | Reads every ticket and assigns category, priority, sentiment & confidence | Maps each ticket to the right team — Billing, Technical, Logistics, Account | Simple queries auto-answered by AI — zero human effort |
| **Speed** | < 2 seconds | Instant | Background task |
| **Accuracy** | ~95% confidence | Rule-based deterministic | ~30% auto-resolve rate |

</div>

<br/>

---

## ✦ Performance at a Glance

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f172a,100:1e1b4b&height=3&section=header" width="100%"/>

</div>

<br/>

<div align="center">

```
┌─────────────────────┬─────────────────────┬─────────────────────┬─────────────────────┐
│  💰 Cost/Ticket      │  ⚡ API Response     │  🤖 AI Analysis      │  🎯 Accuracy         │
│                     │                     │                     │                     │
│    ~$0.0001          │    < 1 second        │    10–20 seconds     │    ~95% confidence   │
│   (Gemini Flash)    │   (non-blocking)    │   (background)      │   (classification)  │
└─────────────────────┴─────────────────────┴─────────────────────┴─────────────────────┘
```

</div>

<br/>

---

## ✦ System Architecture

<br/>

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    ◈  T R I A G E A I   P I P E L I N E  ◈              ║
║                                                                           ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   👤 Customer  ──────►  POST /api/v1/tickets/                             ║
║                                    │                                     ║
║                                    ▼                                     ║
║                        ┌───────────────────────┐                         ║
║                        │       FastAPI          │  ← Instant validation  ║
║                        │      (main.py)         │    + 200 OK response   ║
║                        └───────────┬───────────┘                         ║
║                                    │                                     ║
║                    ┌───────────────┴───────────────┐                     ║
║                    ▼                               ▼                     ║
║          ┌──────────────────┐         ┌────────────────────────┐         ║
║          │   PostgreSQL      │         │    Background Task      │         ║
║          │                  │         │                        │         ║
║          │  saves raw ticket│         │   LangChain Pipeline   │         ║
║          │  immediately ✓   │         │   + Gemini 2.0 Flash   │         ║
║          └──────────────────┘         └────────────┬───────────┘         ║
║                                                    │                     ║
║                             ┌──────────────────────┤                     ║
║                             │                      │                     ║
║                    is_simple = true        is_simple = false             ║
║                             │                      │                     ║
║                             ▼                      ▼                     ║
║                   ╔══════════════════╗   ╔══════════════════════╗        ║
║                   ║  AUTO RESOLVED   ║   ║   ASSIGNED TO TEAM   ║        ║
║                   ║                 ║   ║                      ║        ║
║                   ║ AI writes full  ║   ║  Billing · Technical ║        ║
║                   ║ response ✨      ║   ║  Logistics · Account ║        ║
║                   ╚══════════════════╝   ╚══════════════════════╝        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## ✦ Features

<br/>

<details>
<summary><b>🧠 &nbsp; AI Classification Engine</b> &nbsp;—&nbsp; click to expand</summary>

<br/>

<div align="center">

```
  ◆  CLASSIFICATION CAPABILITIES  ◆
```

</div>

| Feature | Details |
|---|---|
| **Category Detection** | `billing` · `refund` · `technical` · `bug` · `account` · `shipping` · `general` · `other` |
| **Priority Scoring** | `low` · `medium` · `high` · `urgent` — rule-based on business impact |
| **Sentiment Analysis** | `positive` · `neutral` · `negative` · `angry` |
| **Confidence Score** | `0.0 – 1.0` float returned with every AI decision |
| **Auto-Resolution** | Password resets, refund policy, contact info — fully AI-answered |
| **Sub-Category** | Fine-grained labeling within each category |
| **Cost** | ~`$0.0001` per ticket using Gemini 2.0 Flash |

</details>

<br/>

<details>
<summary><b>🎯 &nbsp; Smart Routing System</b> &nbsp;—&nbsp; click to expand</summary>

<br/>

<div align="center">

```
  ◆  SLA ROUTING MATRIX  ◆
```

</div>

| Category Detected | Routed To | SLA Target |
|---|---|:---:|
| `billing` / `refund` | 💳 Billing & Payments Team | **4 hours** |
| `technical` / `bug` | 🔧 Technical Support Team | **2 hours** |
| `account` | 👤 Account Management Team | **8 hours** |
| `shipping` | 📦 Logistics & Shipping Team | **6 hours** |
| `general` / `other` | 🎧 General Support Team | **24 hours** |
| ⚠️ `urgent` (any) | 🔴 Senior Agent Override | **1 hour** |

</details>

<br/>

<details>
<summary><b>📊 &nbsp; Live Dashboard</b> &nbsp;—&nbsp; click to expand</summary>

<br/>

- **4 Stat Cards** — Total · Open · Auto-Resolved · AI Confidence average
- **By Category** — bar chart with live polling from the database
- **By Status** — `open` / `assigned` / `auto_resolved` / `resolved`
- **Ticket Table** — latest 50 tickets with color-coded priority badges
- **Zero Dependencies** — pure HTML / CSS / JS, no build step, no framework

</details>

<br/>

---

## ✦ Project Structure

<br/>

```
TriageAI/
│
├── 📁 backend/
│   │
│   ├── 🚀  main.py                ←  FastAPI app entry point
│   ├── ⚙️   config.py              ←  Pydantic settings (.env reader)
│   ├── 🗄️   database.py            ←  SQLAlchemy engine + session factory
│   ├── 📋  models.py              ←  Ticket & Team ORM models
│   ├── ✅  schemas.py             ←  Pydantic request / response schemas
│   ├── 🌱  seed.py                ←  Seeds 5 default support teams
│   │
│   ├── 📁 routers/
│   │   ├── 🎫  tickets.py         ←  All ticket endpoints + background AI task
│   │   └── 👥  teams.py           ←  Team CRUD endpoints
│   │
│   └── 📁 services/
│       ├── 🧠  classifier.py      ←  LangChain + Gemini classification brain
│       └── 🗺️   router_service.py  ←  Category → Team assignment logic
│
├── 📁 frontend/
│   └── 🖥️   index.html            ←  Full dashboard UI (zero dependencies)
│
├── 📄 .env.example
├── 📄 requirements.txt
└── 📄 README.md
```

<br/>

---

## ✦ Quick Start

<br/>

### Prerequisites

```bash
python --version   # 3.11+
pg_isready         # PostgreSQL must be running
```

<br/>

### 1 · Clone & Setup

```bash
git clone https://github.com/yashwanthyashka/ai-support-platform.git
cd ai-support-platform/backend

python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows

pip install -r requirements.txt
```

<br/>

### 2 · Configure Environment

```bash
cp ../.env.example .env
```

```env
DATABASE_URL=postgresql+psycopg://postgres:yourpassword@localhost:5432/ai_support_db
GEMINI_API_KEY=your-gemini-key-from-aistudio.google.com
APP_SECRET_KEY=any-random-secret
APP_ENV=development
APP_PORT=8000
```

<br/>

### 3 · Initialize Database

```bash
psql -U postgres -c "CREATE DATABASE ai_support_db;"
python seed.py
# ✅ Teams seeded successfully.
```

<br/>

### 4 · Launch

```bash
python main.py
```

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

<br/>

---

## ✦ API Reference

<br/>

<div align="center">

```
  ◆  ENDPOINTS  ◆
```

</div>

| Method | Endpoint | Description |
|:---:|---|---|
| `POST` | `/api/v1/tickets/` | Submit ticket → triggers full AI pipeline |
| `GET` | `/api/v1/tickets/` | List tickets — filter by status / category / priority |
| `GET` | `/api/v1/tickets/{id}` | Retrieve a single ticket by ID |
| `PATCH` | `/api/v1/tickets/{id}` | Update status · assigned agent · internal notes |
| `DELETE` | `/api/v1/tickets/{id}` | Delete a ticket record |
| `GET` | `/api/v1/tickets/stats/dashboard` | Live dashboard stats (charts + KPIs) |
| `GET` | `/api/v1/teams/` | List all support teams |
| `POST` | `/api/v1/teams/` | Create a new support team |
| `GET` | `/health` | Health check |

<br/>

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

<br/>

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

<br/>

---

## ✦ Tech Stack

<br/>

<div align="center">

[![My Skills](https://skillicons.dev/icons?i=python,fastapi,postgresql,googlecloud,docker,github&theme=dark)](https://skillicons.dev)

</div>

<br/>

<div align="center">

| Layer | Technology | Role |
|---|---|---|
| **Framework** | FastAPI 0.111 | Async REST API, auto-generated Swagger docs |
| **AI Orchestration** | LangChain 0.2 | Prompt pipeline, output parsing, chain management |
| **LLM** | Gemini 2.0 Flash | Ticket classification + AI auto-responses |
| **Database** | PostgreSQL 15+ | Persistent storage for tickets and teams |
| **ORM** | SQLAlchemy 2.0 | Type-safe DB models and query builder |
| **Validation** | Pydantic v2 | Request / response schema enforcement |
| **Server** | Uvicorn | High-performance ASGI server |
| **DB Driver** | psycopg3 | Modern async PostgreSQL Python driver |

</div>

<br/>

---

## ✦ Deployment

<br/>

<div align="center">

```
  ◆  FREE-TIER PRODUCTION STACK  ◆

     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
     │   Render.com   │     │   Neon.tech    │     │  Grok AI       │
     │                │     │                │     │                │
     │   Backend API  │────►│  PostgreSQL    │  +  │                │
     │   (Free Tier)  │     │  (Free Tier)   │     │  Grok ai       │
     │                │     │                │     │  1500 req/day  │
     └────────────────┘     └────────────────┘     └────────────────┘
```

</div>

<br/>

---

## ✦ License

MIT License — free to use, modify, and distribute.

<br/>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:312e81,50:1e1b4b,100:020817&height=200&section=footer&text=Built%20by%20Yashwanth&fontSize=42&fontColor=818cf8&fontAlignY=55&animation=fadeIn&desc=github.com%2Fyashwanthyashka&descAlignY=75&descSize=16&descColor=6366f1" width="100%"/>

</div>

<div align="center">

<br/>

[![GitHub stars](https://img.shields.io/github/stars/yashwanthyashka/ai-support-platform?style=social&label=⭐%20Star%20this%20repo)](https://github.com/yashwanthyashka/ai-support-platform)

<br/>

*If this project helped you, a star means everything — thank you.*

</div>
