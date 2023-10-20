"""Static namespace to hold armor definitions."""

from engine.inventory.item import Item, ItemType


class ARMORS:
    """Static namespace to hold armor definitions."""

    # Shared equipment (Zale, Valere, Garl, Seraï)
    AdventurersVest = Item(
        "3ac3907f841cc2a40bd0fdce51cd52e2",
        ItemType.ARMOR,
        "Adventurer's Vest",
        cost=24,
        sell_value=6,
    )
    BoxerShorts = Item(
        "a1d886ffc9682c54ebda876deeed58b4", ItemType.ARMOR, "Boxer Shorts", cost=60, sell_value=35
    )
    PirateGarb = Item(
        "0626cb583af926649b435bcf63c101a7", ItemType.ARMOR, "Pirate Garb", cost=36, sell_value=9
    )

    # Armors (Zale, Valere)
    BasicArmor = Item(
        "a31ee5ffc1b693148be7c48150ebff81", ItemType.ARMOR, "Basic Armor", cost=28, sell_value=7
    )
    BoneArmor = Item(
        "581aaf64cd0270b4bbf12d9ce9ea4ec0", ItemType.ARMOR, "Bone Armor", cost=48, sell_value=12
    )
    DocarriArmor = Item(
        "98223d461dbc41a409926f2a1409f7ec", ItemType.ARMOR, "Docarri Armor", cost=92, sell_value=23
    )
    EclipseArmor = Item(
        "911324cc7daad5b41a0af317180a42db", ItemType.ARMOR, "Eclipse Armor", cost=152, sell_value=38
    )
    MageKnightArmor = Item(
        "1b92e304b4f82144eb3e123ccb755b2c",
        ItemType.ARMOR,
        "Mage Knight Armor",
        cost=60,
        sell_value=15,
    )
    OakenArmor = Item(
        "ebb0e8958a73d394da97e174d0b5b018", ItemType.ARMOR, "Oaken Armor", cost=104, sell_value=26
    )
    RevenantArmor = Item(
        "a0890c10ae319b0409d43f08af673ffd", ItemType.ARMOR, "Revenant Armor", cost=48, sell_value=12
    )
    SparkmeshArmor = Item(
        "ccc69fb007cbda342844f25126c90377",
        ItemType.ARMOR,
        "Sparkmesh Armor",
        cost=152,
        sell_value=38,
    )
    WireplateArmor = Item(
        "67e51219a3a7ea14fa14e9eb4e8643e4",
        ItemType.ARMOR,
        "Wireplate Armor",
        cost=152,
        sell_value=38,
    )

    # Zale
    VolcanicArmor = Item(
        "0c8b9c021791a734892aaafde3b847b6",
        ItemType.ARMOR,
        "Volcanic Armor",
        cost=136,
        sell_value=34,
    )

    # Valere
    SkyArmor = Item(
        "e1e3c71bb3b7e034684d195c2fa5968c", ItemType.ARMOR, "Sky Armor", cost=136, sell_value=34
    )

    # Capes (Garl, Seraï, Resh'an)
    AzureCape = Item(
        "722415b4304ba6444b3f86b7b277d5c0", ItemType.ARMOR, "Azure Cape", cost=128, sell_value=32
    )
    CosmicCape = Item(
        "d1d1bcd5dbc41d648a812fbc7d1861b2", ItemType.ARMOR, "Cosmic Cape", cost=144, sell_value=36
    )
    LeafCape = Item(
        "b441ba29ad2257445a55095e6cb1d537", ItemType.ARMOR, "Leaf Cape", cost=96, sell_value=24
    )
    PliantshellVest = Item(
        "7fdba9db0aa4cbd4e8fa3315f94876ab",
        ItemType.ARMOR,
        "Pliantshell Vest",
        cost=144,
        sell_value=36,
    )
    SparkmeshCape = Item(
        "fe4a8a4cada2d4a4999403d31f73a50a",
        ItemType.ARMOR,
        "Sparkmesh Cape",
        cost=144,
        sell_value=36,
    )
    SpectralCape = Item(
        "d2fd56a9405f9c04fb303795c7840f2f", ItemType.ARMOR, "Spectral Cape", cost=44, sell_value=11
    )
    TatteredCape = Item(
        "ecf26467374cebc4b812538e7fbe44a4", ItemType.ARMOR, "Tattered Cape", cost=92, sell_value=23
    )

    # Cloaks (Seraï, Resh'an)
    ThalassicCloak = Item(
        "0e08751170c68ca4faae2b08ea913275",
        ItemType.ARMOR,
        "Thalassic Cloak",
        cost=96,
        sell_value=24,
    )

    # Garl
    GarlsApron = Item(
        "86737d6ef697c204187aea8533ec4244", ItemType.ARMOR, "Garl's Apron", cost=144, sell_value=36
    )
    MinersSmock = Item(
        "f23fec51c068c00418db6127c54fcc8e", ItemType.ARMOR, "Miner's Smock", cost=32, sell_value=8
    )
    PearlescentApron = Item(
        "bd7a12ffa698146418723ed43e6a5eea",
        ItemType.ARMOR,
        "Pearlescent Apron",
        cost=88,
        sell_value=22,
    )

    # B'st
    CloudySimulacrum = Item(
        "2e09170437a631e46ac9b9669464618c",
        ItemType.ARMOR,
        "Cloudy Simulacrum",
        cost=144,
        sell_value=36,
    )
    DullSimulacrum = Item(
        "e26fa36b128e76041938bf3c86ad8eef",
        ItemType.ARMOR,
        "DullSimulacrum",
        cost=144,
        sell_value=36,
    )
    VitricSimulacrum = Item(
        "ebe89a4a81e46c245bd98a337df06eb8",
        ItemType.ARMOR,
        "Vitric Simulacrum",
        cost=144,
        sell_value=36,
    )
