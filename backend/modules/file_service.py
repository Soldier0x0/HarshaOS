"""File watcher management endpoints."""
from __future__ import annotations

from pathlib import Path
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/files", tags=["files"])


class Rule(BaseModel):
    name: str
    pattern: str
    target_folder: Path


FILE_RULES: list[Rule] = [
    Rule(name="Invoices", pattern=r"invoice_.*\\.pdf", target_folder=Path("exports/invoices")),
    Rule(name="Logs", pattern=r".*\\.log", target_folder=Path("cache/logs")),
]


@router.get("/rules", response_model=List[Rule])
async def list_rules() -> List[Rule]:
    """Return configured regex-based file routing rules."""
    return FILE_RULES


@router.post("/rules", response_model=Rule)
async def add_rule(rule: Rule) -> Rule:
    """Add a new file automation rule to the in-memory registry."""
    FILE_RULES.append(rule)
    return rule
