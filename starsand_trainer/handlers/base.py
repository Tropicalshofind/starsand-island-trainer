from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from starsand_trainer.core.memory import MemoryClient
from starsand_trainer.models.state import TrainerState
from starsand_trainer.services.offset_registry import OffsetRegistry


class BaseHandler(ABC):
    name: str = "base"

    def __init__(self, memory: MemoryClient, offsets: OffsetRegistry,
                 state: TrainerState, config: dict[str, Any]) -> None:
        self.memory = memory
        self.offsets = offsets
        self.state = state
        self.config = config
        self.enabled = bool(config.get("handlers", {}).get(self.name, True))

    @abstractmethod
    def tick(self) -> None: ...