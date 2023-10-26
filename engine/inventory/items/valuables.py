"""Static namespace to hold valuables definitions."""

from engine.inventory.item import Item, ItemType


class VALUABLES:
    """Static namespace to hold valuables definitions."""

    # Ordered in terms of value
    AdamantiteOre = Item(
        guid="77a0a1cac957b4b4d8cfbb1ee9b2548c",
        item_type=ItemType.VALUABLE,
        name="Adamantite Ore",
        order_prio=0,
        sell_value=8,
    )
    ShinyPearl = Item(
        guid="7337dc21759feae4a92aba8200c42898",
        item_type=ItemType.VALUABLE,
        name="Shiny Pearl",
        order_prio=1000,
        sell_value=20,
    )
    TealAmberOre = Item(
        guid="33e568f23e2581d448041ac97fb8358d",
        item_type=ItemType.VALUABLE,
        name="Teal Amber Ore",
        order_prio=995,
        sell_value=35,
    )
    ObsidianOre = Item(
        guid="7a9b2938fabc5434da21134b18b4e0ee",
        item_type=ItemType.VALUABLE,
        name="Obsidian Ore",
        order_prio=990,
        sell_value=45,
    )
    SapphireOre = Item(
        guid="c43421b626574174e9b5156141213250",
        item_type=ItemType.VALUABLE,
        name="Sapphire Ore",
        order_prio=980,
        sell_value=55,
    )
    ObsidianIngot = Item(
        guid="4717dc86cf98f2d4794b40e910b63e61",
        item_type=ItemType.VALUABLE,
        name="Obsidian Ingot",
        order_prio=985,
        sell_value=120,
    )
    SapphireIngot = Item(
        guid="79b159a1b2b69834a96cd56d5e02058c",
        item_type=ItemType.VALUABLE,
        name="Sapphire Ingot",
        order_prio=975,
        sell_value=140,
    )
