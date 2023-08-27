from control import sos_ctrl
from engine.combat.utility.sos_appraisal import SoSAppraisal, SoSAppraisalType
from memory.combat_manager import combat_manager_handle


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
            sos_ctrl().confirm()
        # Just assume we are targeting something
        # TODO: this will be similar to consideration that cycles through targets
        # later until it finds the one where the guid is the same (or the unique id)
        if combat_manager.selected_target_guid != "":
            sos_ctrl().confirm()
            self.complete = True
