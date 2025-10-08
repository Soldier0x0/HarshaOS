"""APScheduler job registry for HarshaOS."""
from __future__ import annotations

import logging
from typing import Callable

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from backend.modules.mail_service import process_incoming_mail
from backend.modules.system_monitor import get_stats

logger = logging.getLogger("harshaos.scheduler")


def configure_scheduler(scheduler: AsyncIOScheduler, app: FastAPI) -> None:
    """Register periodic jobs on the provided scheduler instance."""
    scheduler.add_job(process_incoming_mail, "interval", minutes=30, id="mail-refresh")
    scheduler.add_job(_log_system_stats(app), "interval", minutes=5, id="system-snapshot")


def _log_system_stats(app: FastAPI) -> Callable[[], None]:
    async def _job() -> None:
        stats = await get_stats()  # type: ignore[func-returns-value]
        logger.info("System snapshot: %s", stats.dict())

    return _job
