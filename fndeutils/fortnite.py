from datetime import datetime, timedelta, timezone

SEASON = 32
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
    27: [4, 5],
    28: [5, 1],
    29: [5, 2],
    30: [5, 3],
    31: [5, 4],
    32: [5, 5],
    33: [6, 1],
    34: [6, 2],
}

SEASON_COVER_URL = 'https://cdn1.epicgames.com/offer/fn/FNBR_33-00_C6S1_EGS_Launcher_KeyArt_Blade_1200x1600_1200x1600-70912f1f443af800d0fb55cff7ee5da7'
SEASON_COLOR = 0x391bed
SEASON_GRADIENT = [0x8b1ef6, 0x020951]
SEASON_START = datetime.fromtimestamp(1733022000, tz=timezone.utc)
SEASON_START_OFFSET = timedelta(hours=6.5)
SEASON_END = datetime.fromtimestamp(1740132000, tz=timezone.utc)
LAST_SEASON_START = datetime.fromtimestamp(1730527200, tz=timezone.utc)

EVENT_START = None

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'
