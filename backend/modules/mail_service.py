"""Mail automation endpoints and orchestration logic."""
from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel


router = APIRouter(prefix="/mail", tags=["mail"])


class EmailSummary(BaseModel):
    subject: str
    sender: str
    received_at: datetime
    summary: str


async def collect_mailbox_digest() -> List[EmailSummary]:
    """Placeholder for IMAP ingestion and LLM summarisation."""
    # In the scaffold we return deterministic sample data for the UI to render.
    return [
        EmailSummary(
            subject="Quarterly security report",
            sender="security@example.com",
            received_at=datetime.utcnow(),
            summary="Highlights of vulnerability scans and mitigations.",
        )
    ]


async def process_incoming_mail() -> None:
    """Stub for the background job that fetches and classifies email."""
    await collect_mailbox_digest()


@router.get("/digest", response_model=List[EmailSummary])
async def get_daily_digest() -> List[EmailSummary]:
    """Return the cached daily digest for display in the dashboard."""
    return await collect_mailbox_digest()


@router.post("/refresh")
async def refresh_mail(background_tasks: BackgroundTasks) -> dict[str, str]:
    """Trigger a background refresh of the mailbox."""
    background_tasks.add_task(process_incoming_mail)
    return {"status": "queued"}
