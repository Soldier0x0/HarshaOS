"""Expose module routers for simplified import."""
from backend.modules import mail_service, file_service, system_monitor, finance_service, notes_engine, ai_engine

__all__ = [
    "mail_service",
    "file_service",
    "system_monitor",
    "finance_service",
    "notes_engine",
    "ai_engine",
]
