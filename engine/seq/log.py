"""Logging-based nodes."""

# Libraries and Core Files
import logging
from typing import Self

from control import sos_ctrl
from engine.seq.base import SeqBase
from GUI.tools.commentary import CommentaryAuthor, CommentaryEntry, get_commentary_log

logger = logging.getLogger(__name__)


class SeqLog(SeqBase):
    """Print to the log using the `info` log level."""

    def __init__(self: Self, name: str, text: str) -> None:
        """Initialize a SeqLog node."""
        self.text = text
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        """Print text to log."""
        logging.getLogger(self.name).info(self.text)
        return True


class SeqDebug(SeqBase):
    """Print to the log using the `debug` log level."""

    def __init__(self: Self, name: str, text: str) -> None:
        """Initialize a SeqDebug node."""
        self.text = text
        super().__init__(name)

    def execute(self: Self, delta: float) -> bool:
        """Print text to log."""
        logging.getLogger(self.name).debug(self.text)
        return True


class SeqTextCrawl(SeqBase):
    """
    Print text over time in the TAS GUI, optionally skipping cutscenes.

    This can be used to show a bunch of text to a viewer.
    """

    def __init__(
        self: Self, name: str, text_nodes: list[tuple[str, float]], skip_cutscene: bool = True
    ) -> None:
        """Initialize a SeqTextCrawl node."""
        super().__init__(name)
        self.skip_cutscene = skip_cutscene
        self.step = 0
        self.timer = 0.0
        self.text_nodes = text_nodes

    def execute(self: Self, delta: float) -> bool:
        ctrl = sos_ctrl()
        if self.step >= len(self.text_nodes):
            ctrl.toggle_turbo(state=False)
            ctrl.toggle_confirm(state=False)
            ctrl.toggle_cancel(state=False)
            return True
        # Get the current text node
        _, cur_timeout = self.text_nodes[self.step]

        if self.skip_cutscene:
            ctrl.toggle_turbo(state=True)
            ctrl.toggle_confirm(state=True)
            ctrl.toggle_cancel(state=True)

        # Increase the timer and go to next step
        self.timer += delta
        if self.timer >= cur_timeout:
            self.timer = 0.0
            self.step = self.step + 1
        return False

    def __repr__(self: Self) -> str:
        if self.step >= len(self.text_nodes):
            return ""
        cur_text, _ = self.text_nodes[self.step]
        return f"\n{cur_text}\n"


class SeqCommentary(SeqBase):
    """Prints text entries to a side window that looks like a chat."""

    def __init__(
        self: Self, author: CommentaryAuthor, text: str, delay: float = 0.0, lifetime: float = 60.0
    ) -> None:
        """Initialize a SeqCommentary node."""
        super().__init__()
        self.entry = CommentaryEntry(
            author=author,
            text=text,
            delay=delay,
            lifetime=lifetime,
        )

    def execute(self: Self, delta: float) -> bool:
        log = get_commentary_log()
        # Push data to commentary buffer
        log.append(self.entry)
        return True
