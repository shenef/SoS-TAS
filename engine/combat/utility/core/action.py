from typing import Any, Self

from engine.combat.utility.core.appraisal import Appraisal


class Action:
    """
    Prepare considerations and appraisals for consumption by a reasoner.

    Actions are containers for considerations and appraisals that a reasoner
    can consume to execute an appraisal on the desired consideration.
    """

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
