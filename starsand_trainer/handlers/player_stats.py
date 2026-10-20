from starsand_trainer.handlers.base import BaseHandler


class PlayerStatsHandler(BaseHandler):
    name = "player_stats"

    def tick(self) -> None:
        opts = self.config.get("player_stats", {})
        for key in ("health", "hunger", "thirst"):
            value = opts.get(key)
            if value is None:
                continue
            addr = self.memory.resolve(self.offsets.get(f"player_{key}"))
            self.memory.write_int(addr, int(value))
            self.state.stats[f"{key}_writes"] += 1