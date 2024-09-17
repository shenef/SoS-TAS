from typing import Self

from engine.seq import (
    SeqDelay,
    SeqList,
)
from route.start import SeqEnableSpeedrunRelics


# RelicSelectTest is intended to test the relic selection screen
# when speedrun mode is activated
# It is not intended to be used to run the TAS.
class RelicSelectTest(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new RelicSelectTest object."""
        super().__init__(
            name="RelicTest",
            children=[
                SeqDelay(name="MANUAL: Focus SoS window!", timeout_in_s=2.5),
                RelicSelectSequence(),
            ],
        )


class RelicSelectSequence(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new BattleTestSequence object."""
        super().__init__(
            name="Testing Relics",
            children=[
                SeqEnableSpeedrunRelics(
                    name="Enable Speedrun Relics",
                ),
            ],
        )
