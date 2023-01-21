from enum import Enum, unique


@unique
class AccountType(Enum):
    NORMAL = "/m=hiscore_oldschool/index_lite.ws"
    IRONMAN = "/m=hiscore_oldschool_ironman/index_lite.ws"
    HARDCORE_IRONMAN = "/m=hiscore_oldschool_hardcore_ironman/index_lite.ws"
    ULTIMATE_IRONMAN = "/m=hiscore_oldschool_ultimate/index_lite.ws"
    DEADMAN = "/m=hiscore_oldschool_deadman/index_lite.ws"
    SEASONAL = "/m=hiscore_oldschool_seasonal/index_lite.ws"

    @classmethod
    def normal_types(cls):
        return [cls.NORMAL,
                cls.IRONMAN,
                cls.HARDCORE_IRONMAN,
                cls.ULTIMATE_IRONMAN]


# Thanks to
# http://mirekw.com/rs/RSDOnline/Guides/guide.aspx?file=Experience%20formula.html
# for the formula
def _build_xp_table():
    table = [0]
    xp = 0

    for level in range(1, 99):
        diff = int(level + 300 * (2 ** (level / 7.0)))
        xp += diff
        table.append(xp // 4)

    return table


# index retrives the amount of xp required for level index + 1
XP_TABLE = _build_xp_table()

SKILLS = [
    "attack",
    "defence",
    "strength",
    "hitpoints",
    "ranged",
    "prayer",
    "magic",
    "cooking",
    "woodcutting",
    "fletching",
    "fishing",
    "firemaking",
    "crafting",
    "smithing",
    "mining",
    "herblore",
    "agility",
    "thieving",
    "slayer",
    "farming",
    "runecrafting",
    "hunter",
    "construction",
]

MINIGAMES = [
    "League Points",
    "Bounty Hunter - Hunter",
    "Bounty Hunter - Rogue",
    "Clue Scrolls (all)",
    "Clue Scrolls (beginner)",
    "Clue Scrolls (easy)",
    "Clue Scrolls (medium)",
    "Clue Scrolls (hard)",
    "Clue Scrolls (elite)",
    "Clue Scrolls (master)",
    "LMS - Rank",
    "PvP Arena - Rank",
    "Soul Wars Zeal",
    "Rifts closed",
]

BOSSES = [
    "Abyssal Sire",
    "Alchemical Hydra",
    "Barrows Chests",
    "Bryophyta",
    "Callisto",
    "Cerberus",
    "Chambers of Xeric",
    "Chambers of Xeric: Challenge Mode",
    "Chaos Elemental",
    "Chaos Fanatic",
    "Commander Zilyana",
    "Corporeal Beast",
    "Crazy Archaeologist",
    "Dagannoth Prime",
    "Dagannoth Rex",
    "Dagannoth Supreme",
    "Deranged Archaeologist",
    "General Graardor",
    "Giant Mole",
    "Grotesque Guardians",
    "Hespori",
    "Kalphite Queen",
    "King Black Dragon",
    "Kraken",
    "Kree'Arra",
    "K'ril Tsutsaroth",
    "Mimic",
    "Nex",
    "Nightmare",
    "Phosani's Nightmare",
    "Obor",
    "Phantom Muspah",
    "Sarachnis",
    "Scorpia",
    "Skotizo",
    "Tempoross",
    "The Gauntlet",
    "The Corrupted Gauntlet",
    "Theatre of Blood",
    "Theatre of Blood: Hard Mode",
    "Thermonuclear Smoke Devil",
    "Tombs of Amascut",
    "Tombs of Amascut: Expert Mode",
    "TzKal-Zuk",
    "TzTok-Jad",
    "Venenatis",
    "Vet'ion",
    "Vorkath",
    "Wintertodt",
    "Zalcano",
    "Zulrah",
]

SKILLS_AMT = len(SKILLS)
MINIGAMES_AMT = len(MINIGAMES)
BOSSES_AMT = len(BOSSES)

BASE_URL = "http://services.runescape.com"

BASE_URL_GE = BASE_URL + "/m=itemdb_oldschool/"
GE_BY_ID = BASE_URL_GE + "api/catalogue/detail.json?item="

GE_ICON = BASE_URL_GE + "obj_sprite.gif?id="
GE_LARGE_ICON = BASE_URL_GE + "obj_big.gif?id="

OSBUDDY_PRICE_URI = "http://api.rsbuddy.com/grandExchange?a=guidePrice&i="
