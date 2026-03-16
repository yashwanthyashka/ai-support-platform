"""
seed.py — Seeds the database with default teams.
Run: python seed.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

TEAMS = [
    {"name": "Billing & Payments Team",  "categories": "billing,refund",      "email": "billing@support.com",   "description": "Handles all billing, invoices, and refund requests"},
    {"name": "Technical Support Team",   "categories": "technical,bug",        "email": "tech@support.com",      "description": "Resolves technical issues, bugs, and integration problems"},
    {"name": "Account Management Team",  "categories": "account",              "email": "accounts@support.com",  "description": "Manages account access, upgrades, and security"},
    {"name": "Logistics & Shipping Team","categories": "shipping",             "email": "logistics@support.com", "description": "Tracks orders and resolves shipping issues"},
    {"name": "General Support Team",     "categories": "general,other",        "email": "general@support.com",   "description": "Handles all other inquiries"},
]

db = SessionLocal()
try:
    for t in TEAMS:
        exists = db.query(models.Team).filter(models.Team.name == t["name"]).first()
        if not exists:
            db.add(models.Team(**t))
    db.commit()
    print("✅ Teams seeded successfully.")
finally:
    db.close()
