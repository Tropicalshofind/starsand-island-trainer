from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from starsand_trainer.utils.logger import get_logger

log = get_logger("config")

_DEFAULTS: dict[str, Any] = {
    "process_name": "StarsandIsland.exe",
    "game_build": "2026.03",
    "handlers": {},
}


def load_config(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    cfg: dict[str, Any] = dict(_DEFAULTS)
    if p.exists():
        with p.open("r", encoding="utf-8") as fh:
            loaded = yaml.safe_load(fh) or {}
        cfg.update(loaded)
        log.info("loaded config from %s", p)
    else:
        log.warning("config %s missing, using defaults", p)
    return cfg