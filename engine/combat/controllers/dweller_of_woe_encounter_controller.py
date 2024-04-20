import logging
from typing import Self

from engine.combat.contexts.reasoner_execution_context import ReasonerExecutionContext
from engine.combat.controllers.encounter_controller import EncounterController
from engine.combat.utility.sos_reasoner import SoSReasoner
from memory import (
    combat_manager_handle,
)

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class DwellerOfWoeEncounterController(EncounterController):
    """
    Handles the elder mist fight.

    The general basis of the fight is the sword must be prioritized first,
    then the boss can be attacked.
    """

    DWELLER_OF_WOE = "807fd9a36ea523f4aa7d532ddc565a69"
    DWELLER_OF_WOE_CLONE = "e1685476dd793e44c9c8909fe0b3622f"
    TRUE_DWELLER_OF_WOE = "bcde1eb0ea076f846a0ee20287d88204"

    def __init__(self: Self) -> None:
        """Initialize a new DwellerOfWoeEncounterController object."""
        super().__init__()
        priority_list = [self.TRUE_DWELLER_OF_WOE, self.DWELLER_OF_WOE, self.DWELLER_OF_WOE_CLONE]
        reasoner_execution_context = ReasonerExecutionContext(priority_list)
        self.reasoner = SoSReasoner(reasoner_execution_context)
