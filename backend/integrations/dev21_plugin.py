"""Stub connector generator for 21st.dev schemas."""
from __future__ import annotations

from pathlib import Path


def generate_fastapi_connector(schema_path: Path) -> Path:
    """Mock the creation of a FastAPI connector file."""
    output = Path("backend/integrations/generated") / f"{schema_path.stem}_connector.py"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "from fastapi import APIRouter\n\n"
        "router = APIRouter()\n\n"
        "# TODO: Populate routes from the imported OpenAPI schema.\n",
        encoding="utf-8",
    )
    return output
