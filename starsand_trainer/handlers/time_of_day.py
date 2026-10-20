from starsand_trainer.handlers.base import BaseHandler


class TimeOfDayHandler(BaseHandler):
    name = "time_of_day"

    def tick(self) -> None:
        opts = self.config.get("time_of_day", {})
        freeze = opts.get("freeze_at")
        if freeze is None:
            return
        addr = self.memory.resolve(self.offsets.get("world_time"))
        self.memory.write_int(addr, int(freeze))
        self.state.stats["time_writes"] += 1