"""Routing of Wraith Island."""

import logging
from typing import Self

from engine.seq import SeqList

logger = logging.getLogger(__name__)


class WraithIsland(SeqList):
    """Top-level routing of Wraith Island, from arrival to returning to Brisk."""

    def __init__(self: Self) -> None:
        """Initialize a new WraithIsland object."""
        super().__init__(
            name="Wraith Island",
            children=[
                # TODO(orkaboy): Continue routing
            ],
        )
