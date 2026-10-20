"""Thin wrapper around pymem with dry-run support and safe reads."""
from __future__ import annotations

import struct
from typing import Optional

from pymem import Pymem
from pymem.exception import ProcessNotFound

from starsand_trainer.utils.logger import get_logger

log = get_logger("memory")


class MemoryClient:
    def __init__(self, process_name: str, pid: Optional[int] = None,
                 dry_run: bool = False) -> None:
        self.process_name = process_name
        self.requested_pid = pid
        self.dry_run = dry_run
        self.pm: Optional[Pymem] = None
        self.pid: int = -1
        self.base_address: int = 0

    def open(self) -> None:
        if self.dry_run:
            self.pid = self.requested_pid or 0
            self.base_address = 0x140000000
            log.info("[dry-run] pretending to attach to %s", self.process_name)
            return
        try:
            if self.requested_pid:
                self.pm = Pymem(process_id=self.requested_pid)
            else:
                self.pm = Pymem(process_name=self.process_name)
        except ProcessNotFound as exc:
            raise RuntimeError(
                f"process {self.process_name!r} not found — is the game running?"
            ) from exc
        self.pid = self.pm.process_id
        self.base_address = self.pm.base_address

    def read_int(self, address: int) -> int:
        if self.dry_run or self.pm is None:
            return 0
        return struct.unpack("<i", self.pm.read_bytes(address, 4))[0]

    def write_int(self, address: int, value: int) -> None:
        if self.dry_run or self.pm is None:
            log.debug("[dry-run] write_int(0x%X, %d)", address, value)
            return
        self.pm.write_int(address, value)

    def resolve(self, module_offset: int) -> int:
        return self.base_address + module_offset

    def close(self) -> None:
        if self.pm is not None:
            try:
                self.pm.close_process()
            except Exception:  # noqa: BLE001
                pass
            self.pm = None