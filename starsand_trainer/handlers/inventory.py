from starsand_trainer.handlers.base import BaseHandler


class InventoryHandler(BaseHandler):
    name = "inventory"

    def tick(self) -> None:
        opts = self.config.get("inventory", {})
        if not opts.get("unlimited_stacks", False):
            return
        base = self.memory.resolve(self.offsets.get("inventory_base"))
        slots = int(opts.get("slot_count", 24))
        cap = int(opts.get("stack_size", 999))
        for i in range(slots):
            slot_addr = base + i * 0x10
            count = self.memory.read_int(slot_addr + 0x8)
            if 0 < count < cap:
                self.memory.write_int(slot_addr + 0x8, cap)
                self.state.stats["stack_writes"] += 1