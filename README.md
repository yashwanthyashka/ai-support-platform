<div align="center">❖ Triage AIAI-Powered Customer Support AutomationClassify → Route → Auto-Resolve • Powered by LangChain, Gemini & FastAPI</div>✦ Core CapabilitiesIntelligent ClassificationPrecision RoutingZero-Touch ResolutionReads every ticket to assign category, priority, sentiment, and confidence scores in under 2 seconds.Intelligently maps each ticket to the correct department (Billing, Technical, Logistics, Account, etc.).Instantly auto-answers routine queries (e.g., password resets, refund policies) requiring zero human intervention.✦ System ArchitecturePlaintext╔══════════════════════════════════════════════════════════════════╗
║                    TriageAI PIPELINE                             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   Customer  ──►  POST /api/v1/tickets/                           ║
║                        │                                         ║
║                        ▼                                         ║
║              ┌─────────────────┐                                 ║
║              │   FastAPI       │  ← Validates request            ║
║              │   (main.py)     │    instantly                    ║
║              └────────┬────────┘                                 ║
║                       │                                          ║
║            ┌──────────┴──────────┐                               ║
║            ▼                     ▼                               ║
║     ┌─────────────┐    ┌──────────────────┐                      ║
║     │ PostgreSQL  │    │ Background Task  │                      ║
║     │ (saves raw  │    │                  │                      ║
║     │  ticket)    │    │  LangChain +     │                      ║
║     └─────────────┘    │  Gemini 2.0      │                      ║
║                        │  Flash           │                      ║
║                        └────────┬─────────┘                      ║
║                                 │                                ║
║                    ┌────────────┴────────────┐                   ║
║                    ▼                         ▼                   ║
║              is_simple = true          is_simple = false         ║
║                    │                         │                   ║
║                    ▼                         ▼                   ║
║              AUTO RESOLVED             ASSIGNED TO TEAM          ║
║           (AI writes response)      (Billing / Tech / etc.)      ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
✦ Platform FeaturesAI Classification EngineDynamic Categorization: Detects intent across billing, refund, technical, bug, account, shipping, general, and other categories.Priority Scoring: Automatically assigns low, medium, high, or urgent status based on business impact rules.Sentiment Analysis: Evaluates customer tone (positive, neutral, negative, angry) to prioritize escalations.Confidence Metrics: Generates a precise 0.0 – 1.0 confidence float for every algorithmic decision.Cost-Efficient: Operates at approximately ~$0.0001 per ticket utilizing Gemini 2.0 Flash.Smart Routing MatrixCategoryDesignated TeamSLA TargetBilling / RefundBilling & Payments4 hoursTechnical / BugTechnical Support2 hoursAccountAccount Management8 hoursShippingLogistics & Shipping6 hoursGeneral / OtherGeneral Support24 hoursUrgent (Any)Senior Escalation Agent1 hourLive DashboardKey Metrics: Real-time tracking of Total, Open, Auto-Resolved, and AI Confidence scores.Data Visualization: Live bar charts categorizing incoming volume.Status Tracking: Segmented views for open, assigned, auto-resolved, and resolved tickets.Lightweight: Built with pure HTML/CSS/JS—zero framework or build steps required.✦ System PerformanceMetricTarget ValueCost per ticket~$0.0001API response time< 1 secondAI analysis time10–20 seconds (background)Auto-resolve rate~30% of standard ticketsClassification accuracy~95% baseline confidence✦ Project StructurePlaintextTriageAI/
├── backend/
│   ├── main.py              # FastAPI entry point
│   ├── config.py            # Pydantic settings (.env reader)
│   ├── database.py          # SQLAlchemy engine + session
│   ├── models.py            # Ticket & Team DB models
│   ├── schemas.py           # Request/response validation
│   ├── seed.py              # Seeds default teams
│   │
│   ├── routers/
│   │   ├── tickets.py       # Ticket endpoints & background AI
│   │   └── teams.py         # Team CRUD endpoints
│   │
│   └── services/
│       ├── classifier.py    # LangChain + Gemini orchestration
│       └── router_service.py# Category-to-Team mapping logic
│
├── frontend/
│   └── index.html           # Standalone dashboard UI
│
├── .env.example
├── requirements.txt
└── README.md
✦ Quick Start1. PrerequisitesEnsure you have Python 3.11+ and an active PostgreSQL instance running.2. Clone & SetupBashgit clone https://github.com/yashwanthyashka/ai-support-platform.git
cd ai-support-platform/backend

python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

pip install -r requirements.txt
3. Environment ConfigurationCreate a .env file from the provided example:Bashcp ../.env.example .env
Update .env with your credentials:Code snippetDATABASE_URL=postgresql+psycopg://postgres:yourpassword@localhost:5432/ai_support_db
GEMINI_API_KEY=your-gemini-key-from-aistudio.google.com
APP_SECRET_KEY=your-secure-random-secret
APP_ENV=development
APP_PORT=8000
4. Database InitializationBash# Create the database instance
psql -U postgres -c "CREATE DATABASE ai_support_db;"

# Seed default organizational teams
python seed.py
5. Launch the ApplicationBashpython main.py
✦ API ReferenceMethodEndpointDescriptionPOST/api/v1/tickets/Submit a ticket & trigger the AI pipelineGET/api/v1/tickets/List tickets (supports status/category/priority filtering)GET/api/v1/tickets/{id}Retrieve a specific ticketPATCH/api/v1/tickets/{id}Update ticket status, agent assignment, or notesDELETE/api/v1/tickets/{id}Remove a ticketGET/api/v1/tickets/statsFetch live dashboard statisticsGET/api/v1/teams/List all available routing teams<details><summary><b>View Example Payload & Response</b></summary>Request:Bashcurl -X POST https://ai-support-platform-hn4y.onrender.com/api/v1/tickets/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Yashwanth Kumar",
    "customer_email": "yash@example.com",
    "subject": "I was charged twice for my subscription",
    "body": "Hi, I noticed two charges of $49 on my card this month. Please refund one."
  }'
Response:JSON{
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
</details>✦ Deployment InfrastructureThis application is optimized for lightweight, cost-effective hosting:Compute: Render.comDatabase: Neon.tech (Serverless PostgreSQL)LLM Provider: Google AI Studio<div align="center">Triage AI • Designed and developed by <a href="https://github.com/yashwanthyashka">Yashwanth</a>.<i>Released under the MIT License.</i></div>
