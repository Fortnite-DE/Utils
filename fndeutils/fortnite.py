from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'


#########################################
############# Battle Royale #############
#########################################

SEASON = 34
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
}

SEASON_COVER_URL = 'https://cdn2.unrealengine.com/fnbr-34-00-c6s2-discover-playlist-tiles-keyart-1920x1080-1920x1080-6877a7dfe21c.jpg?resize=1&w=2560'
SEASON_COLOR = 0x735c75
SEASON_GRADIENT = [0x9C7650, 0x4A4397]
SEASON_START = datetime(day=21, month=2, year=2025, hour=13, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
SEASON_END = datetime(day=2, month=5, year=2025, hour=10, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 2
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fn33-00-c1s1-discover-playlist-tiles-og-1920x1080-1920x1080-9c81a114f52d.jpg?resize=1&w=1600'
OG_SEASON_COLOR = 0x545A42
OG_SEASON_GRADIENT = [0xFFA515, 0xF3DB24]
OG_SEASON_START = datetime.fromtimestamp(1738314000, tz=timezone.utc)
OG_SEASON_START_OFFSET = timedelta(hours=0)
OG_SEASON_END = datetime.fromtimestamp(1742893200, tz=timezone.utc)

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 7
FESTIVAL_ARTISTS = {
    1: "The Weeknd",
    2: "Lady Gaga",
    3: "Billie Eilish",
    4: "Metallica",
    5: "Karol G",
    6: "Snoop Dogg",
    7: "Hatsune Miku"
}

FESTIVAL_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fnsp-07-discoverytile-mainstage-1920x1080-1920x1080-f838ca292932.jpg?resize=1&w=1600'
FESTIVAL_SEASON_COLOR = 0x33c9f0
FESTIVAL_SEASON_GRADIENT = [0x2b72b3, 0x8fe9fd]
FESTIVAL_SEASON_START = datetime(2025, 1, 14, 11, tzinfo=timezone.utc)
FESTIVAL_SEASON_START_OFFSET = timedelta(hours=0)
FESTIVAL_SEASON_END = datetime(2025, 4, 8, 8, 30, tzinfo=timezone.utc)

FESTIVAL_EVENT_START = None
