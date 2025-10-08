"""Simple plugin loader stub for optional integrations."""
from __future__ import annotations

import importlib
import logging
from pathlib import Path
from types import ModuleType
from typing import Iterable

import yaml

logger = logging.getLogger("harshaos.integrations")

CONFIG_FILE = Path("backend/configs/integrations.yaml")


def load_enabled_plugins() -> Iterable[ModuleType]:
    if not CONFIG_FILE.exists():
        logger.info("No integrations configuration found at %s", CONFIG_FILE)
        return []

    config = yaml.safe_load(CONFIG_FILE.read_text(encoding="utf-8")) or {}
    enabled = config.get("enabled", [])
    plugins = []
    for dotted_path in enabled:
        try:
            module = importlib.import_module(dotted_path)
            plugins.append(module)
            logger.info("Loaded integration plugin: %s", dotted_path)
        except ImportError as exc:
            logger.warning("Failed to load plugin %s: %s", dotted_path, exc)
    return plugins
