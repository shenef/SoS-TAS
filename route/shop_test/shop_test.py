from typing import Self

from engine.inventory.items import ARMORS, VALUABLES, WEAPONS
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
                # SeqToggleRelic(
                #     "Relic test 1",
                #     relics=[
                #         RELICS.AmuletOfStorytelling,
                #         RELICS.ArtfulGambit,
                #         RELICS.DubiousDare,
                #         RELICS.AdamantShard,
                #         RELICS.AmuletOfStorytelling,
                #         RELICS.BearingReel,
                #         RELICS.GoldTooth,
                #         RELICS.ExtraPockets,
                #         RELICS.AmuletOfStorytelling,
                #     ],
                # ),
                SeqShop(
                    name="Equipment Shop",
                    commands=[
                        ShoppingCommand(item=VALUABLES.ShinyPearl, sell=True),
                        ShoppingCommand(item=VALUABLES.TealAmberOre, amount=5, sell=True),
                        ShoppingCommand(item=VALUABLES.ObsidianOre, sell=True),
                        ShoppingCommand(item=VALUABLES.ObsidianIngot, sell=True),
                        ShoppingCommand(item=WEAPONS.ShimmeringDaggers, sell=True),
                        ShoppingCommand(item=WEAPONS.SeraiWeapon, sell=True),
                        ShoppingCommand(item=WEAPONS.CauldronLid, sell=True),
                        ShoppingCommand(item=WEAPONS.TrainingStaff, sell=True),
                        ShoppingCommand(item=ARMORS.AdventurersVest, sell=True),
                        ShoppingCommand(
                            item=ARMORS.PearlescentApron, character=PlayerPartyCharacter.Garl
                        ),
                        ShoppingCommand(
                            item=ARMORS.DocarriArmor, character=PlayerPartyCharacter.Zale
                        ),
                        ShoppingCommand(
                            item=ARMORS.DocarriArmor, character=PlayerPartyCharacter.Valere
                        ),
                        ShoppingCommand(
                            item=WEAPONS.CoralStaff,
                            character=PlayerPartyCharacter.Valere,
                        ),
                        ShoppingCommand(
                            item=WEAPONS.CoralSword,
                            character=PlayerPartyCharacter.Zale,
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
