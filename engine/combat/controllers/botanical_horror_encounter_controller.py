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


class BotanicalHorrorEncounterController(EncounterController):
    """
    Handles the botanical horror fight.

    The general basis of the fight is the flowers must be prioritized first,
    then the boss can be attacked.
    """

    BOTANICAL_HORROR_GUID = "64246a3a9059257409ea628466ced26e"
    TOP_FLOWER_GUID = "621eeda6cacd76740b9b24518c3d211b"
    BOTTOM_FLOWER_GUID = "3bbc6ad42918c444c9947d156e7674aa"

    def __init__(self: Self) -> None:
        """Initialize a new BotanicalHorrorEncounterController object."""
        super().__init__()
        priority_list = [self.TOP_FLOWER_GUID, self.BOTTOM_FLOWER_GUID, self.BOTANICAL_HORROR_GUID]
        reasoner_execution_context = ReasonerExecutionContext(priority_list)
        self.reasoner = SoSReasoner(reasoner_execution_context)
