"""Core trainer engine: owns the process handle and dispatches handlers."""
from __future__ import annotations

import time
from typing import Any

from starsand_trainer.core.memory import MemoryClient
from starsand_trainer.handlers import HANDLERS
from starsand_trainer.models.state import TrainerState
from starsand_trainer.services.offset_registry import OffsetRegistry
from starsand_trainer.utils.logger import get_logger

log = get_logger("engine")

TICK_INTERVAL = 0.25


class TrainerEngine:
    def __init__(self, config: dict[str, Any], dry_run: bool = False,
                 pid: int | None = None) -> None:
        self.config = config
        self.dry_run = dry_run
        self.pid = pid
        self.memory: MemoryClient | None = None
        self.offsets = OffsetRegistry(config.get("game_build", "unknown"))
        self.state = TrainerState()
        self._running = False

    def attach(self) -> None:
        self.memory = MemoryClient(process_name=self.config["process_name"],
                                   pid=self.pid, dry_run=self.dry_run)
        self.memory.open()
        log.info("attached to pid=%s base=0x%X",
                 self.memory.pid, self.memory.base_address)

    def run(self) -> None:
        self._running = True
        handlers = [cls(self.memory, self.offsets, self.state, self.config)
                    for cls in HANDLERS]
        log.info("loaded %d handlers: %s", len(handlers),
                 ", ".join(h.name for h in handlers))

        while self._running:
            for h in handlers:
                if h.enabled:
                    try:
                        h.tick()
                    except Exception as exc:  # noqa: BLE001
                        log.warning("handler %s failed: %s", h.name, exc)
            time.sleep(TICK_INTERVAL)

    def shutdown(self) -> None:
        self._running = False
        if self.memory is not None:
            self.memory.close()
        log.info("engine stopped")