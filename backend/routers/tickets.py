import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from database import get_db
import models, schemas
from services.classifier import analyze_ticket
from services.router_service import route_ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# ─── POST /tickets — Submit a new ticket ─────────────────────────────────────

@router.post("/", response_model=schemas.TicketResponse, status_code=201)
async def create_ticket(payload: schemas.TicketCreate, db: Session = Depends(get_db)):
    """
    1. Save raw ticket to DB
    2. Send to AI for classification, routing, and optional auto-answer
    3. Update ticket with AI results
    4. Return enriched ticket
    """
    # Step 1 — persist raw ticket
    ticket = models.Ticket(**payload.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    # Step 2 — AI analysis
    try:
        analysis = await analyze_ticket(
            subject=ticket.subject,
            body=ticket.body,
            customer_name=ticket.customer_name,
        )

        # Step 3 — routing
        routing = route_ticket(analysis)

        # Step 4 — update ticket
        ticket.category        = analysis.category
        ticket.sub_category    = analysis.sub_category
        ticket.priority        = analysis.priority
        ticket.sentiment       = analysis.sentiment
        ticket.confidence      = analysis.confidence
        ticket.assigned_team   = routing["assigned_team"]
        ticket.assigned_agent  = routing["assigned_agent"]

        if analysis.is_simple and analysis.auto_response:
            ticket.auto_response    = analysis.auto_response
            ticket.is_auto_resolved = True
            ticket.status           = "auto_resolved"
        else:
            ticket.status = "assigned"

        db.commit()
        db.refresh(ticket)

    except Exception as e:
        # Don't fail the whole request — ticket is saved, just not AI-enriched
        ticket.status = "open"
        ticket.resolution_note = f"AI analysis failed: {str(e)}"
        db.commit()
        db.refresh(ticket)

    return ticket


# ─── GET /tickets — List tickets ─────────────────────────────────────────────

@router.get("/", response_model=List[schemas.TicketResponse])
def list_tickets(
    skip:     int = Query(0, ge=0),
    limit:    int = Query(20, le=100),
    status:   Optional[str] = None,
    category: Optional[str] = None,
    priority: Optional[str] = None,
    db: Session = Depends(get_db),
):
    q = db.query(models.Ticket)
    if status:
        q = q.filter(models.Ticket.status == status)
    if category:
        q = q.filter(models.Ticket.category == category)
    if priority:
        q = q.filter(models.Ticket.priority == priority)
    return q.order_by(models.Ticket.created_at.desc()).offset(skip).limit(limit).all()


# ─── GET /tickets/:id ─────────────────────────────────────────────────────────

@router.get("/{ticket_id}", response_model=schemas.TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


# ─── PATCH /tickets/:id — Update status / agent ──────────────────────────────

@router.patch("/{ticket_id}", response_model=schemas.TicketResponse)
def update_ticket(
    ticket_id: int,
    payload: schemas.TicketUpdate,
    db: Session = Depends(get_db),
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(ticket, field, value)

    db.commit()
    db.refresh(ticket)
    return ticket


# ─── DELETE /tickets/:id ──────────────────────────────────────────────────────

@router.delete("/{ticket_id}", status_code=204)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(ticket)
    db.commit()


# ─── GET /tickets/stats/dashboard ────────────────────────────────────────────

@router.get("/stats/dashboard", response_model=schemas.DashboardStats)
def dashboard_stats(db: Session = Depends(get_db)):
    total   = db.query(models.Ticket).count()
    open_   = db.query(models.Ticket).filter(models.Ticket.status == "open").count()
    auto_r  = db.query(models.Ticket).filter(models.Ticket.is_auto_resolved == True).count()
    avg_conf = db.query(func.avg(models.Ticket.confidence)).scalar() or 0.0

    by_cat = {
        r[0]: r[1]
        for r in db.query(models.Ticket.category, func.count()).group_by(models.Ticket.category).all()
        if r[0]
    }
    by_pri = {
        r[0]: r[1]
        for r in db.query(models.Ticket.priority, func.count()).group_by(models.Ticket.priority).all()
        if r[0]
    }
    by_sta = {
        r[0]: r[1]
        for r in db.query(models.Ticket.status, func.count()).group_by(models.Ticket.status).all()
        if r[0]
    }

    return schemas.DashboardStats(
        total_tickets=total,
        open_tickets=open_,
        auto_resolved=auto_r,
        avg_confidence=round(float(avg_conf), 3),
        tickets_by_category=by_cat,
        tickets_by_priority=by_pri,
        tickets_by_status=by_sta,
    )
