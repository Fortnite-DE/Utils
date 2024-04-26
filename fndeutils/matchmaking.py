MESSAGE_COUNT_OFFSET = 5

DELETE_AFK_LOBBY = 5 * 60 # 5 Minuten
VOICE_PENDING_TIME = 20 # 20 Sekunden
JOIN_REQUEST_TIME = 10 * 60 # 10 Minuten
CLOSE_AFK_THREADS = 60 * 60 # 1 Stunde
DELETE_OLD_THREADS = 24 * 60 * 60 # 1 Tag
DELETE_JOIN_LEFT_DATA = 24 * 60 * 60 # 1 Tag

FEEDBACK_TIME = 10 * 60 # 10 Minuten
FEEDBACK_COOLDOWN = 3 * 24 * 60 * 60 # 3 Tage
REPORT_KICK_CLEAN_TIME = 14 * 24 * 60 * 60 # 2 Wochen
STATS_UPDATE_TIME = 15 * 60 # 15 Minuten
SAVE_SEARCH_LIMIT = 10
DIVISION_RANGE = 3
TOURNAMENT_TIME = 5 * 60 * 60 # 5 Stunden

KICK_FACTOR = 4.0
REPORT_FACTOR = 2.5
JOIN_DATE_FACTOR = 1.0
FEEDBACK_FACTOR = 0.5

DIVISIONS = {
    0: "Bronze I",
    1: "Bronze II",
    2: "Bronze III",
    3: "Silber I",
    4: "Silber II",
    5: "Silber III",
    6: "Gold I",
    7: "Gold II",
    8: "Gold III",
    9: "Platin I",
    10: "Platin II",
    11: "Platin III",
    12: "Diamant I",
    13: "Diamant II",
    14: "Diamant III",
    15: "Elite",
    16: "Champion",
    17: "Unreal",
    18: "Unranked",
}

PLAYLIST_TYPES = {
    "Battle Royale": 0,
    "Battle Royale (no build)": 1,
    "Kreativmodus": 2,
    "UEFN": 3,
    "LEGO Fortnite": 4,
    "Rocket Racing": 5,
    "Fortnite Festival": 6,
    "Rette die Welt": 7,
}

RANKED_PLAYLIST_TYPES = {
    "ranked-br": 0,
    "ranked-zb": 1,
    "delmar-competitive": 5,
}
