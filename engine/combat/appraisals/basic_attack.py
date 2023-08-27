from engine.combat.utility.sos_appraisal import SoSAppraisal, SoSAppraisalType


class BasicAttack(SoSAppraisal):
    def __init__(self):
        super().__init__()
        self.type = SoSAppraisalType.Basic

    # executes a basic attack with timing
    def execute(self):
        pass
