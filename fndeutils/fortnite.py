from datetime import datetime, timedelta, timezone

SEASON = 26
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
}
SEASON_COVER_URL = 'https://cdn1.epicgames.com/offer/fn/26BR_C4S4_EGS_Launcher_Blade_1200x1600_1200x1600-72d477839e2f1e1a9b3847d0998f50bc'
SEASON_COLOR = 0xBC0020
SEASON_GRADIENT = [0x400408, 0xBC0020]
SEASON_START = datetime.fromtimestamp(1692921600, tz=timezone.utc)
SEASON_START_OFFSET = timedelta(hours=11)
SEASON_END = datetime.fromtimestamp(1698994800, tz=timezone.utc)
LAST_SEASON_START = datetime.fromtimestamp(1686265200, tz=timezone.utc)

EVENT_START = None

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'
