"""Routing of Mesa Island."""

import logging
from typing import Self

from engine.seq import SeqList
from route.mesa_island.autumn_hills import AutumnHills
from route.mesa_island.mesa_hike import MesaHike

logger = logging.getLogger(__name__)


class MesaIsland(SeqList):
    """Top-level routing of Mesa Island, from coming ashore to Dweller of Strife."""

    def __init__(self: Self) -> None:
        """Initialize a new MesaIsland object."""
        super().__init__(
            name="Mesa Island",
            children=[
                MesaHike(),
                AutumnHills(),
                # TODO(orkaboy): Continue routing
            ],
        )
