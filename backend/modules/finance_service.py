"""Finance analytics endpoints."""
from __future__ import annotations

from datetime import date
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/finance", tags=["finance"])


class Transaction(BaseModel):
    id: int
    date: date
    merchant: str
    category: str
    amount: float
    is_subscription: bool = False


class ExpenseSummary(BaseModel):
    category: str
    total: float


@router.get("/transactions", response_model=List[Transaction])
async def list_transactions() -> List[Transaction]:
    """Return mocked transaction data for the initial scaffold."""
    return [
        Transaction(id=1, date=date.today(), merchant="Local Grocery", category="Food", amount=45.30),
        Transaction(id=2, date=date.today(), merchant="Gym Membership", category="Health", amount=29.99, is_subscription=True),
    ]


@router.get("/summary", response_model=List[ExpenseSummary])
async def expense_summary() -> List[ExpenseSummary]:
    """Aggregate totals by category."""
    totals: dict[str, float] = {}
    for txn in await list_transactions():
        totals[txn.category] = totals.get(txn.category, 0.0) + txn.amount
    return [ExpenseSummary(category=cat, total=total) for cat, total in totals.items()]
