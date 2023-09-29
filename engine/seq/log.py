"""Logging-based nodes."""

# Libraries and Core Files
import logging
from typing import Self

from engine.seq.base import SeqBase

logger = logging.getLogger(__name__)


class SeqLog(SeqBase):
    """Print to the log using the `info` log level."""

    def __init__(self: Self, name: str, text: str) -> None:
        self.text = text
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        """Print text to log."""
        logging.getLogger(self.name).info(self.text)
        return True


class SeqDebug(SeqBase):
    """Print to the log using the `debug` log level."""

    def __init__(self: Self, name: str, text: str) -> None:
        self.text = text
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        """Print text to log."""
        logging.getLogger(self.name).debug(self.text)
        return True
