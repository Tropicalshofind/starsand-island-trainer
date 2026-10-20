"""Helper: scan the running game for candidate offsets (dev only)."""
import argparse

from starsand_trainer.core.memory import MemoryClient
from starsand_trainer.utils.logger import get_logger

log = get_logger("dump")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--process", default="StarsandIsland.exe")
    ap.add_argument("--start", type=lambda s: int(s, 0), default=0x02A00000)
    ap.add_argument("--length", type=lambda s: int(s, 0), default=0x40000)
    args = ap.parse_args()

    client = MemoryClient(process_name=args.process)
    client.open()
    log.info("dumping 0x%X..0x%X from pid=%d",
             args.start, args.start + args.length, client.pid)
    # Real scanning logic lives in a private branch; this stub just proves
    # the process attaches and the base address resolves.
    log.info("base=0x%X", client.base_address)
    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())