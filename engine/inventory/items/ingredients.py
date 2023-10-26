"""Static namespace to hold ingredient definitions."""

from engine.inventory.item import Item, ItemType


class INGREDIENTS:
    """Static namespace to hold ingredient definitions."""

    Apple = Item(
        guid="1050b67b61f94084d970b6ae4c33dc01",
        item_type=ItemType.INGREDIENT,
        name="Apple",
        order_prio=140,
        cost=4,
        sell_value=2,
    )
    Bone = Item(
        guid="9a6abc7114f0eb9409f27b6816830fff",
        item_type=ItemType.INGREDIENT,
        name="Bone",
        order_prio=40,
        cost=6,
        sell_value=3,
    )
    Dairy = Item(
        guid="b8f81159f93c18740ba72fffdd12a13e",
        item_type=ItemType.INGREDIENT,
        name="Dairy",
        order_prio=30,
        cost=4,
        sell_value=2,
    )
    Egg = Item(
        guid="a17b0505c55affc45a066431eb30c655",
        item_type=ItemType.INGREDIENT,
        name="Egg",
        order_prio=20,
        cost=6,
        sell_value=3,
    )
    Fish = Item(
        guid="7f49bbd04a7b4b84092aec1d8f54d1cb",
        item_type=ItemType.INGREDIENT,
        name="Fish",
        order_prio=60,
        cost=2,
        sell_value=1,
    )
    Grains = Item(
        guid="841382ac016092346b0cf860a932c3c7",
        item_type=ItemType.INGREDIENT,
        name="Grains",
        order_prio=35,
        cost=4,
        sell_value=2,
    )
    Lettuce = Item(
        guid="21471472fcbc68149b8cf7a9dac2b785",
        item_type=ItemType.INGREDIENT,
        name="Lettuce",
        order_prio=120,
        cost=2,
        sell_value=1,
    )
    MapleSyrup = Item(
        guid="4b5c4bf16feb4b448bdc3cf8057f2be0",
        item_type=ItemType.INGREDIENT,
        name="Maple Syrup",
        order_prio=0,
        cost=8,
        sell_value=4,
    )
    Meat = Item(
        guid="0b7efbffd76a27f489ea26df56bbc5ad",
        item_type=ItemType.INGREDIENT,
        name="Meat",
        order_prio=50,
        cost=4,
        sell_value=2,
    )
    Mushroom = Item(
        guid="8a5e759b4475ca04d882e7d2b0c9b47a",
        item_type=ItemType.INGREDIENT,
        name="Mushroom",
        order_prio=110,
        cost=2,
        sell_value=1,
    )
    Onion = Item(
        guid="4ffc27dc684ae1e48b5a48909f79c3ca",
        item_type=ItemType.INGREDIENT,
        name="Onion",
        order_prio=80,
        cost=4,
        sell_value=2,
    )
    Peach = Item(
        guid="47336b026e675b34f99d949b4c2f67d0",
        item_type=ItemType.INGREDIENT,
        name="Peach",
        order_prio=150,
        cost=4,
        sell_value=2,
    )
    BellPepper = Item(
        guid="094de5a55e6f5444aaf870aad7e78297",
        item_type=ItemType.INGREDIENT,
        name="Bell Pepper",
        order_prio=85,
        cost=4,
        sell_value=2,
    )
    Potato = Item(
        guid="13dea75b6b52c814b939519cb2b0675c",
        item_type=ItemType.INGREDIENT,
        name="Potato",
        order_prio=90,
        cost=2,
        sell_value=1,
    )
    RedBerry = Item(
        guid="1f83e925faef7584b9f34b0723137d76",
        item_type=ItemType.INGREDIENT,
        name="Red Berry",
        order_prio=160,
        cost=2,
        sell_value=1,
    )
    Seafood = Item(
        guid="76b491199a5df8745a77f2a20ae8bc38",
        item_type=ItemType.INGREDIENT,
        name="Seafood",
        order_prio=70,
        cost=2,
        sell_value=1,
    )
    Tomato = Item(
        guid="f8bf6d10c6c6da840883935fa4aa8c9c",
        item_type=ItemType.INGREDIENT,
        name="Tomato",
        order_prio=130,
        cost=2,
        sell_value=1,
    )
