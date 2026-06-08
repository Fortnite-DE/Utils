from __future__ import annotations

from datetime import UTC, datetime
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
    "LEGO_EVENT_START",
    "LEGO_PASSES",
    "LEGO_SEASON",
    "LEGO_SEASON_COLOR",
    "LEGO_SEASON_COVER_URL",
    "LEGO_SEASON_END",
    "LEGO_SEASON_GRADIENT",
    "LEGO_SEASON_START",
    "OG_EVENT_START",
    "OG_SEASON",
    "OG_SEASONS",
    "OG_SEASON_COLOR",
    "OG_SEASON_COVER_URL",
    "OG_SEASON_END",
    "OG_SEASON_GRADIENT",
    "OG_SEASON_START",
    "SEASON",
    "SEASONS",
    "SEASON_COLOR",
    "SEASON_COVER_URL",
    "SEASON_END",
    "SEASON_GRADIENT",
    "SEASON_START",
    "get_fortnite_api_icon_link",
]

FORTNITE_API_ICON_LINK = "https://fortnite-api.com/assets/img/logo_small_128.png?t="


def get_fortnite_api_icon_link():
    return f"{FORTNITE_API_ICON_LINK}{datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}"


#########################################
############# Battle Royale #############
#########################################

SEASON = 41
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
    39: [7, 1],
    40: [7, 2],
    41: [7, 3],
}

SEASON_COVER_URL = "https://cdn1.epicgames.com/offer/fn/FNBR_41-00_C7S3_EGS_Launcher_Blade_1200x1600_1200x1600-95bf3eb7070b41cfa898b87732d14d63"
SEASON_COLOR = 0x360718
SEASON_GRADIENT = [0x375BAB, 0xFE1D2F]
SEASON_START = datetime(
    day=6, month=5, year=2026, hour=12, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)
SEASON_END = datetime(
    day=20, month=8, year=2026, hour=8, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)

EVENT_START = None

#########################################
############## Fortnite OG ##############
#########################################

OG_SEASON = 8
OG_SEASONS = SEASONS

OG_SEASON_COVER_URL = "https://cdn1.epicgames.com/offer/fn/EN_FN_OG_C1S8_40-10_EGS_Launcher_KeyArt_Blade_1200x1600_1200x1600-b326a8e7a0a44a72894df10fbcb96ccb"
OG_SEASON_COLOR = 0x7A02B2
OG_SEASON_GRADIENT = [0x7A02B2, 0x52018A]
OG_SEASON_START = datetime(
    day=1, month=4, year=2026, hour=12, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)
OG_SEASON_END = datetime(
    day=24, month=6, year=2026, hour=8, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)

OG_EVENT_START = None

########################################
############### Festival ###############
########################################

FESTIVAL_SEASON = 14
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
    12: "LISA",
    13: "Chappell Roan",
    14: "Laufey",
}

FESTIVAL_SEASON_COVER_URL = "https://cdn1.epicgames.com/offer/fn/FNSP_40-20_IndoorLace_KeyArt_EGS_Launcher_Blade_1200x1600_1200x1600-7a08eb9d039542d3b83361918a6f6e04"
FESTIVAL_SEASON_COLOR = 0xF7FB6F
FESTIVAL_SEASON_GRADIENT = [0xF7FB6F, 0xF7FB6F]
FESTIVAL_SEASON_START = datetime(
    day=15, month=4, year=2026, hour=12, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)
FESTIVAL_SEASON_END = datetime(
    day=29, month=7, year=2026, hour=8, minute=0, tzinfo=ZoneInfo("Europe/Berlin")
)

FESTIVAL_EVENT_START = None

########################################
################# LEGO #################
########################################

LEGO_SEASON = 10
LEGO_PASSES = {
    1: "Abenteuer der Rebellen",
    2: "Tropenschätze",
    5: "Goldrausch-Galerie",
    6: "Die Erste Ordnung",
    7: "Supernova Academy",
    8: "Palmenparadies",
    9: "Ninjago 1",
    10: "Ninjago 2",
}

LEGO_SEASON_COVER_URL = "https://cdn1.epicgames.com/offer/fn/FNSP_40-20_IndoorLace_KeyArt_EGS_Launcher_Blade_1200x1600_1200x1600-7a08eb9d039542d3b83361918a6f6e04"
LEGO_SEASON_COLOR = 0xED8109
LEGO_SEASON_GRADIENT = [0x321B0E, 0xAD2223]
LEGO_SEASON_START = datetime(day=16, month=4, year=2026, hour=12, minute=0, tzinfo=UTC)
LEGO_SEASON_END = datetime(day=2, month=9, year=2026, hour=8, minute=0, tzinfo=UTC)


LEGO_EVENT_START = None
