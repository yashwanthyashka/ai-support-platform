from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# ─── Ticket Schemas ───────────────────────────────────────────────────────────

class TicketCreate(BaseModel):
    customer_name:  str = Field(..., min_length=1, max_length=150)
    customer_email: EmailStr
    subject:        str = Field(..., min_length=3, max_length=500)
    body:           str = Field(..., min_length=10)


class TicketUpdate(BaseModel):
    status:          Optional[str] = None
    assigned_team:   Optional[str] = None
    assigned_agent:  Optional[str] = None
    resolution_note: Optional[str] = None


class TicketResponse(BaseModel):
    id:               int
    customer_name:    str
    customer_email:   str
    subject:          str
    body:             str
    category:         Optional[str]
    sub_category:     Optional[str]
    priority:         Optional[str]
    sentiment:        Optional[str]
    confidence:       Optional[float]
    assigned_team:    Optional[str]
    assigned_agent:   Optional[str]
    status:           str
    auto_response:    Optional[str]
    is_auto_resolved: bool
    resolution_note:  Optional[str]
    created_at:       datetime
    updated_at:       Optional[datetime]

    model_config = {"from_attributes": True}


# ─── AI Analysis Schema ───────────────────────────────────────────────────────

class AIAnalysis(BaseModel):
    category:       str
    sub_category:   str
    priority:       str
    sentiment:      str
    confidence:     float
    assigned_team:  str
    is_simple:      bool          # can be auto-answered?
    auto_response:  Optional[str] # filled if is_simple=True


# ─── Team Schemas ─────────────────────────────────────────────────────────────

class TeamCreate(BaseModel):
    name:        str
    description: Optional[str] = None
    categories:  Optional[str] = None
    email:       Optional[str] = None


class TeamResponse(BaseModel):
    id:          int
    name:        str
    description: Optional[str]
    categories:  Optional[str]
    email:       Optional[str]
    created_at:  datetime

    model_config = {"from_attributes": True}


# ─── Stats Schema ─────────────────────────────────────────────────────────────

class DashboardStats(BaseModel):
    total_tickets:       int
    open_tickets:        int
    auto_resolved:       int
    avg_confidence:      float
    tickets_by_category: dict
    tickets_by_priority: dict
    tickets_by_status:   dict
