from engine.combat import SeqCombatAndMove
from engine.seq import (
    InteractMove,
    SeqDelay,
    SeqList,
)


class BattleTest(SeqList):
    def __init__(self):
        super().__init__(
            name="BattleTest",
            children=[
                SeqDelay(name="Wait for select screen", timeout_in_s=3.0),
                BattleTestSequence(),
            ],
        )


class BattleTestSequence(SeqList):
    def __init__(self):
        super().__init__(
            name="Testing Fight",
            children=[
                SeqCombatAndMove(
                    name="Fights",
                    coords=[
                        InteractMove(33.253, 6.002, 20.273),
                    ],
                ),
            ],
        )
