"""Static namespace to hold valuables definitions."""

from engine.inventory.item import Item, ItemType


class VALUABLES:
    """Static namespace to hold valuables definitions."""

    # Ordered in terms of value
    AdamantiteOre = Item(
        "77a0a1cac957b4b4d8cfbb1ee9b2548c", ItemType.VALUABLE, "Adamantite Ore", sell_value=8
    )
    ShinyPearl = Item(
        "7337dc21759feae4a92aba8200c42898", ItemType.VALUABLE, "Shiny Pearl", sell_value=20
    )
    TealAmberOre = Item(
        "33e568f23e2581d448041ac97fb8358d", ItemType.VALUABLE, "Teal Amber Ore", sell_value=35
    )
    ObsidianOre = Item(
        "7a9b2938fabc5434da21134b18b4e0ee", ItemType.VALUABLE, "Obsidian Ore", sell_value=45
    )
    SapphireOre = Item(
        "c43421b626574174e9b5156141213250", ItemType.VALUABLE, "Sapphire Ore", sell_value=55
    )
    ObsidianIngot = Item(
        "4717dc86cf98f2d4794b40e910b63e61", ItemType.VALUABLE, "Obsidian Ingot", sell_value=120
    )
    SapphireIngot = Item(
        "79b159a1b2b69834a96cd56d5e02058c", ItemType.VALUABLE, "Sapphire Ingot", sell_value=140
    )
