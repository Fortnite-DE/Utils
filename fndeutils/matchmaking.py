MESSAGE_COUNT_OFFSET = 5

DELETE_AFK_LOBBY = 5 * 60  # 5 Minuten
VOICE_PENDING_TIME = 20  # 20 Sekunden
JOIN_REQUEST_TIME = 10 * 60  # 10 Minuten
CLOSE_AFK_THREADS = 30 * 60  # 30 Minuten
DELETE_OLD_THREADS = 24 * 60 * 60  # 1 Tag
DELETE_JOIN_LEFT_DATA = 24 * 60 * 60  # 1 Tag

FEEDBACK_TIME = 10 * 60  # 10 Minuten
FEEDBACK_COOLDOWN = 3 * 24 * 60 * 60  # 3 Tage
REPORT_KICK_CLEAN_TIME = 14 * 24 * 60 * 60  # 2 Wochen
STATS_UPDATE_TIME = 15 * 60  # 15 Minuten
SAVE_SEARCH_LIMIT = 10
DIVISION_RANGE = 3
TOURNAMENT_TIME = 5 * 60 * 60  # 5 Stunden

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
    "OG Battle Royale": 2,
    "OG Battle Royale (no build)": 3,
    "Reload": 4,
    "Reload (no build)": 5,
    "LTM": 6,
    "Kreativmodus": 7,
    "UEFN": 8,
    "LEGO Fortnite": 9,
    "Rocket Racing": 10,
    "Fortnite Festival": 11,
    "Rette die Welt": 12,
}

RANKED_PLAYLIST_TYPES = {
    "ranked-br": 0,
    "ranked-zb": 1,
    "ranked_blastberry_build": 4,
    "ranked_blastberry_nobuild": 5,
    "delmar-competitive": 10,
}
