from datetime import datetime, timedelta, timezone

SEASON = 31
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
}
SEASON_COVER_URL = 'https://cdn1.epicgames.com/offer/fn/Blade_1200x1600_1200x1600-fcea56f5eb92df731a89121e2b4416b5'
SEASON_COLOR = 0x101732
SEASON_GRADIENT = [0x101831, 0x2d447a]
SEASON_START = datetime.fromtimestamp(1723777200, tz=timezone.utc)
SEASON_START_OFFSET = timedelta(hours=5)
SEASON_END = datetime.fromtimestamp(1730527200, tz=timezone.utc)
LAST_SEASON_START = datetime.fromtimestamp(1716530400, tz=timezone.utc)

EVENT_START = None

FORTNITE_API_ICON_LINK = 'https://fortnite-api.com/assets/img/logo_small_128.png?t='


def get_fortnite_api_icon_link():
    return f'{FORTNITE_API_ICON_LINK}{datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0).timestamp()}'
