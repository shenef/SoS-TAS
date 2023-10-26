from typing import Self

from engine.inventory import ARMORS
from engine.seq import (
    SeqDelay,
    SeqList,
    SeqShop,
    ShoppingCommand,
)
from memory.player_party_manager import PlayerPartyCharacter


# BattleTest is intended for testing the Utility AI battle system.
# It is not intended to be used to run the TAS.
# This should be run only when the game is in a battle state to start
# the combat controller and then run the battle test sequence.
class ShopTest(SeqList):
    def __init__(self: Self) -> None:
        """Initialize a new ShopTest object."""
        super().__init__(
            name="ShopTest",
            children=[
                SeqDelay(name="MANUAL: Focus SoS window!", timeout_in_s=2.5),
                SeqShop(
                    name="Equipment Shop",
                    commands=[
                        ShoppingCommand(item=ARMORS.AdventurersVest, sell=True),
                        ShoppingCommand(item=ARMORS.BasicArmor, sell=True),
                        ShoppingCommand(item=ARMORS.CosmicCape, sell=False),
                        ShoppingCommand(
                            item=ARMORS.DocarriArmor,
                            sell=False,
                            character=PlayerPartyCharacter.Zale,
                        ),
                        ShoppingCommand(item=ARMORS.EclipseArmor, sell=True),
                        ShoppingCommand(
                            item=ARMORS.GarlsApron, sell=False, character=PlayerPartyCharacter.Garl
                        ),
                    ],
                ),
                # SeqShop(
                #    name="Item Shop",
                #    commands=[
                #        ShoppingCommand(item=VALUABLES.AdamantiteOre, sell=True),
                #        ShoppingCommand(item=VALUABLES.ObsidianIngot, amount=5),
                #        ShoppingCommand(item=VALUABLES.SapphireIngot, amount=9),
                #        ShoppingCommand(item=VALUABLES.ShinyPearl, amount=3),
                #    ],
                # ),
            ],
        )
