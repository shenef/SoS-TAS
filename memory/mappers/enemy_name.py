class EnemyName:
    """Static namespace for guid to enemy name mapping."""

    NAMES = {
        # Evermist Island: Mountain Trail
        "c3a2f1d99be4e0c42aca0ae1ff590028": "Wanderer",
        "fc2736fdbb731394c98da56e8f476d5e": "Rochèvre",
        # Evermist Island: Final Trial
        "a9b692dccd6e2a748abe6f848cff857e": "Training Croube",
        "8beb20a7311444a47b1764ae7ace6658": "Wyrd",
        # Evermist Island: Forbidden Cave
        "f526fdd8553bd7344a34243f16f8fc96": "Luslug",
        "5750f181921e1f349b595e8e47760d33": "Bosslug",
        "3c02795df7f5ec647b8ba102263e7574": "Acid Bug",
        # Elder Mist Trials
        "72351ffc3ecd46d46bf11cec4eee353a": "Tern",
        "962aa552d33fc124782b230fce9185ce": "Elder Mist",
        "ddc4a3bbf0edb9945ba4b06f96f9c20e": "Elder Mist's Sword",
        # Sleeper Island: Moorlands
        "e6ac627711e4ee44da103c47d1cd5736": "Ant Bruiser",
        "2a9a0b40f493b11429febb5d927ef84b": "Srower",
        "d0f2cf59f69f42842ac0703193f39c85": "Salamander",
        "810980f005079324fb9fb643243eccee": "Malkomud",
        "fc51f181f5f913f4e99195da947b1425": "Malkomount",
        # Wraith Island: Cursed Woods
        "f93fa5cbb04648047902c7c612f418ee": "Lonzon",
        "6dd1189ece4445c48a7fb978f16eb797": "Boulbe",
        "01101b1b5a47ca14b8979f4597514a59": "Woodland Spirit",
        "30372e1cddf4d8245861bd27363d5f9a": "Arentee",
        # Wraith Island: Necromancer's Lair
        "4cc1949eb31a81a4782b1075c32d268e": "Gulgul",
        "f8de7842d6be99b40a6d8160044b5f62": "Mermofwizquard",
        "a5d5e39e2ca42bb43b343c4cde2ec1e7": "Revenant",
        "5cdedb65d17f3b24c8b7ad5bcbe1bea6": "Romaya",
        "30bd6b9747d75724496a60116d875f96": "Bone Pile",
        "ebf760c7aea1c1d46b18e9db92c5af76": "Flesh Pile",
        # Wraith Island: Haunted Mansion
        "8c69440417c1b28438d94128cd86af6d": "SpellBook",
        "d98c3fb06819d104aa554170cbc05e56": "Waltzers",
        "64246a3a9059257409ea628466ced26e": "Botanical Horror",
        "3bbc6ad42918c444c9947d156e7674aa": "Bottom Flower",
        "621eeda6cacd76740b9b24518c3d211b": "Top Flower",
        "807fd9a36ea523f4aa7d532ddc565a69": "Dweller of Woe",
        "e1685476dd793e44c9c8909fe0b3622f": "DoW Clone",
        "bcde1eb0ea076f846a0ee20287d88204": "DoW Phase 2",
        "ec0b935c78a26044f89a236921671642": "Brugraves?",
        "1dc70fb2d0f1b374cbecf052b953824b": "Erlina?",
        # Watcher Island: Jungle Path
        "d34eee0d16a720248a3ce2e6ce2b108b": "Skullpion",
        "fb69218273345394baef9abf6fa9a345": "Prapra",
        "50229dee567088647809e9b737b397b7": "Croube",
        # Watcher Island: Torment Peak
        "40f05ed0202783449a704978e8670c9b": "Tsiclop",
        "c6f57cbee5d9cff4a82778ce36f94fdf": "Sleuth",
        "e79eceacb415fd04f84e6da6f9b23d3d": "BilePile",
        # Mesa Island: Glacial Peak
        "a1a5c1333a1e7fe4f98de4d28b3b9900": "Rochecrossidere",
        "33a6c54c83b68894a93b46c02da7fbc8": "Boulder Douche",
        # Mesa Island: Autumn Hills
        "51b36d4dce9be614f95e77477caecace": "Tock",
        "2c78ebcab00eb2c4daef5082c88503cc": "Grassassin",
        "c99b902697c6f734f9fc64b421c06728": "Leaf Monster",
        # Mesa Island: Songshroom Marsh
        "0af340a99d84e2f4a98c5d9b617fe0ea": "Fungtoise",
        "acf70102f6cc47e41b953fc2c44ad802": "Shroomy Shroomy Knight",
        # Mesa Island: Clockwork Castle
        "3e00a15f95b3e1d4cb68e71021579758": "Cukoo Monster",
        "090c2ec246656b643a5d1e5b0bb3db28": "Clock Zombie",
        "ffe45f0323cb8924e8296b7cc86d9d1b": "Strife Minion",
        "cc767e360aab54d4ca314a206e32ffee": "Brugraves",
        "1894c41627be94d408bd64295ab6dd18": "Erlina",
        "a5d39cc10d1848d478b59c892f636e3b": "Dweller of Strife",
        # The Acolytes
        "76c4290aa2a896b4cb405e5a2d29b3a0": "One",
        "73c4c0922e5ae274eb759f86702353a8": "Two",
        "e77c07b22ee83854e8c006101ef5731f": "Three",
        "0c831eb6bc1c0c648828b405cb8c0667": "Four",
        # Skylands
        "4e00be6b55350d64090bff46533eb2aa": "SlingRabbit",
        "9cbcb4063d9b8d8448cf96a2c14a6826": "Braidzard",
        # Kiln Mountain
        "f08a6f708a24d87499439e14326c7a59": "Firecracker",
        "eb913e79ba73fd24c809490043822d62": "BigBuggy",
        "816de006c125b9b4eaa7139bac5c6b77": "Toadcano",
        # Trek to the center of the world
        "6db3b04b05f18ae48a952691c0edc99f": "Ant Bruiser",
        "e0e39853cf0aedc4a87abc25605ea4a6": "GooGoon",
        "5e1fb9276fd3e714d8fe1a4cfa8681af": "Woodland Spirit",
        "d788814517a8e1549b0253e534126938": "Rochèvre",
        "f875c492e9ff81d46917be56218ba834": "Kunus'nuku Acolyte",
        "d7cdfe62090e94047991a1b9ca612a6d": "Lonzon",
        "7181b3e6a1edf44409d05e9b51b86f02": "Garnooy",
        # Cerulean Expanse
        "bbaa918249ce3a04883d88eca37cf348": "Drone",
        "99c8b97ca2edc2644ab9b57832c9984c": "Ronin Cowboy",
        "68f9357277cff414eb0bf287dabd1cb0": "Hoarsemech",
        # Aephorul's Workshop/Lost Ones Hamlet
        "bb02eb1602e1ec142b85cd6b505ef5b6": "Meduso",
        "79150c51ef673bd49a3e5b83af4c5f8c": "Canister",
        # Sacrosanct Spires
        "09b42ce72465d8149997ff1d7bb8708a": "Anointed",
        "5ca276f08b35cd448b7458d85cc8ee5b": "Scout",
        "a071d2cccf4848746bbc63e27a0af3b9": "Owlsassin",
    }

    @staticmethod
    def get(guid: str) -> str:
        """Fetch name from the mapping."""
        return EnemyName.NAMES.get(guid)
