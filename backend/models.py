from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float
from sqlalchemy.sql import func
from database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id              = Column(Integer, primary_key=True, index=True)
    customer_name   = Column(String(150), nullable=False)
    customer_email  = Column(String(250), nullable=False, index=True)
    subject         = Column(String(500), nullable=False)
    body            = Column(Text, nullable=False)

    # AI-populated fields
    category        = Column(String(80),  nullable=True)   # billing, technical, general …
    sub_category    = Column(String(120), nullable=True)   # more granular label
    priority        = Column(String(20),  default="medium")  # low / medium / high / urgent
    sentiment       = Column(String(20),  nullable=True)   # positive / neutral / negative
    confidence      = Column(Float,       nullable=True)   # 0.0 – 1.0 classification confidence

    # Routing
    assigned_team   = Column(String(150), nullable=True)
    assigned_agent  = Column(String(150), nullable=True)

    # Resolution
    status          = Column(String(50),  default="open")
    auto_response   = Column(Text,        nullable=True)
    is_auto_resolved = Column(Boolean,   default=False)
    resolution_note = Column(Text,        nullable=True)

    # Timestamps
    created_at      = Column(DateTime(timezone=True), server_default=func.now())
    updated_at      = Column(DateTime(timezone=True), onupdate=func.now())


class Team(Base):
    __tablename__ = "teams"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(150), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    categories  = Column(Text, nullable=True)   # comma-separated list of categories this team handles
    email       = Column(String(250), nullable=True)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
