"""
router_service.py — Determines which team and agent gets a ticket.
Currently rule-based on top of the AI category. You can extend this
to query a real agent database or use round-robin assignment.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from schemas import AIAnalysis

# ─── Team definitions ─────────────────────────────────────────────────────────
# Each team has: name, categories it handles, default agent

TEAMS = {
    "billing": {
        "team": "Billing & Payments Team",
        "default_agent": "billing-bot@support.com",
        "sla_hours": 4,
    },
    "refund": {
        "team": "Billing & Payments Team",
        "default_agent": "billing-bot@support.com",
        "sla_hours": 4,
    },
    "technical": {
        "team": "Technical Support Team",
        "default_agent": "tech-bot@support.com",
        "sla_hours": 2,
    },
    "bug": {
        "team": "Technical Support Team",
        "default_agent": "tech-bot@support.com",
        "sla_hours": 2,
    },
    "account": {
        "team": "Account Management Team",
        "default_agent": "accounts-bot@support.com",
        "sla_hours": 8,
    },
    "shipping": {
        "team": "Logistics & Shipping Team",
        "default_agent": "logistics-bot@support.com",
        "sla_hours": 6,
    },
    "general": {
        "team": "General Support Team",
        "default_agent": "general-bot@support.com",
        "sla_hours": 24,
    },
    "other": {
        "team": "General Support Team",
        "default_agent": "general-bot@support.com",
        "sla_hours": 24,
    },
}


def route_ticket(analysis: AIAnalysis) -> dict:
    """
    Returns routing metadata: team name, default agent, SLA hours.
    """
    config = TEAMS.get(analysis.category, TEAMS["other"])

    # Urgent tickets always go to senior agents
    if analysis.priority == "urgent":
        config = config.copy()
        config["default_agent"] = f"senior-{config['default_agent']}"
        config["sla_hours"] = 1

    return {
        "assigned_team":  config["team"],
        "assigned_agent": config["default_agent"],
        "sla_hours":      config["sla_hours"],
    }
