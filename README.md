# AI Customer Support Automation Platform

> Full-stack AI system that classifies tickets, routes them to teams, and auto-answers simple queries.
> Stack: LangChain · FastAPI · PostgreSQL · GPT-4o-mini

***

## Architecture

```
Customer → POST /api/v1/tickets
              │
              ▼
         FastAPI (main.py)
              │
              ├─► PostgreSQL  ← raw ticket saved immediately
              │
              └─► LangChain (classifier.py)
                       │
                       ├─► GPT-4o-mini (classify + sentiment + priority)
                       │
                       ├─► router_service.py  (maps category → team)
                       │
                       └─► Auto-answer? ──yes──► status = auto_resolved
                                        │
                                        no──► status = assigned → team notified
```

### Data Flow per Ticket

1. Customer submits ticket (name, email, subject, body)
2. FastAPI saves raw ticket to PostgreSQL (instant)
3. LangChain sends ticket to GPT-4o-mini for analysis
4. GPT returns: category, sub-category, priority, sentiment, confidence, is\_simple, auto\_response
5. Router maps category → team
6. Ticket updated in DB with all AI-enriched fields
7. Response returned to caller

***

## Keys & Credentials Needed

| Key              | Where to get                           | Used for                        |
| ---------------- | -------------------------------------- | ------------------------------- |
| `OPENAI_API_KEY` | <https://platform.openai.com/api-keys> | GPT-4o-mini calls via LangChain |
| `DATABASE_URL`   | Your PostgreSQL instance               | Ticket & team storage           |
| `APP_SECRET_KEY` | Any random string                      | Future auth/JWT signing         |

### OpenAI Costs (Approximate)

- GPT-4o-mini: \~$0.15 / 1M input tokens, $0.60 / 1M output tokens
- Each ticket analysis: ~~400–600 tokens → \*\*~~$0.0001 per ticket\*\*
- 10,000 tickets/month ≈ **$1 total**

***

## Project Structure

```
ai-support-platform/
├── backend/
│   ├── main.py              ← FastAPI app entry point
│   ├── config.py            ← Pydantic settings (reads .env)
│   ├── database.py          ← SQLAlchemy engine + session
│   ├── models.py            ← Ticket & Team DB models
│   ├── schemas.py           ← Pydantic request/response schemas
│   ├── seed.py              ← Seeds default teams into DB
│   ├── requirements.txt
│   ├── routers/
│   │   ├── tickets.py       ← All ticket endpoints
│   │   └── teams.py         ← Team CRUD endpoints
│   └── services/
│       ├── classifier.py    ← LangChain + GPT-4o-mini brain
│       └── router_service.py← Rule-based team routing
├── frontend/
│   └── index.html           ← Dashboard UI (no framework needed)
└── .env.example
```

***

## Setup & How to Run

### Step 1 — Prerequisites

```bash
# Install Python 3.11+
python --version

# Install PostgreSQL and start it
# Mac:   brew install postgresql && brew services start postgresql
# Ubuntu: sudo apt install postgresql && sudo service postgresql start
# Windows: download from https://www.postgresql.org/download/windows/
```

### Step 2 — Create Database

```bash
# Open psql
psql -U postgres

# Inside psql:
CREATE DATABASE ai_support_db;
\q
```

### Step 3 — Clone & Setup

```bash
git clone <your-repo>
cd ai-support-platform/backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
python -m venv venv
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4 — Configure Environment

```bash
# Copy the example env file
cp ../.env.example .env

# Edit .env with your values
# Windows: notepad .env
# Mac/Linux: nano .env
```

Fill in your `.env`:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/ai_support_db
OPENAI_API_KEY=sk-proj-YOUR_KEY_HERE
APP_SECRET_KEY=any-random-secret-string
APP_ENV=development
```

### Step 5 — Seed the Database

```bash
# Still inside backend/ with venv active
python seed.py
# ✅ Teams seeded successfully.
```

