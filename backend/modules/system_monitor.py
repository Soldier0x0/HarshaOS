"""System telemetry endpoints for HarshaOS."""
from __future__ import annotations

import platform
import psutil
from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/system", tags=["system"])


class SystemStats(BaseModel):
    hostname: str
    os: str
    uptime_seconds: float
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    timestamp: datetime


@router.get("/stats", response_model=SystemStats)
async def get_stats() -> SystemStats:
    """Collect local system metrics."""
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = (datetime.utcnow() - boot_time).total_seconds()
    return SystemStats(
        hostname=platform.node(),
        os=f"{platform.system()} {platform.release()}",
        uptime_seconds=uptime,
        cpu_percent=psutil.cpu_percent(interval=None),
        memory_percent=psutil.virtual_memory().percent,
        disk_percent=psutil.disk_usage("/").percent,
        timestamp=datetime.utcnow(),
    )
