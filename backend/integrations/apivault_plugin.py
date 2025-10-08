"""Stub integration for apivault.dev catalogue."""
from __future__ import annotations

from typing import List


def fetch_api_catalogue() -> List[dict[str, str]]:
    """Return a static API catalogue placeholder."""
    return [
        {"name": "Example API", "description": "Offline cached API listing.", "category": "developer"}
    ]
