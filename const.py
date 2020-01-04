class AccountType(object):
    NORMAL = 0
    IRONMAN = 1
    HARDCORE_IRONMAN = 2
    ULTIMATE_IRONMAN = 3
    DEADMAN = 4
    DEADMAN_SEASONAL = 5


# Thanks to http://mirekw.com/rs/RSDOnline/Guides/guide.aspx?file=Experience%20formula.html for the formula
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

UNUSED_OR_UNKNOWN = (
    "UNUSED_OR_UNKNOWN"  # Some rows in the API response don't seem to map to anything
)

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
    UNUSED_OR_UNKNOWN,
    "Bounty Hunter",
    "Bounty Hunter Rogue",
    "Clue Scrolls (all)",
    "Clue Scrolls (beginner)",
    "Clue Scrolls (easy)",
    "Clue Scrolls (medium)",
    "Clue Scrolls (hard)",
    "Clue Scrolls (elite)",
    "Clue Scrolls (master)",
    "Last Man Standing",
]

BOSSES = [
    "Abyssal Sire",
    "Alchemical Hydra",
    "Barrows Chests",
    UNUSED_OR_UNKNOWN,
    "Chambers of Xeric",
    UNUSED_OR_UNKNOWN,
    "Chaos Elemental",
    "Chaos Fanatic",
    "Commander Zilyana",
    UNUSED_OR_UNKNOWN,
    "Crazy Archaeologist",
    "Dagannoth Prime",
    "Dagannoth Rex",
    "Dagannoth Supreme",
    UNUSED_OR_UNKNOWN,
    "General Graardor",
    "Giant Mole",
    UNUSED_OR_UNKNOWN,
    "Hespori",
    "Kalphite Queen",
    "King Black Dragon",
    "Kraken",
    "Kree'Arra",
    "K'ril Tsutsaroth",
    UNUSED_OR_UNKNOWN,
    UNUSED_OR_UNKNOWN,
    UNUSED_OR_UNKNOWN,
    "Scorpia",
    "Skotizo",
    UNUSED_OR_UNKNOWN,
    UNUSED_OR_UNKNOWN,
    UNUSED_OR_UNKNOWN,
    "Thermonuclear Smoke Devil",
    UNUSED_OR_UNKNOWN,
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
HISCORE_URLS = [
    "/m=hiscore_oldschool/index_lite.ws",
    "/m=hiscore_oldschool_ironman/index_lite.ws",
    "/m=hiscore_oldschool_hardcore_ironman/index_lite.ws",
    "/m=hiscore_oldschool_ultimate/index_lite.ws",
    "/m=hiscore_oldschool_deadman/index_lite.ws",
    "/m=hiscore_oldschool_seasonal/index_lite.ws",
]

BASE_URL_GE = BASE_URL + "/m=itemdb_oldschool/"
GE_BY_ID = BASE_URL_GE + "api/catalogue/detail.json?item="

GE_ICON = BASE_URL_GE + "obj_sprite.gif?id="
GE_LARGE_ICON = BASE_URL_GE + "obj_big.gif?id="

OSBUDDY_PRICE_URI = "http://api.rsbuddy.com/grandExchange?a=guidePrice&i="
