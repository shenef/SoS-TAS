# When calculating an action to pick, the reasoner will select the
# an action and return the consideration and appraisal as an Action
# which will be consumed to execute on an action.
# The consideration will execute to setup for the action, and
# then the appraisal will execute.

from typing import Any, Self

from engine.combat.utility.core.appraisal import Appraisal


class Action:
    # TODO(eein): Fix Any due to circular dependency
    def __init__(
        self: Self,
        consideration: Any,  # noqa: ANN401
        appraisal: Appraisal,
    ) -> None:
        self.consideration = consideration
        self.appraisal = appraisal

    def execute(self: Self) -> None:
        pass
