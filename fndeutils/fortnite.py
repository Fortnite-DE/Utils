from datetime import datetime, timedelta, timezone
import discord
from redbot.core.i18n import Translator

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='

def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'

#########################################
############# Battle Royale #############
#########################################

SEASON = 33
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

SEASON_COVER_URL = 'https://cdn1.epicgames.com/offer/fn/FNBR_33-00_C6S1_EGS_Launcher_KeyArt_Blade_1200x1600_1200x1600-70912f1f443af800d0fb55cff7ee5da7'
SEASON_COLOR = 0x391bed
SEASON_GRADIENT = [0x8b1ef6, 0x020951]
SEASON_START = datetime.fromtimestamp(1733022000, tz=timezone.utc)
SEASON_START_OFFSET = timedelta(hours=6.5)
SEASON_END = datetime.fromtimestamp(1740132000, tz=timezone.utc)

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 1
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fn33-00-c1s1-discover-playlist-tiles-og-1920x1080-1920x1080-2a20f7eb1c14.jpg?resize=1&w=2560'
OG_SEASON_COLOR = 0x545a42
OG_SEASON_GRADIENT = [0xfdf465, 0xf3c516]
OG_SEASON_START = datetime.fromtimestamp(1733821200, tz=timezone.utc)
OG_SEASON_START_OFFSET = timedelta(hours=0)
OG_SEASON_END = datetime.fromtimestamp(1741680000, tz=timezone.utc)

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 6
FESTIVAL_ARTISTS = {
    1: "The Weeknd",
    2: "Lady Gaga",
    3: "Billie Eilish",
    4: "Metallica",
    5: "Karol G",
    6: "Snoop Dogg",
}

FESTIVAL_SEASON_COVER_URL = 'https://cdn2.unrealengine.com/de-fnsp-06-discoverytile-mainstage-1920x1080-1920x1080-9faef70179d3.jpg?resize=1&w=2560'
FESTIVAL_SEASON_COLOR = 0xf09efe
FESTIVAL_SEASON_GRADIENT = [0xeadc8c, 0xa77711]
FESTIVAL_SEASON_START = datetime(2024, 11, 2, 14, tzinfo=timezone.utc)
FESTIVAL_SEASON_START_OFFSET = timedelta(hours=0)
FESTIVAL_SEASON_END = datetime(2025, 1, 14, 14, tzinfo=timezone.utc)

FESTIVAL_EVENT_START = None
