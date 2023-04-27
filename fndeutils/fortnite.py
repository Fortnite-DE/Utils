from datetime import datetime, timedelta

SEASON = 24
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
}
SEASON_COVER_URL = 'https://cdn1.epicgames.com/offer/fn/24BR_S24_EGS_Launcher_Blade_1200x1600_1200x1600-0f74a2c818a2b043fa684875eca49784'
SEASON_COLOR = 0x7700f0
SEASON_GRADIENT = [0x00c2ff, 0xeb5ed8]
SEASON_START = datetime.fromtimestamp(1678406400)
SEASON_START_OFFSET = timedelta(hours=12)
SEASON_END = datetime.fromtimestamp(1686290400)
ARENA_SEASON_START = datetime.fromtimestamp(1678406400)
LAST_SEASON_START = datetime.fromtimestamp(1670112001)
LAST_ARENA_SEASON_START = datetime.fromtimestamp(1670112001)

EVENT_START = None

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'
