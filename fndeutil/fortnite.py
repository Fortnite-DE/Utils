from datetime import datetime, timedelta

SEASON = 22
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
    23: [3, 5],
}
SEASON_COVER = 'https://cdn1.epicgames.com/offer/fn/22BR_C3S4_EGS_StoreArt_Blade_1200x1600_1200x1600-0f4096bc5da796d51594e14f3e340eac'
SEASON_COLOR = 0x6c128e
SEASON_GRADIENT = [0x6c128e, 0x932d9b]
SEASON_START = datetime.fromtimestamp(1663459201)
SEASON_START_OFFSET = timedelta(hours=12)
SEASON_END = datetime.fromtimestamp(1670058000)
ARENA_SEASON_START = datetime.fromtimestamp(1663459201)
LAST_SEASON_START = datetime.fromtimestamp(1654387201)
LAST_ARENA_SEASON_START = datetime.fromtimestamp(1655805600)

EVENT_START = None