### Step 6 — Run the Server

```bash
python main.py
# OR
uvicorn main:app --reload --port 8000
```

You should see:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

### Step 7 — Open the Dashboard

Open your browser and go to:

- **Dashboard UI:** <http://localhost:8000>  (or open `frontend/index.html` directly)
- **API Docs:**     <http://localhost:8000/docs>
- **ReDoc:**        <http://localhost:8000/redoc>

***

## API Endpoints

| Method | Endpoint                          | Description                                       |
| ------ | --------------------------------- | ------------------------------------------------- |
| POST   | `/api/v1/tickets/`                | Submit new ticket → triggers AI analysis          |
| GET    | `/api/v1/tickets/`                | List tickets (filter by status/category/priority) |
| GET    | `/api/v1/tickets/{id}`            | Get single ticket                                 |
| PATCH  | `/api/v1/tickets/{id}`            | Update ticket (status, agent, notes)              |
| DELETE | `/api/v1/tickets/{id}`            | Delete ticket                                     |
| GET    | `/api/v1/tickets/stats/dashboard` | Dashboard statistics                              |
| GET    | `/api/v1/teams/`                  | List teams                                        |
| POST   | `/api/v1/teams/`                  | Create team                                       |
| GET    | `/health`                         | Health check                                      |

***

## Real-Time Usage Guide

### 1. Submit a ticket via API (curl)

```bash
curl -X POST http://localhost:8000/api/v1/tickets/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Yashwanth Kumar",
    "customer_email": "yash@example.com",
    "subject": "I was charged twice for my subscription",
    "body": "Hi, I noticed two charges of $49 on my card this month for the Pro plan. Can you please refund one of them? My order ID is #ORD-2024-8821."
  }'
```

Expected response:

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

### 2. Submit a simple ticket (auto-resolved)

```bash
curl -X POST http://localhost:8000/api/v1/tickets/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Priya Sharma",
    "customer_email": "priya@example.com",
    "subject": "How do I reset my password?",
    "body": "I forgot my password and cannot log into my account."
  }'
```

Expected: `"is_auto_resolved": true` with a complete auto\_response.

### 3. Filter tickets by priority

```bash
curl "http://localhost:8000/api/v1/tickets/?priority=urgent"
```

### 4. Update a ticket status

```bash
curl -X PATCH http://localhost:8000/api/v1/tickets/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "resolved", "resolution_note": "Refund processed."}'
```

### 5. Dashboard stats

```bash
curl http://localhost:8000/api/v1/tickets/stats/dashboard
```

***

## Customization Guide

### Add new categories

Edit `TEAM_ROUTING` in `services/classifier.py` and `TEAMS` in `services/router_service.py`.

### Change the AI model

In `services/classifier.py`:

```python
llm = ChatOpenAI(model="gpt-4o", ...)  # upgrade to gpt-4o for better accuracy
```

### Add email notifications

Install `fastapi-mail` and trigger emails in `routers/tickets.py` after DB update.

### Add authentication

Install `python-jose` and `passlib`, then add JWT middleware to `main.py`.

### Deploy to production

1. Set `APP_ENV=production` in `.env`
2. Use `gunicorn -k uvicorn.workers.UvicornWorker main:app`
3. Use a managed PostgreSQL (Railway, Supabase, Neon)
4. Deploy to Railway, Render, or a VPS

***

## Resume Talking Points

- Built an AI-powered ticket triage system using **LangChain** and **GPT-4o-mini** that classifies, routes, and auto-resolves support tickets
- Designed a **multi-stage async pipeline**: raw persistence → LLM analysis → rule-based routing → conditional auto-resolution
- Implemented **structured output parsing** from LLM responses with graceful fallbacks for production reliability
- Achieved **\~$0.0001 per ticket** inference cost using prompt-optimized GPT-4o-mini
- Built RESTful API with **FastAPI**, **SQLAlchemy ORM**, and **PostgreSQL** with live dashboard analytics

