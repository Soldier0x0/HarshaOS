"""Entry point for the HarshaOS backend service.

This module wires together the FastAPI application, background scheduler,
and modular routers that expose local-first automation capabilities.
"""
from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from backend.scheduler.jobs import configure_scheduler
from backend.modules import (
    mail_service,
    file_service,
    system_monitor,
    finance_service,
    notes_engine,
    ai_engine,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("harshaos.backend")


def create_app() -> FastAPI:
    """Instantiate the FastAPI app with router registrations."""
    app = FastAPI(
        title="HarshaOS Local API",
        description="Local-first automation and analytics engine for HarshaOS.",
        version="1.1",
    )

    # Allow local Electron frontend to communicate via HTTP/WebSocket.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://127.0.0.1", "*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers from each module.
    app.include_router(mail_service.router)
    app.include_router(file_service.router)
    app.include_router(system_monitor.router)
    app.include_router(finance_service.router)
    app.include_router(notes_engine.router)
    app.include_router(ai_engine.router)

    scheduler = AsyncIOScheduler()
    configure_scheduler(scheduler, app)
    scheduler.start()

    logger.info("HarshaOS backend initialised with scheduled jobs: %s", scheduler.get_jobs())

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    cache_path = Path("cache").resolve()
    cache_path.mkdir(parents=True, exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=9080)
