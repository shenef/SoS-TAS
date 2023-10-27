"""Static namespace to hold food definitions."""

from engine.inventory.item import FoodItem


class FOOD:
    """Static namespace to hold food definitions."""

    BasicSalad = FoodItem(
        guid="68c337d503ebc7e4a837052ed38452b5",
        name="Basic Salad",
        order_prio=20,
        cost=10,
        sell_value=15,
        hp_to_restore=35,
    )
    BerryJam = FoodItem(
        guid="74a5e5d26b56b7e429c36d1acb84a120",
        name="Berry Jam",
        order_prio=9,
        cost=10,
        sell_value=5,
        mp_to_restore=5,
    )
    Bouillabaisse = FoodItem(
        guid="f2868459715d3df45ad1da473d197ac6",
        name="Bouillabaisse",
        order_prio=45,
        cost=28,
        sell_value=14,
        hp_to_restore=110,
        mp_to_restore=6,
    )
    Braise = FoodItem(
        guid="512b3f049d35cbd4eb4648aa5a1105f6",
        name="Braise",
        order_prio=79,
        cost=76,
        sell_value=38,
        hp_use_percent=True,
        mp_use_percent=True,
        hp_percent_to_restore=1.0,
        mp_percent_to_restore=1.0,
    )
    ChampionsOmelette = FoodItem(
        guid="5608bed7407aae34ba3012feba387b00",
        name="Champions Omelette",
        order_prio=70,
        cost=56,
        sell_value=28,
        hp_to_restore=255,
    )
    Chaudree = FoodItem(
        guid="71853a3bd516511428ea6d23bc7eb34f",
        name="Chaudree",
        order_prio=24,
        cost=12,
        sell_value=6,
        mp_to_restore=8,
    )
    Croustade = FoodItem(
        guid="46bfb5ae7593f8f4bb870c9644635a99",
        name="Croustade",
        order_prio=47,
        cost=64,
        sell_value=32,
        is_aoe=True,
        hp_to_restore=80,
        mp_to_restore=7,
    )
    MooncradleFishPie = FoodItem(
        guid="6e613ca39c27bff49ae0da1773c6ab03",
        name="Mooncradle Fish Pie",
        order_prio=38,
        cost=36,
        sell_value=18,
        is_aoe=True,
        hp_to_restore=55,
        mp_to_restore=5,
    )
    GourmetBurger = FoodItem(
        guid="918caccd92d8f7540929427a743d1f15",
        name="Gourmet Burger",
        order_prio=55,
        cost=40,
        sell_value=20,
        hp_to_restore=175,
        mp_to_restore=7,
    )
    HeartyStew = FoodItem(
        guid="a4a1c78380553e74bb92899ddcd62440",
        name="Hearty Stew",
        order_prio=40,
        cost=32,
        sell_value=16,
        hp_to_restore=90,
    )
    HerbedFilet = FoodItem(
        guid="88bc64e502aab364f800ff8b94427f5f",
        name="Herbed Filet",
        order_prio=25,
        cost=8,
        sell_value=4,
        hp_to_restore=50,
    )
    Lasagna = FoodItem(
        guid="e8908ed6c2bd60f4bb4042067baa2a8c",
        name="Lasagna",
        order_prio=68,
        cost=72,
        sell_value=36,
        is_aoe=True,
        hp_to_restore=180,
    )
    LegendaryFeast = FoodItem(
        guid="425a2ecc6c4b87c4d89735500c6c9d95",
        name="Legendary Feast",
        order_prio=80,
        cost=90,
        sell_value=45,
        is_aoe=True,
        hp_use_percent=True,
        mp_use_percent=True,
        hp_percent_to_restore=1.0,
        mp_percent_to_restore=1.0,
    )
    MushroomScramble = FoodItem(
        guid="c1866d6de70d4834b951c06d4ae23306",
        name="Mushroom Scramble",
        order_prio=21,
        cost=18,
        sell_value=9,
        hp_to_restore=35,
        mp_to_restore=5,
    )
    MushroomSoup = FoodItem(
        guid="df724719b2fbf6e40a85e8f9bc4ccae2",
        name="Mushroom Soup",
        order_prio=35,
        cost=26,
        sell_value=13,
        is_aoe=True,
        hp_to_restore=40,
    )
    PainDore = FoodItem(
        guid="f6b47783588bed64e9fa44dba59b4a49",
        name="Pain Dore",
        order_prio=49,
        cost=50,
        sell_value=25,
        is_aoe=True,
        mp_to_restore=9,
    )
    # TODO(orkaboy): Cures KO + 50%
    Papillotte = FoodItem(
        guid="9151230a300ed934bbd8d6c1c659fc34",
        name="Papillotte",
        order_prio=31,
        cost=14,
        sell_value=7,
    )
    # TODO(orkaboy): Cures KO + 75%
    Parfait = FoodItem(
        guid="fceb00c496ecb5844b14022ba450de53",
        name="Parfait",
        order_prio=48,
        cost=24,
        sell_value=12,
    )
    PeachStrudel = FoodItem(
        guid="d508421fae4fe5549a21d767a5d7d10c",
        name="Peach Strudel",
        order_prio=44,
        cost=32,
        sell_value=16,
        mp_to_restore=12,
    )
    # TODO(orkaboy): Cures KO + 100%
    Poutine = FoodItem(
        guid="8af2d2fccb35a0f43a965bbdd7a993f1",
        name="Poutine",
        order_prio=78,
        cost=32,
        sell_value=16,
    )
    PuddingChomeur = FoodItem(
        guid="52004597d9485634dbd4fca16b151c89",
        name="Pudding Chomeur",
        order_prio=69,
        cost=36,
        sell_value=18,
        mp_use_percent=True,
        mp_percent_to_restore=1.0,
    )
    RoastSandwich = FoodItem(
        guid="520e9f55dc3432a498ec389a59d7401f",
        name="Roast Sandwich",
        order_prio=30,
        cost=16,
        sell_value=8,
        hp_to_restore=60,
    )
    Sashimi = FoodItem(
        guid="92dbbdececf32284eb6868f3529ff7ac",
        name="Sashimi",
        order_prio=50,
        cost=18,
        sell_value=9,
        hp_to_restore=155,
    )
    SurfAndTurfTataki = FoodItem(
        guid="b504e699b3af5ab4faa0b252ff7d49f6",
        name="Surf And Turf Tataki",
        order_prio=65,
        cost=48,
        sell_value=24,
        is_aoe=True,
        hp_to_restore=135,
        mp_to_restore=8,
    )
    TomatoClub = FoodItem(
        guid="1aafd2f9435698349a63a99837e9104e",
        name="Tomato Club",
        order_prio=10,
        cost=8,
        sell_value=4,
        hp_to_restore=20,
    )
    YakitoriShrimp = FoodItem(
        guid="547cb5586279b80489ace061c33eb861",
        name="Yakitori Shrimp",
        order_prio=65,
        cost=18,
        sell_value=9,
        mp_to_restore=15,
    )
