from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

FORTNITE_API_ICON_LINK = "https://fortnite-api.com/assets/img/logo_small_128.png?t="


def get_fortnite_api_icon_link():
    return f"{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}"


#########################################
############# Battle Royale #############
#########################################

SEASON = 36
SEASONS = {
    1: [1, 1],
    2: [1, 2],
    3: [1, 3],
    4: [1, 4],
    5: [1, 5],
    6: [1, 6],
    7: [1, 7],
    8: [1, 8],
    9: [1, 9],
    10: [1, 10],
    11: [2, 1],
    12: [2, 2],
    13: [2, 3],
    14: [2, 4],
    15: [2, 5],
    16: [2, 6],
    17: [2, 7],
    18: [2, 8],
    19: [3, 1],
    20: [3, 2],
    21: [3, 3],
    22: [3, 4],
    23: [4, 1],
    24: [4, 2],
    25: [4, 3],
    26: [4, 4],
    27: "Kapitel 1: OG",
    28: [5, 1],
    29: [5, 2],
    30: [5, 3],
    31: [5, 4],
    32: "Kapitel 2: Remix",
    33: [6, 1],
    34: [6, 2],
    35: "GALACTIC BATTLE",
    36: [6, 3],
}

SEASON_COVER_URL = (
    "https://cdn2.unrealengine.com/fnbr-36-00-c6s3-sonylauncher-coverart-3840x2160-logo-3840x2160-ed23e7986f8a.jpg"
)
SEASON_COLOR = 0xCF0C10
SEASON_GRADIENT = [0xA2C2C1, 0xFEFEFC]
SEASON_START = datetime(day=7, month=6, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
SEASON_START_OFFSET = timedelta(hours=0)
SEASON_END = datetime(day=7, month=8, year=2025, hour=7, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 4
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = "https://cdn2.unrealengine.com/de-fnfig-36-00-c1s4-egs-launcher-keyart-og-blade-2560x1440-2560x1440-de33b6b4d50b.jpg"
OG_SEASON_COLOR = 0xB161C0
OG_SEASON_GRADIENT = [0x42E1F6, 0xD3FEFB]
OG_SEASON_START = datetime(day=7, month=6, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
OG_SEASON_START_OFFSET = timedelta(hours=0)
OG_SEASON_END = datetime(day=7, month=8, year=2025, hour=7, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 9
FESTIVAL_ARTISTS = {
    1: "The Weeknd",
    2: "Lady Gaga",
    3: "Billie Eilish",
    4: "Metallica",
    5: "Karol G",
    6: "Snoop Dogg",
    7: "Hatsune Miku",
    8: "Sabrina Carpenter",
    9: "Bruno Mars",
}

FESTIVAL_SEASON_COVER_URL = "https://cdn2.unrealengine.com/de-fnsp-09-dryerase-discoverplaylisttile-1920x1080-1920x1080-b32681cd6a90.jpg?resize=1&w=2560"
FESTIVAL_SEASON_COLOR = 0x78E142
FESTIVAL_SEASON_GRADIENT = [0x3BCE1E, 0xFFDB10]
FESTIVAL_SEASON_START = datetime(day=17, month=6, year=2025, hour=10, minute=0, tzinfo=timezone.utc)
FESTIVAL_SEASON_START_OFFSET = timedelta(hours=0)
FESTIVAL_SEASON_END = datetime(day=26, month=8, year=2025, hour=9, minute=30, tzinfo=timezone.utc)

FESTIVAL_EVENT_START = None

########################################
################# LEGO #################
########################################

LEGO_SEASON = 5
LEGO_PASSES = {
    5: "Goldrausch-Galerie",
}

LEGO_SEASON_COVER_URL = (
    "https://cdn2.unrealengine.com/fortnite-rebel-oro-lego-style-thumbnail-576x576-768a2b70edd5.jpg?resize=1&w=2560"
)
LEGO_SEASON_COLOR = 0xED8109
LEGO_SEASON_GRADIENT = [0x321B0E, 0xAD2223]
LEGO_SEASON_START = datetime(day=11, month=3, year=2025, hour=10, minute=0, tzinfo=timezone.utc)
LEGO_SEASON_START_OFFSET = timedelta(hours=0)
LEGO_SEASON_END = datetime(day=2, month=5, year=2025, hour=10, minute=0, tzinfo=timezone.utc)


LEGO_EVENT_START = None
