"""Routing of the restored Brisk during the Cataclysm."""

import logging
from typing import Self

from engine.seq import (
    SeqList,
)

logger = logging.getLogger(__name__)


class BriskRestored(SeqList):
    """Routing of the restored Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new BriskRestored object."""
        super().__init__(
            name="Brisk restored",
            children=[
                # TODO(orkaboy): Continue routing
            ],
        )


class Mirth(SeqList):
    """Routing of the restored Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new BriskRestored object."""
        super().__init__(
            name="Brisk restored",
            children=[
                # TODO(orkaboy): Continue routing
            ],
        )
