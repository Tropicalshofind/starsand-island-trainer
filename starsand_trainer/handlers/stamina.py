from starsand_trainer.handlers.base import BaseHandler


class StaminaHandler(BaseHandler):
    name = "stamina"

    def tick(self) -> None:
        opts = self.config.get("stamina", {})
        if not opts.get("enabled", True):
            return
        addr = self.memory.resolve(self.offsets.get("player_stamina"))
        current = self.memory.read_int(addr)
        target = int(opts.get("value", 100))
        if current < target:
            self.memory.write_int(addr, target)
            self.state.stats["stamina_writes"] += 1