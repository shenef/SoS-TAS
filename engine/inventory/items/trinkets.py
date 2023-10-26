"""Static namespace to hold trinket definitions."""

from engine.inventory.item import EquippableItem, ItemType


class TRINKETS:
    """Static namespace to hold trinket definitions."""

    # Trinkets
    ArcaneAmulet = EquippableItem(
        guid="d8a7bdab9aa9a6e4e95036b0eff55239",
        item_type=ItemType.TRINKET,
        name="Arcane Amulet",
        cost=200,
        sell_value=50,
    )
    AssassinsPin = EquippableItem(
        guid="88810f8353ed7404bb576582cc39189f",
        item_type=ItemType.TRINKET,
        name="Assassin's Pin",
        cost=328,
        sell_value=82,
    )
    BlueLeaf = EquippableItem(
        guid="588f0765e48c5124a8d9f671b57db116",
        item_type=ItemType.TRINKET,
        name="Blue Leaf",
        cost=220,
        sell_value=55,
    )
    CelestialRay = EquippableItem(
        guid="23cd65231a0ab0c45be5987e87455136",
        item_type=ItemType.TRINKET,
        name="Celestial Ray",
        cost=220,
        sell_value=55,
    )
    DextrousBangle = EquippableItem(
        guid="f93c6f846bc2f0b4484e896221759b94",
        item_type=ItemType.TRINKET,
        name="Dextrous Bangle",
        cost=150,
        sell_value=38,
    )
    EnchantedChainLink = EquippableItem(
        guid="d311de20fa85a5148a7b523f0af76f47",
        item_type=ItemType.TRINKET,
        name="Enchanted Chain Link",
        cost=150,
        sell_value=120,
    )
    EnchantedScarf = EquippableItem(
        guid="9e03ef3b70751944abae3f3880c733b7",
        item_type=ItemType.TRINKET,
        name="Enchanted Scarf",
        cost=190,
        sell_value=45,
    )
    EvergreenLeaf = EquippableItem(
        guid="af3e10fe5b7abd940baadad96a4e5e7c",
        item_type=ItemType.TRINKET,
        name="Evergreen Leaf",
        cost=220,
        sell_value=55,
    )
    GreenLeaf = EquippableItem(
        guid="0ee892db1da195541bcbe578898265b5",
        item_type=ItemType.TRINKET,
        name="Green Leaf",
        cost=28,
        sell_value=7,
    )
    HeliacalEarrings = EquippableItem(
        guid="acadc7386a182444692a4622393aac6b",
        item_type=ItemType.TRINKET,
        name="Heliacal Earrings",
        cost=200,
        sell_value=50,
    )
    LeechingThorn = EquippableItem(
        guid="933db0df85333b341a7d58da22f3b39c",
        item_type=ItemType.TRINKET,
        name="Leeching Thorn",
        cost=44,
        sell_value=11,
    )
    MoonstoneBracer = EquippableItem(
        guid="4441ac030d9882445867b6ee06fbe941",
        item_type=ItemType.TRINKET,
        name="Moonstone Bracer",
        cost=200,
        sell_value=50,
    )
    PowerBelt = EquippableItem(
        guid="154461019876b7741bbd74980276c852",
        item_type=ItemType.TRINKET,
        name="Power Belt",
        cost=24,
        sell_value=6,
    )
    ShimmeringShard = EquippableItem(
        guid="71ff97ab95cbcd84985e62255cbca323",
        item_type=ItemType.TRINKET,
        name="Shimmering Shard",
        cost=195,
        sell_value=45,
    )
    SignetOfClarity = EquippableItem(
        guid="62dcbc88129046140a17fb2790ad258b",
        item_type=ItemType.TRINKET,
        name="Signet Of Clarity",
        cost=190,
        sell_value=45,
    )
    SolsticeSash = EquippableItem(
        guid="076aaeb73b8283748accfb24f68a5c64",
        item_type=ItemType.TRINKET,
        name="Solstice Sash",
        cost=220,
        sell_value=55,
    )


class GROUPTRINKETS:
    """Static namespace to hold group trinket definitions."""

    # Group trinkets
    Abacus = EquippableItem(
        guid="6a39fd9b315b53a4faa9e3736d820eff",
        item_type=ItemType.GROUPTRINKET,
        name="Abacus",
        cost=36,
        sell_value=9,
    )
    AmuletOfOnboarding = EquippableItem(
        guid="b6acbe8e6e78e014d830094e248870af",
        item_type=ItemType.GROUPTRINKET,
        name="Amulet Of Onboarding",
        cost=150,
        sell_value=120,
    )
    Cornucopia = EquippableItem(
        guid="fb067e7ba3b744342bbca13afcfb2a50",
        item_type=ItemType.GROUPTRINKET,
        name="Cornucopia",
        cost=300,
    )
    EyeOfYomara = EquippableItem(
        guid="e7e2fc32454eda44d9d93ba6009d8752",
        item_type=ItemType.GROUPTRINKET,
        name="Eye Of Yomara",
        cost=888,
        sell_value=87,
    )
    GamblersEarring = EquippableItem(
        guid="478d680b15f759d44987b2cef327ce2f",
        item_type=ItemType.GROUPTRINKET,
        name="Gambler's Earring",
        cost=150,
        sell_value=120,
    )
    LucentCrystal = EquippableItem(
        guid="92e2af189aebd9949a662314b01ab847",
        item_type=ItemType.GROUPTRINKET,
        name="Lucent Crystal",
        cost=150,
        sell_value=120,
    )
    MagicPocket = EquippableItem(
        guid="8c32a9ec62778cc4f8cef577c6d80812",
        item_type=ItemType.GROUPTRINKET,
        name="Magic Pocket",
        cost=328,
        sell_value=82,
    )
    NanoInjector = EquippableItem(
        guid="8c4cbe75847cc6249b3bd79cb5a29e8c",
        item_type=ItemType.GROUPTRINKET,
        name="Nano Injector",
        cost=344,
        sell_value=86,
    )
    SpiritOfNinja = EquippableItem(
        guid="1d744837c9ee072498a3e668104325ac",
        item_type=ItemType.GROUPTRINKET,
        name="Spirit of Ninja",
        cost=300,
        sell_value=75,
    )
    ReapersMercy = EquippableItem(
        guid="427eaeae77b247442a8ec3e014542890",
        item_type=ItemType.GROUPTRINKET,
        name="Reaper's Mercy",
        cost=300,
        sell_value=75,
    )
    SolsticeMageRing = EquippableItem(
        guid="c7eb103c76a21974c844159ab0f5a0d2",
        item_type=ItemType.GROUPTRINKET,
        name="Solstice Mage Ring",
        cost=999,
        sell_value=125,
    )
