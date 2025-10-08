"""Notes and semantic search endpoints."""
from __future__ import annotations

from pathlib import Path
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/notes", tags=["notes"])

NOTES_PATH = Path("notes")
NOTES_PATH.mkdir(parents=True, exist_ok=True)


class Note(BaseModel):
    title: str
    tags: list[str]
    path: Path
    summary: str


class NoteCreate(BaseModel):
    title: str
    tags: list[str] = []
    body: str


@router.get("/list", response_model=List[Note])
async def list_notes() -> List[Note]:
    """Enumerate markdown files in the notes vault."""
    notes: list[Note] = []
    for md_file in NOTES_PATH.glob("**/*.md"):
        content = md_file.read_text(encoding="utf-8") if md_file.exists() else ""
        first_line = content.splitlines()[0] if content else ""
        notes.append(
            Note(
                title=md_file.stem.replace("_", " "),
                tags=[],
                path=md_file,
                summary=first_line,
            )
        )
    return notes


@router.post("/create", response_model=Note)
async def create_note(payload: NoteCreate) -> Note:
    """Persist a new note to the vault."""
    file_path = NOTES_PATH / f"{payload.title.replace(' ', '_').lower()}.md"
    file_path.write_text(payload.body, encoding="utf-8")
    return Note(title=payload.title, tags=payload.tags, path=file_path, summary=payload.body.splitlines()[0] if payload.body else "")
