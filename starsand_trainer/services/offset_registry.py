"""Per-build offset table. Update when the game patches."""
from __future__ import annotations

# Offsets are relative to the module base. Values below match the
# public 2026.03 build of Starsand Island (offline client).
_OFFSETS_BY_BUILD: dict[str, dict[str, int]] = {
    "2026.03": {
        "player_stamina": 0x02A1B4C0,
        "player_health": 0x02A1B4C8,
        "player_hunger": 0x02A1B4D0,
        "player_thirst": 0x02A1B4D8,
        "inventory_base": 0x02A1C000,
        "world_time": 0x02A2E010,
    },
    "2026.01": {
        "player_stamina": 0x02A0F2C0,
        "player_health": 0x02A0F2C8,
        "player_hunger": 0x02A0F2D0,
        "player_thirst": 0x02A0F2D8,
        "inventory_base": 0x02A0FE00,
        "world_time": 0x02A21E10,
    },
}


class OffsetRegistry:
    def __init__(self, build: str) -> None:
        if build not in _OFFSETS_BY_BUILD:
            raise KeyError(f"unknown game build {build!r}; "
                           f"known: {sorted(_OFFSETS_BY_BUILD)}")
        self.build = build
        self._table = _OFFSETS_BY_BUILD[build]

    def get(self, key: str) -> int:
        try:
            return self._table[key]
        except KeyError as exc:
            raise KeyError(f"no offset for {key!r} on build {self.build}") from exc

    def keys(self) -> list[str]:
        return sorted(self._table)