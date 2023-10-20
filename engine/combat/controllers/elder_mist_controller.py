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


class ElderMistEncounterController(EncounterController):
    """
    Handles the elder mist fight.

    The general basis of the fight is the sword must be prioritized first,
    then the boss can be attacked.
    """

    ELDER_MIST_SWORD_GUID = "ddc4a3bbf0edb9945ba4b06f96f9c20e"

    def __init__(self: Self) -> None:
        """Initialize a new ElderMistController object."""
        super().__init__()
        priority_list = [self.ELDER_MIST_SWORD_GUID]
        reasoner_execution_context = ReasonerExecutionContext(priority_list)
        self.reasoner = SoSReasoner(reasoner_execution_context)
