"""Application bootstrap: parse args, load config, start the engine."""
from __future__ import annotations

import argparse
import sys

from colorama import Fore, Style, init as colorama_init

from starsand_trainer.core.engine import TrainerEngine
from starsand_trainer.services.config_loader import load_config
from starsand_trainer.utils.logger import get_logger

log = get_logger("bootstrap")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="starsand-trainer")
    parser.add_argument("--config", default="config/default.yaml")
    parser.add_argument("--dry-run", action="store_true",
                        help="log writes instead of applying them")
    parser.add_argument("--pid", type=int, default=None,
                        help="attach to a specific PID instead of auto-detect")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    colorama_init()
    args = _parse_args(argv if argv is not None else sys.argv[1:])
    log.info("%sStarsand Island Trainer%s starting (dry_run=%s)",
             Fore.CYAN, Style.RESET_ALL, args.dry_run)

    cfg = load_config(args.config)
    engine = TrainerEngine(config=cfg, dry_run=args.dry_run, pid=args.pid)

    try:
        engine.attach()
        engine.run()
    except KeyboardInterrupt:
        log.info("interrupted by user, shutting down")
    finally:
        engine.shutdown()
    return 0