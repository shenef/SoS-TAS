"""Routing of Sleeper Island."""

import logging
from typing import Self

from engine.seq import SeqCheckpoint, SeqList
from route.sleeper_island.brisk import Brisk, BriskToWizardLab
from route.sleeper_island.coral_cascades import CoralCascades, CoralCascadesToBrisk
from route.sleeper_island.moorlands import Moorlands
from route.sleeper_island.stonemasons import StonemasonsOutpost
from route.sleeper_island.wizard_lab import WizardLab
from route.sleeper_island.xtols_landing import XtolsLanding

logger = logging.getLogger(__name__)


class SleeperIsland(SeqList):
    """Top-level routing of Sleeper Island, from arrival at X'tol to leaving for Wraith Island."""

    def __init__(self: Self) -> None:
        super().__init__(
            name="Sleeper Island",
            children=[
                XtolsLanding(),
                SeqCheckpoint("moorlands"),
                Moorlands(),
                StonemasonsOutpost(),
                CoralCascades(),
                CoralCascadesToBrisk(),
                Brisk(),
                BriskToWizardLab(),
                WizardLab(),
                # TODO(orkaboy): Routing
            ],
        )
