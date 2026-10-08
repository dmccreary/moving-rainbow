# Module: Picture Gallery (used by program 10 and by the picture mode of program 18)
# Filename: pictures.py
# Version: 1.0.0
#
# Eight pictures for the 8x8 matrix. A picture is 8 rows of 8 letters, and
# each letter stands for a color in COLORS. A dot is a pixel that stays off.
# To add your own picture, write it like the ones below, then add a line
# for it to GALLERY at the bottom.
# This file has no hardware in it: it is only the pictures.

# the color key: which color each letter stands for. The numbers stay small
# because a picture can light all 64 pixels at once.
COLORS = {
    ".": (0, 0, 0),         # off
    "R": (32, 0, 0),        # red
    "O": (32, 10, 0),       # orange
    "Y": (28, 22, 0),       # yellow
    "G": (0, 28, 0),        # green
    "C": (0, 22, 22),       # cyan (blue-green)
    "B": (0, 0, 32),        # blue
    "V": (16, 0, 28),       # violet
    "P": (32, 6, 14),       # pink
    "W": (18, 18, 18),      # white
    "N": (14, 6, 0),        # brown
}

SMILEY = [
    "..YYYY..",
    ".YYYYYY.",
    "YYBYYBYY",
    "YYYYYYYY",
    "YRYYYYRY",
    "YYRRRRYY",
    ".YYYYYY.",
    "..YYYY..",
]

HEART = [
    ".RR..RR.",
    "RPRRRRRR",
    "RRRRRRRR",
    "RRRRRRRR",
    ".RRRRRR.",
    "..RRRR..",
    "...RR...",
    "........",
]

ALIEN = [
    "...GG...",
    "..GGGG..",
    ".GGGGGG.",
    "GG.GG.GG",
    "GGGGGGGG",
    "..G..G..",
    ".G.GG.G.",
    "G.G..G.G",
]

GHOST = [
    "..WWWW..",
    ".WWWWWW.",
    "WBBWWBBW",
    "WBBWWBBW",
    "WWWWWWWW",
    "WWWWWWWW",
    "WWWWWWWW",
    "W.WW.WW.",
]

RAINBOW = [
    "........",
    "..RRRR..",
    ".RYYYYR.",
    "RYGGGGYR",
    "RYGBBGYR",
    "RYG..GYR",
    "WWW..WWW",
    ".W....W.",
]

FLOWER = [
    "...PP...",
    ".PPPPPP.",
    ".PPYYPP.",
    ".PPPPPP.",
    "...PP...",
    "...GG...",
    ".G.GG.G.",
    "..GGGG..",
]

FISH = [
    "........",
    "..CCC...",
    ".CCCCC.C",
    "CWCCCCCC",
    "CCCCCCCC",
    ".CCCCC.C",
    "..CCC...",
    "........",
]

ROCKET = [
    "...WW...",
    "..WWWW..",
    "..WBBW..",
    "..WWWW..",
    "..WWWW..",
    ".RWWWWR.",
    ".R.OO.R.",
    "...YY...",
]

# the order the pictures are shown in: (name, picture)
GALLERY = [
    ("Smiley", SMILEY),
    ("Heart", HEART),
    ("Alien", ALIEN),
    ("Ghost", GHOST),
    ("Rainbow", RAINBOW),
    ("Flower", FLOWER),
    ("Fish", FISH),
    ("Rocket", ROCKET),
]
