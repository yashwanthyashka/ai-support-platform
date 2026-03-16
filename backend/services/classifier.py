"""
classifier.py — Uses LangChain + OpenAI to:
  1. Classify ticket category & priority
  2. Detect sentiment
  3. Route to the correct team
  4. Auto-answer simple queries
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import json
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import settings
from schemas import AIAnalysis

logger = logging.getLogger(__name__)

# ─── LLM Setup ───────────────────────────────────────────────────────────────

# ─── New ──────────────────────────────────────────────────────────────────────
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=settings.GEMINI_API_KEY,
    request_timeout=30,
)

# ─── Team → Category Mapping (edit as needed) ─────────────────────────────────

TEAM_ROUTING = {
    "billing":   "Billing & Payments Team",
    "refund":    "Billing & Payments Team",
    "technical": "Technical Support Team",
    "bug":       "Technical Support Team",
    "account":   "Account Management Team",
    "shipping":  "Logistics & Shipping Team",
    "general":   "General Support Team",
    "other":     "General Support Team",
}

# ─── Simple FAQ answers ───────────────────────────────────────────────────────

FAQ_ANSWERS = {
    "password_reset": (
        "To reset your password: go to the login page → click 'Forgot Password' → "
        "enter your email → check your inbox for a reset link (valid for 30 min). "
        "If you don't receive the email, check your spam folder."
    ),
    "refund_policy": (
        "Our refund policy: full refunds within 30 days of purchase, no questions asked. "
        "After 30 days, refunds are evaluated case by case. "
        "Please allow 5-7 business days for the amount to appear on your statement."
    ),
    "contact_info": (
        "You can reach us at support@yourcompany.com (24/7) or call +1-800-XXX-XXXX "
        "(Mon–Fri, 9 AM – 6 PM EST). For urgent issues, use the 'Priority Support' "
        "button in your account dashboard."
    ),
}

# ─── Master Prompt ────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """
You are an AI support-ticket analyst for a SaaS company.
Analyze the customer ticket and return a JSON object — nothing else, no markdown, no code fences.

JSON schema (all fields required):
{
  "category":      "<billing|refund|technical|bug|account|shipping|general|other>",
  "sub_category":  "<short descriptive label, e.g. 'payment failed', 'login issue'>",
  "priority":      "<low|medium|high|urgent>",
  "sentiment":     "<positive|neutral|negative|angry>",
  "confidence":    <float 0.0-1.0>,
  "is_simple":     <true if the query can be fully answered with a canned response, else false>,
  "auto_response": "<complete reply to send the customer, or null if is_simple=false>"
}

Priority rules:
- urgent  → production down / data loss / security breach / billing locked out
- high    → major feature broken / repeated failures / refund over $500
- medium  → partial issues / general bugs / standard refund requests
- low     → questions / feedback / feature requests

Auto-response rules (is_simple=true only for):
- Password reset requests
- Refund policy questions
- Contact / office hours questions
- Very generic how-to questions answerable in 2-3 sentences

For auto_response, write a warm, professional reply addressed to the customer by first name.
Start with "Hi <first_name>," and end with "Best regards,\nAI Support Assistant".
""".strip()


# ─── Core function ────────────────────────────────────────────────────────────

async def analyze_ticket(
    subject: str,
    body: str,
    customer_name: str,
) -> AIAnalysis:
    """
    Sends the ticket to GPT-4o-mini and returns a structured AIAnalysis object.
    """
    first_name = customer_name.split()[0] if customer_name else "there"

    human_message = f"""
Customer name: {customer_name}
Subject: {subject}

Message:
{body}
""".strip()

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=human_message),
    ]

    try:
        response = await llm.ainvoke(messages)
        raw = response.content.strip()

        # Strip accidental markdown fences
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        data = json.loads(raw)

        # Map category → assigned team
        category      = data.get("category", "other").lower()
        assigned_team = TEAM_ROUTING.get(category, "General Support Team")

        return AIAnalysis(
            category=category,
            sub_category=data.get("sub_category", ""),
            priority=data.get("priority", "medium"),
            sentiment=data.get("sentiment", "neutral"),
            confidence=float(data.get("confidence", 0.8)),
            assigned_team=assigned_team,
            is_simple=bool(data.get("is_simple", False)),
            auto_response=data.get("auto_response"),
        )

    except json.JSONDecodeError as e:
        logger.error(f"JSON parse error from LLM: {e}\nRaw response: {raw}")
        # Fallback safe defaults
        return AIAnalysis(
            category="other",
            sub_category="parse error",
            priority="medium",
            sentiment="neutral",
            confidence=0.0,
            assigned_team="General Support Team",
            is_simple=False,
            auto_response=None,
        )
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        raise
