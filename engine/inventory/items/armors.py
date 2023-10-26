"""Static namespace to hold armor definitions."""

from engine.inventory.item import EquippableItem, ItemType
from memory.player_party_manager import PlayerPartyCharacter


class ARMORS:
    """Static namespace to hold armor definitions."""

    # Shared equipment (Zale, Valere, Garl, Seraï)
    AdventurersVest = EquippableItem(
        guid="3ac3907f841cc2a40bd0fdce51cd52e2",
        item_type=ItemType.ARMOR,
        name="Adventurer's Vest",
        order_prio=0,
        cost=24,
        sell_value=6,
        phy_def=5,
        mag_def=5,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
        ],
    )
    BoxerShorts = EquippableItem(
        guid="a1d886ffc9682c54ebda876deeed58b4",
        item_type=ItemType.ARMOR,
        name="Boxer Shorts",
        order_prio=0,
        cost=60,
        sell_value=35,
        phy_def=0,
        mag_def=0,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
        ],
    )
    PirateGarb = EquippableItem(
        guid="0626cb583af926649b435bcf63c101a7",
        item_type=ItemType.ARMOR,
        name="Pirate Garb",
        order_prio=15,
        cost=36,
        sell_value=9,
        phy_def=19,
        mag_def=15,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
        ],
    )

    # Armors (Zale, Valere)
    BasicArmor = EquippableItem(
        guid="a31ee5ffc1b693148be7c48150ebff81",
        item_type=ItemType.ARMOR,
        name="Basic Armor",
        order_prio=5,
        cost=28,
        sell_value=7,
        phy_def=13,
        mag_def=9,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    BoneArmor = EquippableItem(
        guid="581aaf64cd0270b4bbf12d9ce9ea4ec0",
        item_type=ItemType.ARMOR,
        name="Bone Armor",
        order_prio=125,
        cost=48,
        sell_value=12,
        phy_def=22,
        mag_def=20,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    DocarriArmor = EquippableItem(
        guid="98223d461dbc41a409926f2a1409f7ec",
        item_type=ItemType.ARMOR,
        name="Docarri Armor",
        order_prio=140,
        cost=92,
        sell_value=23,
        phy_def=28,
        mag_def=22,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    EclipseArmor = EquippableItem(
        guid="911324cc7daad5b41a0af317180a42db",
        item_type=ItemType.ARMOR,
        name="Eclipse Armor",
        order_prio=225,
        cost=152,
        sell_value=38,
        phy_def=53,
        mag_def=49,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    MageKnightArmor = EquippableItem(
        guid="1b92e304b4f82144eb3e123ccb755b2c",
        item_type=ItemType.ARMOR,
        name="Mage-Knight Armor",
        order_prio=20,
        cost=60,
        sell_value=15,
        phy_def=15,
        mag_def=28,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    OakenArmor = EquippableItem(
        guid="ebb0e8958a73d394da97e174d0b5b018",
        item_type=ItemType.ARMOR,
        name="Oaken Armor",
        order_prio=160,
        cost=104,
        sell_value=26,
        phy_def=34,
        mag_def=27,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    RevenantArmor = EquippableItem(
        guid="a0890c10ae319b0409d43f08af673ffd",
        item_type=ItemType.ARMOR,
        name="Revenant Armor",
        order_prio=135,
        cost=48,
        sell_value=12,
        phy_def=23,
        mag_def=25,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    SparkmeshArmor = EquippableItem(
        guid="ccc69fb007cbda342844f25126c90377",
        item_type=ItemType.ARMOR,
        name="Sparkmesh Armor",
        order_prio=200,
        cost=152,
        sell_value=38,
        phy_def=46,
        mag_def=41,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )
    WireplateArmor = EquippableItem(
        guid="67e51219a3a7ea14fa14e9eb4e8643e4",
        item_type=ItemType.ARMOR,
        name="Wireplate Armor",
        order_prio=185,
        cost=152,
        sell_value=38,
        phy_def=43,
        mag_def=36,
        equippable_by=[
            PlayerPartyCharacter.Zale,
            PlayerPartyCharacter.Valere,
        ],
    )

    # Zale
    VolcanicArmor = EquippableItem(
        guid="0c8b9c021791a734892aaafde3b847b6",
        item_type=ItemType.ARMOR,
        name="Volcanic Armor",
        order_prio=175,
        cost=136,
        sell_value=34,
        phy_def=40,
        mag_def=32,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )

    # Valere
    SkyArmor = EquippableItem(
        guid="e1e3c71bb3b7e034684d195c2fa5968c",
        item_type=ItemType.ARMOR,
        name="Sky Armor",
        order_prio=170,
        cost=136,
        sell_value=34,
        phy_def=38,
        mag_def=35,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )

    # Capes (Garl, Seraï, Resh'an)
    AzureCape = EquippableItem(
        guid="722415b4304ba6444b3f86b7b277d5c0",
        item_type=ItemType.ARMOR,
        name="Azure Cape",
        order_prio=180,
        cost=128,
        sell_value=32,
        phy_def=33,
        mag_def=39,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    CosmicCape = EquippableItem(
        guid="d1d1bcd5dbc41d648a812fbc7d1861b2",
        item_type=ItemType.ARMOR,
        name="Cosmic Cape",
        order_prio=215,
        cost=144,
        sell_value=36,
        phy_def=45,
        mag_def=50,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    LeafCape = EquippableItem(
        guid="b441ba29ad2257445a55095e6cb1d537",
        item_type=ItemType.ARMOR,
        name="Leaf Cape",
        order_prio=165,
        cost=96,
        sell_value=24,
        phy_def=28,
        mag_def=33,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    PliantshellVest = EquippableItem(
        guid="7fdba9db0aa4cbd4e8fa3315f94876ab",
        item_type=ItemType.ARMOR,
        name="Pliantshell Vest",
        order_prio=190,
        cost=144,
        sell_value=36,
        phy_def=37,
        mag_def=41,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    SparkmeshCape = EquippableItem(
        guid="fe4a8a4cada2d4a4999403d31f73a50a",
        item_type=ItemType.ARMOR,
        name="Sparkmesh Cape",
        order_prio=205,
        cost=144,
        sell_value=36,
        phy_def=43,
        mag_def=44,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    SpectralCape = EquippableItem(
        guid="d2fd56a9405f9c04fb303795c7840f2f",
        item_type=ItemType.ARMOR,
        name="Spectral Cape",
        order_prio=130,
        cost=44,
        sell_value=11,
        phy_def=19,
        mag_def=23,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )
    TatteredCape = EquippableItem(
        guid="ecf26467374cebc4b812538e7fbe44a4",
        item_type=ItemType.ARMOR,
        name="Tattered Cape",
        order_prio=155,
        cost=92,
        sell_value=23,
        phy_def=26,
        mag_def=33,
        equippable_by=[
            PlayerPartyCharacter.Garl,
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )

    # Cloaks (Seraï, Resh'an)
    ThalassicCloak = EquippableItem(
        guid="0e08751170c68ca4faae2b08ea913275",
        item_type=ItemType.ARMOR,
        name="Thalassic Cloak",
        order_prio=150,
        cost=96,
        sell_value=24,
        phy_def=25,
        mag_def=33,
        equippable_by=[
            PlayerPartyCharacter.Serai,
            PlayerPartyCharacter.Reshan,
        ],
    )

    # Garl
    GarlsApron = EquippableItem(
        guid="86737d6ef697c204187aea8533ec4244",
        item_type=ItemType.ARMOR,
        name="Garl's Apron",
        order_prio=224,
        cost=144,
        sell_value=36,
        phy_def=50,
        mag_def=50,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    MinersSmock = EquippableItem(
        guid="f23fec51c068c00418db6127c54fcc8e",
        item_type=ItemType.ARMOR,
        name="Miner's Smock",
        order_prio=10,
        cost=32,
        sell_value=8,
        phy_def=18,
        mag_def=12,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    PearlescentApron = EquippableItem(
        guid="bd7a12ffa698146418723ed43e6a5eea",
        item_type=ItemType.ARMOR,
        name="Pearlescent Apron",
        order_prio=145,
        cost=88,
        sell_value=22,
        phy_def=25,
        mag_def=25,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )

    # B'st
    CloudySimulacrum = EquippableItem(
        guid="2e09170437a631e46ac9b9669464618c",
        item_type=ItemType.ARMOR,
        name="Cloudy Simulacrum",
        order_prio=210,
        cost=144,
        sell_value=36,
        phy_def=45,
        mag_def=42,
        equippable_by=[
            PlayerPartyCharacter.Bst,
        ],
    )
    DullSimulacrum = EquippableItem(
        guid="e26fa36b128e76041938bf3c86ad8eef",
        item_type=ItemType.ARMOR,
        name="DullSimulacrum",
        order_prio=195,
        cost=144,
        sell_value=36,
        phy_def=37,
        mag_def=37,
        equippable_by=[
            PlayerPartyCharacter.Bst,
        ],
    )
    VitricSimulacrum = EquippableItem(
        guid="ebe89a4a81e46c245bd98a337df06eb8",
        item_type=ItemType.ARMOR,
        name="Vitric Simulacrum",
        order_prio=220,
        cost=144,
        sell_value=36,
        phy_def=53,
        mag_def=51,
        equippable_by=[
            PlayerPartyCharacter.Bst,
        ],
    )
