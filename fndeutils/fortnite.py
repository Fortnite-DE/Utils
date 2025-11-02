from __future__ import annotations

from datetime import UTC, datetime, timedelta
from zoneinfo import ZoneInfo

__all__ = [
    "EVENT_START",
    "FESTIVAL_ARTISTS",
    "FESTIVAL_EVENT_START",
    "FESTIVAL_SEASON",
    "FESTIVAL_SEASON_COLOR",
    "FESTIVAL_SEASON_COVER_URL",
    "FESTIVAL_SEASON_END",
    "FESTIVAL_SEASON_GRADIENT",
    "FESTIVAL_SEASON_START",
    "FESTIVAL_SEASON_START_OFFSET",
    "LEGO_EVENT_START",
    "LEGO_PASSES",
    "LEGO_SEASON",
    "LEGO_SEASON_COLOR",
    "LEGO_SEASON_COVER_URL",
    "LEGO_SEASON_END",
    "LEGO_SEASON_GRADIENT",
    "LEGO_SEASON_START",
    "LEGO_SEASON_START_OFFSET",
    "OG_EVENT_START",
    "OG_SEASON",
    "OG_SEASONS",
    "OG_SEASON_COLOR",
    "OG_SEASON_COVER_URL",
    "OG_SEASON_END",
    "OG_SEASON_GRADIENT",
    "OG_SEASON_START",
    "OG_SEASON_START_OFFSET",
    "SEASON",
    "SEASONS",
    "SEASON_COLOR",
    "SEASON_COVER_URL",
    "SEASON_END",
    "SEASON_GRADIENT",
    "SEASON_START",
    "SEASON_START_OFFSET",
    "get_fortnite_api_icon_link",
]

FORTNITE_API_ICON_LINK = "https://fortnite-api.com/assets/img/logo_small_128.png?t="


def get_fortnite_api_icon_link():
    return f"{FORTNITE_API_ICON_LINK}{datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}"


#########################################
############# Battle Royale #############
#########################################

SEASON = 38
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
    37: [6, 4],
    38: "the Simpsons",
}

SEASON_COVER_URL = "https://media.discordapp.net/attachments/1423792767238410301/1434374494130278410/cdn-uploader-FNBR_38-00_C6MS2_BR_DiscoverPlaylistTile_-1920x1080-68ccc1fb.png?ex=6908c198&is=69077018&hm=6450453575b4ce3d535648cfbf3ce8df2d900f2e3f4330279f994c52e8ec8a2f&=&format=webp&quality=lossless&width=2112&height=1188"
SEASON_COLOR = 0xFDC200
SEASON_GRADIENT = [0xFDC200, 0xE55421]
SEASON_START = datetime(day=1, month=11, year=2025, hour=1, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))
SEASON_START_OFFSET = timedelta(hours=0)
SEASON_END = datetime(day=29, month=11, year=2025, hour=7, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 6
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = "https://media.discordapp.net/attachments/1423792767238410301/1423804806199509093/de-fnfigment-37-00-c1s6-egs-launcher-keyart-carousel-pdp-2560x1440-logo-2560x1440-bda8f6afb9a5.png?ex=6908894e&is=690737ce&hm=6a10c941315927fcaf057a595d160a90849b49f42b4c95d4617a3d7cf6cf27da&=&format=webp&quality=lossless&width=605&height=340"
OG_SEASON_COLOR = 0x7A02B2
OG_SEASON_GRADIENT = [0x7A02B2, 0x52018A]
OG_SEASON_START = datetime(day=2, month=10, year=2025, hour=11, minute=0, tzinfo=ZoneInfo("Europe/Berlin"))
OG_SEASON_START_OFFSET = timedelta(hours=0)
OG_SEASON_END = datetime(day=11, month=12, year=2025, hour=8, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 11
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
    10: "Gorillaz",
    11: "Mixtape",
}

FESTIVAL_SEASON_COVER_URL = "https://media.discordapp.net/attachments/1423792767238410301/1434356215118434414/cdn-uploader-DE_FNSP_37-50_S11MusicPass_KeyArt_DiscoverPlaylistTile_-1920x1080-18e19bbe.png?ex=6908b092&is=69075f12&hm=cd66658ec5d9b0b16e98d25357aad24f0c080e982200db970fa8e5513b0501f1&=&format=webp&quality=lossless&width=2112&height=1188"
FESTIVAL_SEASON_COLOR = 0xF7FB6F
FESTIVAL_SEASON_GRADIENT = [0xF7FB6F, 0xF7FB6F]
FESTIVAL_SEASON_START = datetime(day=9, month=10, year=2025, hour=11, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))
FESTIVAL_SEASON_START_OFFSET = timedelta(hours=0)
FESTIVAL_SEASON_END = datetime(day=29, month=11, year=2025, hour=7, minute=30, tzinfo=ZoneInfo("Europe/Berlin"))

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
LEGO_SEASON_START = datetime(day=11, month=3, year=2025, hour=10, minute=0, tzinfo=UTC)
LEGO_SEASON_START_OFFSET = timedelta(hours=0)
LEGO_SEASON_END = datetime(day=2, month=5, year=2025, hour=10, minute=0, tzinfo=UTC)


LEGO_EVENT_START = None
