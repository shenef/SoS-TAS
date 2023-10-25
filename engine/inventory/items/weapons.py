"""Static namespace to hold weapon definitions."""

from engine.inventory.item import EquippableItem, ItemType
from memory.player_party_manager import PlayerPartyCharacter


class WEAPONS:
    """Static namespace to hold weapon definitions."""

    # Zale
    BambooSlicer = EquippableItem(
        guid="0a9e0ac0bb822b349af356af38ad6a5d",
        item_type=ItemType.WEAPON,
        name="Bamboo Slicer",
        cost=140,
        sell_value=35,
        phy_atk=22,
        mag_atk=19,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    CloudSword = EquippableItem(
        guid="5877570357bf9f441ae01cd06bccd9f4",
        item_type=ItemType.WEAPON,
        name="Cloud Sword",
        cost=156,
        sell_value=39,
        phy_atk=29,
        mag_atk=24,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    CoralSword = EquippableItem(
        guid="16d199bda90813f40a28fd9203865374",
        item_type=ItemType.WEAPON,
        name="Coral Sword",
        cost=112,
        sell_value=28,
        phy_atk=19,
        mag_atk=15,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    FirmamentEdge = EquippableItem(
        guid="7d6c888ffacc1cd4ab3ce414b294c67e",
        item_type=ItemType.WEAPON,
        name="Firmament Edge",
        cost=168,
        sell_value=42,
        phy_atk=42,
        mag_atk=32,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    KybersteelBlade = EquippableItem(
        guid="0dddb9e8063bbdd4fb724929ee784f38",
        item_type=ItemType.WEAPON,
        name="Kybersteel Blade",
        cost=168,
        sell_value=42,
        phy_atk=35,
        mag_atk=29,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    PlasmaBlade = EquippableItem(
        guid="301554cfa6770af4d9e0791f01488999",
        item_type=ItemType.WEAPON,
        name="Plasma Blade",
        cost=168,
        sell_value=42,
        phy_atk=40,
        mag_atk=29,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    ScrimshawedBlade = EquippableItem(
        guid="7ce9f696d3089434fbff10c7653d0026",
        item_type=ItemType.WEAPON,
        name="Scrimshawed Blade",
        cost=80,
        sell_value=20,
        phy_atk=13,
        mag_atk=10,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    ShimmeringBlade = EquippableItem(
        guid="10e93ab756357f142b3c6ef3ec7a7c4b",
        item_type=ItemType.WEAPON,
        name="Shimmering Blade",
        cost=80,
        sell_value=20,
        phy_atk=15,
        mag_atk=10,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    SilverBlade = EquippableItem(
        guid="71cfc6d93b292d3499c472b73e9daae1",
        item_type=ItemType.WEAPON,
        name="Silver Blade",
        cost=52,
        sell_value=13,
        phy_atk=9,
        mag_atk=7,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    SolenSword = EquippableItem(
        guid="8f96ab39454c54641812c57f7b332481",
        item_type=ItemType.WEAPON,
        name="Solen Sword",
        cost=168,
        sell_value=42,
        phy_atk=50,
        mag_atk=35,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    SquireSword = EquippableItem(
        guid="4a1710ba97ae350428f18704e36fe234",
        item_type=ItemType.WEAPON,
        name="Squire Sword",
        cost=32,
        sell_value=8,
        phy_atk=5,
        mag_atk=5,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )
    TrainingSword = EquippableItem(
        guid="e3098c0169021924a97713b57a009928",
        item_type=ItemType.WEAPON,
        name="Training Sword",
        cost=10,
        sell_value=5,
        phy_atk=1,
        mag_atk=3,
        equippable_by=[
            PlayerPartyCharacter.Zale,
        ],
    )

    # Valere
    AdamantineStaff = EquippableItem(
        guid="5d108fe330c777241bb2b7c5326acc54",
        item_type=ItemType.WEAPON,
        name="Adamantine Staff",
        cost=168,
        sell_value=42,
        phy_atk=39,
        mag_atk=23,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    CopperStaff = EquippableItem(
        guid="10d0cb7c4836f794bb6f4d965f2b76c8",
        item_type=ItemType.WEAPON,
        name="Copper Staff",
        cost=36,
        sell_value=9,
        phy_atk=7,
        mag_atk=4,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    CoralStaff = EquippableItem(
        guid="70a7707a760f40046b71b4b2e111a708",
        item_type=ItemType.WEAPON,
        name="Coral Staff",
        cost=112,
        sell_value=28,
        phy_atk=22,
        mag_atk=10,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    EarthshineStaff = EquippableItem(
        guid="27a72590849651b4ba1cf80fe6be8d4a",
        item_type=ItemType.WEAPON,
        name="Earthshine Staff",
        cost=168,
        sell_value=42,
        phy_atk=47,
        mag_atk=25,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    IgneousStaff = EquippableItem(
        guid="e93c519d3c18fa245937cc461e4de24d",
        item_type=ItemType.WEAPON,
        name="Igneous Staff",
        cost=156,
        sell_value=39,
        phy_atk=32,
        mag_atk=20,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    MoonBo = EquippableItem(
        guid="95ac264461a94a0458a14a39954e3afc",
        item_type=ItemType.WEAPON,
        name="Moon Bo",
        cost=168,
        sell_value=42,
        phy_atk=58,
        mag_atk=28,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    NeobsidianStaff = EquippableItem(
        guid="d25d22b957a9c5c478e188e1f03f7107",
        item_type=ItemType.WEAPON,
        name="Neobsidian Staff",
        cost=168,
        sell_value=42,
        phy_atk=44,
        mag_atk=23,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    OrnateBo = EquippableItem(
        guid="c82873a6208c95241834faa4a0c90321",
        item_type=ItemType.WEAPON,
        name="Ornate Bo",
        cost=140,
        sell_value=35,
        phy_atk=25,
        mag_atk=14,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    OsseousStaff = EquippableItem(
        guid="3e2210133b9ad0940bddde38c647e3e7",
        item_type=ItemType.WEAPON,
        name="Osseous Staff",
        cost=76,
        sell_value=19,
        phy_atk=15,
        mag_atk=8,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    ShimmeringStaff = EquippableItem(
        guid="f7d49514f7bfca34b942d95722b76a32",
        item_type=ItemType.WEAPON,
        name="Shimmering Staff",
        cost=76,
        sell_value=19,
        phy_atk=16,
        mag_atk=8,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    TealAmberStaff = EquippableItem(
        guid="e27094f36cb7bb140b614b89fde60550",
        item_type=ItemType.WEAPON,
        name="Teal Amber Staff",
        cost=48,
        sell_value=12,
        phy_atk=11,
        mag_atk=6,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )
    TrainingStaff = EquippableItem(
        guid="40b7062ac812c5d47bb1ff0df4987e8e",
        item_type=ItemType.WEAPON,
        name="Training Staff",
        cost=10,
        sell_value=5,
        phy_atk=3,
        mag_atk=1,
        equippable_by=[
            PlayerPartyCharacter.Valere,
        ],
    )

    # Garl
    CalciteLid = EquippableItem(
        guid="108a40870288c934d94c1661286ff1f0",
        item_type=ItemType.WEAPON,
        name="Calcite Lid",
        cost=56,
        sell_value=14,
        phy_atk=15,
        mag_atk=13,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    CauldronLid = EquippableItem(
        guid="b9995b298ada14e4887faf134942b564",
        item_type=ItemType.WEAPON,
        name="Cauldron Lid",
        cost=10,
        sell_value=7,
        phy_atk=6,
        mag_atk=7,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    MooncradleBoyLid = EquippableItem(
        guid="0f0053be4fa1bf84db338a626d751eb2",
        item_type=ItemType.WEAPON,
        name="Mooncradle Boy Lid",
        cost=136,
        sell_value=34,
        phy_atk=50,
        mag_atk=35,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    ObsidianLid = EquippableItem(
        guid="c16988af55e565545b978150228fc5e7",
        item_type=ItemType.WEAPON,
        name="Obsidian Lid",
        cost=56,
        sell_value=14,
        phy_atk=10,
        mag_atk=8,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    PhosphoriteLid = EquippableItem(
        guid="8df0767e67aa4e34584a5066469765de",
        item_type=ItemType.WEAPON,
        name="Phosphorite Lid",
        cost=112,
        sell_value=28,
        phy_atk=21,
        mag_atk=15,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    RockLid = EquippableItem(
        guid="7694b5b801204a74c888d67a49f06d42",
        item_type=ItemType.WEAPON,
        name="Rock Lid",
        cost=44,
        sell_value=11,
        phy_atk=10,
        mag_atk=9,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )
    SturdyCog = EquippableItem(
        guid="68d99c8b95dbf7c41a00d562b41b289a",
        item_type=ItemType.WEAPON,
        name="Sturdy Cog",
        cost=136,
        sell_value=34,
        phy_atk=27,
        mag_atk=19,
        equippable_by=[
            PlayerPartyCharacter.Garl,
        ],
    )

    # Seraï
    ApogeeDaggers = EquippableItem(
        guid="a164640364ccf3546b0b9a0ac82b59cf",
        item_type=ItemType.WEAPON,
        name="Apogee Daggers",
        cost=184,
        sell_value=46,
        phy_atk=41,
        mag_atk=35,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    CoralDaggers = EquippableItem(
        guid="d78f39987eaedcc42b938fc1763bba59",
        item_type=ItemType.WEAPON,
        name="Coral Daggers",
        cost=124,
        sell_value=31,
        phy_atk=14,
        mag_atk=20,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    KybersteelDaggers = EquippableItem(
        guid="e24926f361bf385478653d34ac9f6a41",
        item_type=ItemType.WEAPON,
        name="Kybersteel Daggers",
        cost=184,
        sell_value=46,
        phy_atk=32,
        mag_atk=32,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    PhantomDaggers = EquippableItem(
        guid="3f851aff158a63042bd188b378bc3d81",
        item_type=ItemType.WEAPON,
        name="Phantom Daggers",
        cost=130,
        sell_value=30,
        phy_atk=20,
        mag_atk=20,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    PlasmaDaggers = EquippableItem(
        guid="1ca6171b638ffdb49bda2f4cfcb2e564",
        item_type=ItemType.WEAPON,
        name="Plasma Daggers",
        cost=184,
        sell_value=46,
        phy_atk=36,
        mag_atk=32,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    SeraiWeapon = EquippableItem(
        guid="6dfc4e7a1624a9c4eaaf2ae75c336b5c",
        item_type=ItemType.WEAPON,
        name="Serai Weapon",
        cost=10,
        sell_value=10,
        phy_atk=5,
        mag_atk=8,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    ShimmeringDaggers = EquippableItem(
        guid="b883d3f8ffbc78040ade7dc4675ac1c6",
        item_type=ItemType.WEAPON,
        name="Shimmering Daggers",
        cost=10,
        sell_value=10,
        phy_atk=9,
        mag_atk=14,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    ShroomyDaggers = EquippableItem(
        guid="aa8b7c8001ca94d4eaa65d1ffb58a5e2",
        item_type=ItemType.WEAPON,
        name="Shroomy Daggers",
        cost=144,
        sell_value=36,
        phy_atk=20,
        mag_atk=24,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    StarShards = EquippableItem(
        guid="a27614e2379ef9e4dac1950a51b3f71d",
        item_type=ItemType.WEAPON,
        name="Star Shards",
        cost=184,
        sell_value=46,
        phy_atk=49,
        mag_atk=38,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )
    TruesilverDaggers = EquippableItem(
        guid="0d86cee64cf8be44985fcee7a34c49f2",
        item_type=ItemType.WEAPON,
        name="Truesilver Daggers",
        cost=168,
        sell_value=42,
        phy_atk=27,
        mag_atk=29,
        equippable_by=[
            PlayerPartyCharacter.Serai,
        ],
    )

    # Resh'an
    AetherwoodCork = EquippableItem(
        guid="807d9f5c8b8f5514abcf261a36dc1711",
        item_type=ItemType.WEAPON,
        name="Aetherwood Cork",
        cost=172,
        sell_value=43,
        phy_atk=44,
        mag_atk=49,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    CypressCork = EquippableItem(
        guid="1a8eae5901ae6754a8899a58a692a2b3",
        item_type=ItemType.WEAPON,
        name="Cypress Cork",
        cost=164,
        sell_value=41,
        phy_atk=26,
        mag_atk=32,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    MapleCork = EquippableItem(
        guid="8f50c130484e7c44a8d90860eaaa2806",
        item_type=ItemType.WEAPON,
        name="Maple Cork",
        cost=136,
        sell_value=34,
        phy_atk=20,
        mag_atk=22,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    RosewoodCork = EquippableItem(
        guid="c2d85fc1508398e4a8c4db3e12594978",
        item_type=ItemType.WEAPON,
        name="Rosewood Cork",
        cost=172,
        sell_value=43,
        phy_atk=34,
        mag_atk=39,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    SalixCork = EquippableItem(
        guid="2a8606f2bf7f5224cadb8ae2c1d1b531",
        item_type=ItemType.WEAPON,
        name="Salix Cork",
        cost=172,
        sell_value=43,
        phy_atk=37,
        mag_atk=41,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    WalnutCork = EquippableItem(
        guid="c3b22a46f99faba498bfbc7519cce88c",
        item_type=ItemType.WEAPON,
        name="Walnut Cork",
        cost=172,
        sell_value=43,
        phy_atk=29,
        mag_atk=39,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
    WitheredCork = EquippableItem(
        guid="441bec8771714944eb32ff53c082f8da",
        item_type=ItemType.WEAPON,
        name="Withered Cork",
        cost=112,
        sell_value=28,
        phy_atk=17,
        mag_atk=18,
        equippable_by=[
            PlayerPartyCharacter.Reshan,
        ],
    )
