from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

engine = create_engine(
    settings.DATABASE_URL.replace("postgresql://", "postgresql+psycopg://").replace("postgresql+psycopg2://", "postgresql+psycopg://"),
    pool_pre_ping=True,       # reconnects on stale connections
    pool_size=10,
    max_overflow=20,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# ─── Dependency ──────────────────────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
