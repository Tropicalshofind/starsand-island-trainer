from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainerState:
    attached: bool = False
    stats: dict[str, int] = field(default_factory=lambda: {
        "stamina_writes": 0,
        "stack_writes": 0,
        "time_writes": 0,
        "health_writes": 0,
        "hunger_writes": 0,
        "thirst_writes": 0,
    })

    def summary(self) -> str:
        return ", ".join(f"{k}={v}" for k, v in sorted(self.stats.items()) if v)