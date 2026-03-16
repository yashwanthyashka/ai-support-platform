"""
main.py — AI Customer Support Automation Platform
FastAPI entry point
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import uvicorn

from config import settings
from database import Base, engine
from routers import tickets, teams

# ─── Create all DB tables ─────────────────────────────────────────────────────
Base.metadata.create_all(bind=engine)

# ─── App init ─────────────────────────────────────────────────────────────────
app = FastAPI(
    title="AI Customer Support Automation Platform",
    description="Classifies, routes, and auto-resolves support tickets using LangChain + Gemini-1.5-flash",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ─── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins_list + ["*"],   # lock down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routers ──────────────────────────────────────────────────────────────────
app.include_router(tickets.router, prefix="/api/v1")
app.include_router(teams.router,   prefix="/api/v1")

# ─── Serve frontend (optional) ────────────────────────────────────────────────
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

    @app.get("/", include_in_schema=False)
    def serve_frontend():
        return FileResponse(os.path.join(frontend_dir, "index.html"))


# ─── Health check ─────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "version": "1.0.0"}


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.APP_PORT,
        reload=settings.APP_ENV == "development",
    )
