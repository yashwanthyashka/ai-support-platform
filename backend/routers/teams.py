import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.post("/", response_model=schemas.TeamResponse, status_code=201)
def create_team(payload: schemas.TeamCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Team).filter(models.Team.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Team already exists")
    team = models.Team(**payload.model_dump())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


@router.get("/", response_model=List[schemas.TeamResponse])
def list_teams(db: Session = Depends(get_db)):
    return db.query(models.Team).all()


@router.get("/{team_id}", response_model=schemas.TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.delete("/{team_id}", status_code=204)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(models.Team).filter(models.Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    db.delete(team)
    db.commit()
