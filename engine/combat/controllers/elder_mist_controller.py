import logging
from typing import Self

from engine.combat.controllers.encounter_controller import (
    EncounterController,
    ReasonerExecutionContext,
)
from engine.combat.utility.sos_reasoner import SoSReasoner
from memory import (
    combat_manager_handle,
)

logger = logging.getLogger(__name__)
combat_manager = combat_manager_handle()


class ElderMistEncounterController(EncounterController):
    def __init__(self: Self) -> None:
        """Initialize a new ElderMistController object."""
        super().__init__()
        priority_list = ["ddc4a3bbf0edb9945ba4b06f96f9c20e"] # elder mist sword
        reasoner_execution_context = ReasonerExecutionContext(priority_list)
        self.reasoner = SoSReasoner(reasoner_execution_context)