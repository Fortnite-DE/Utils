from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'


#########################################
############# Battle Royale #############
#########################################

SEASON = 35
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
    35: "GALACTIC BATTLE"
}

SEASON_COVER_URL = 'https://fortnite.gg/img/seasons/bg/35.jpg'
SEASON_COLOR = 0x8F5780
SEASON_GRADIENT = [0xD4302B, 0x4281E0]
SEASON_START = datetime(day=2, month=5, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
SEASON_START_OFFSET = timedelta(hours=0)
SEASON_END = datetime(day=7, month=6, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 3
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fn33-00-c1s3-discover-playlist-tiles-og-1920x1080-1920x1080-0413194f4108.jpg?resize=1&w=1920'
OG_SEASON_COLOR = 0x545A42
OG_SEASON_GRADIENT = [0xFFA515, 0xF3DB24]
OG_SEASON_START = datetime(day=25, month=3, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
OG_SEASON_START_OFFSET = timedelta(hours=0)
OG_SEASON_END = datetime(day=8, month=6, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 8
FESTIVAL_ARTISTS = {
    1: "The Weeknd",
    2: "Lady Gaga",
    3: "Billie Eilish",
    4: "Metallica",
    5: "Karol G",
    6: "Snoop Dogg",
    7: "Hatsune Miku",
    8: "Sabrina Carpenter"
}

FESTIVAL_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fnsp-08-discoverytile-mainstage-1920x1080-1920x1080-f02b954abedb.jpg?resize=1&w=1600'
FESTIVAL_SEASON_COLOR = 0xdfc47a
FESTIVAL_SEASON_GRADIENT = [0xDDBC55, 0xE6D8D6]
FESTIVAL_SEASON_START = datetime(day=8, month=4, year=2025, hour=10, minute=0, tzinfo=timezone.utc)
FESTIVAL_SEASON_START_OFFSET = timedelta(hours=0)
FESTIVAL_SEASON_END = datetime(day=17, month=6, year=2025, hour=10, minute=0, tzinfo=timezone.utc)

FESTIVAL_EVENT_START = None

########################################
################# LEGO #################
########################################

LEGO_SEASON = 5
LEGO_PASSES = {
    5: "Goldrausch-Galerie",
}

LEGO_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/fortnite-rebel-oro-lego-style-thumbnail-576x576-768a2b70edd5.jpg?resize=1&w=2560'
LEGO_SEASON_COLOR = 0xed8109
LEGO_SEASON_GRADIENT = [0x321B0E, 0xAD2223]
LEGO_SEASON_START = datetime(day=11, month=3, year=2025, hour=10, minute=0, tzinfo=timezone.utc)
LEGO_SEASON_START_OFFSET = timedelta(hours=0)
LEGO_SEASON_END = datetime(day=2, month=5, year=2025, hour=10, minute=0, tzinfo=timezone.utc)


LEGO_EVENT_START = None
