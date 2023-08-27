from control import sos_ctrl
from engine.combat.utility.sos_appraisal import SoSAppraisal, SoSAppraisalType
from memory.combat_manager import CombatCharacter, combat_manager_handle


class BasicAttack(SoSAppraisal):
    def __init__(self):
        super().__init__()
        self.type = SoSAppraisalType.Basic
        self.complete = False

    # executes a basic attack with timing
    def execute(self):
        combat_manager = combat_manager_handle()
        if (
            combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index == 0
        ):
            print("selecting attack")
            sos_ctrl().confirm()
        # Just assume we are targeting something
        # TODO: this will be similar to consideration that cycles through targets
        # later until it finds the one where the guid is the same (or the unique id)
        if (
            not combat_manager.battle_command_has_focus
            and combat_manager.battle_command_index is None
            and combat_manager.selected_character != CombatCharacter.NONE
        ):
            print("Following up attack")
            sos_ctrl().confirm()
            print("completing")
            self.complete = True
