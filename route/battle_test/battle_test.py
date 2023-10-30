from typing import Self

from engine.combat import SeqCombatAndMove
from engine.seq import (
    InteractMove,
    SeqBlackboard,
    SeqDelay,
    SeqList,
)


# BattleTest is intended for testing the Utility AI battle system.
# It is not intended to be used to run the TAS.
# This should be run only when the game is in a battle state to start
# the combat controller and then run the battle test sequence.
class BattleTest(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new BattleTest object."""
        super().__init__(
            name="BattleTest",
            children=[
                SeqDelay(name="MANUAL: Focus SoS window!", timeout_in_s=2.5),
                BattleTestSequence(),
            ],
        )


class BattleTestSequence(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new BattleTestSequence object."""
        super().__init__(
            name="Testing Fight",
            children=[
                SeqBlackboard("Dash Strike", key="dash_strike", value=True),
                SeqCombatAndMove(
                    name="Fights",
                    coords=[
                        InteractMove(33.253, 6.002, 20.273),
                    ],
                ),
            ],
        )
