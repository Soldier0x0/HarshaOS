"""Database initialisation utilities for HarshaOS."""
from __future__ import annotations

import sqlite3
from pathlib import Path

import duckdb

BASE_PATH = Path(__file__).resolve().parents[2]
CACHE_PATH = BASE_PATH / "cache"
SQLITE_PATH = CACHE_PATH / "harshaos.db"
DUCKDB_PATH = CACHE_PATH / "analytics.duckdb"

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS mail_digest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    sender TEXT NOT NULL,
    summary TEXT NOT NULL,
    received_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    occurred_on TEXT NOT NULL,
    merchant TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    is_subscription INTEGER DEFAULT 0
);
"""


def init_sqlite() -> None:
    CACHE_PATH.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(SQLITE_PATH) as conn:
        conn.executescript(SCHEMA_SQL)
        conn.commit()


def init_duckdb() -> None:
    CACHE_PATH.mkdir(parents=True, exist_ok=True)
    with duckdb.connect(str(DUCKDB_PATH)) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS metrics (name VARCHAR PRIMARY KEY, value DOUBLE, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
        )


if __name__ == "__main__":
    init_sqlite()
    init_duckdb()
    print(f"Initialised SQLite at {SQLITE_PATH}")
    print(f"Initialised DuckDB at {DUCKDB_PATH}")
