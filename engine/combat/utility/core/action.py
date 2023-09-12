# When calculating an action to pick, the reasoner will select the
# an action and return the consideration and appraisal as an Action
# which will be consumed to execute on an action.
# The consideration will execute to setup for the action, and
# then the appraisal will execute.

from engine.combat.utility.core.appraisal import Appraisal


class Action:
    def __init__(self, consideration, appraisal: Appraisal):
        self.consideration = consideration
        self.appraisal = appraisal

    def execute(self):
        pass
