# Module: Pixel Font (used by program 12, kit.py and the message mode of program 18)
# Filename: font.py
# Version: 1.0.0
#
# A tiny font for the matrix. Every letter is a small picture, 5 pixels
# tall. An "X" is a lit pixel and a "." is a dark one. Most letters are 3
# pixels wide. M and W need 5, N and Q need 4, and ! needs only 1.
# This file has no hardware in it: it is only the letter shapes.

LETTERS = {
    "A": (".X.", "X.X", "XXX", "X.X", "X.X"),
    "B": ("XX.", "X.X", "XX.", "X.X", "XX."),
    "C": (".XX", "X..", "X..", "X..", ".XX"),
    "D": ("XX.", "X.X", "X.X", "X.X", "XX."),
    "E": ("XXX", "X..", "XX.", "X..", "XXX"),
    "F": ("XXX", "X..", "XX.", "X..", "X.."),
    "G": (".XX", "X..", "X.X", "X.X", ".XX"),
    "H": ("X.X", "X.X", "XXX", "X.X", "X.X"),
    "I": ("XXX", ".X.", ".X.", ".X.", "XXX"),
    "J": ("..X", "..X", "..X", "X.X", ".X."),
    "K": ("X.X", "X.X", "XX.", "X.X", "X.X"),
    "L": ("X..", "X..", "X..", "X..", "XXX"),
    "M": ("X...X", "XX.XX", "X.X.X", "X...X", "X...X"),
    "N": ("X..X", "XX.X", "X.XX", "X..X", "X..X"),
    "O": (".X.", "X.X", "X.X", "X.X", ".X."),
    "P": ("XX.", "X.X", "XX.", "X..", "X.."),
    "Q": (".XX.", "X..X", "X..X", "X.X.", ".X.X"),
    "R": ("XX.", "X.X", "XX.", "X.X", "X.X"),
    "S": (".XX", "X..", ".X.", "..X", "XX."),
    "T": ("XXX", ".X.", ".X.", ".X.", ".X."),
    "U": ("X.X", "X.X", "X.X", "X.X", "XXX"),
    "V": ("X.X", "X.X", "X.X", "X.X", ".X."),
    "W": ("X...X", "X...X", "X.X.X", "XX.XX", "X...X"),
    "X": ("X.X", "X.X", ".X.", "X.X", "X.X"),
    "Y": ("X.X", "X.X", ".X.", ".X.", ".X."),
    "Z": ("XXX", "..X", ".X.", "X..", "XXX"),
    "0": ("XXX", "X.X", "X.X", "X.X", "XXX"),
    "1": (".X.", "XX.", ".X.", ".X.", "XXX"),
    "2": ("XXX", "..X", "XXX", "X..", "XXX"),
    "3": ("XXX", "..X", "XXX", "..X", "XXX"),
    "4": ("X.X", "X.X", "XXX", "..X", "..X"),
    "5": ("XXX", "X..", "XXX", "..X", "XXX"),
    "6": ("XXX", "X..", "XXX", "X.X", "XXX"),
    "7": ("XXX", "..X", "..X", "..X", "..X"),
    "8": ("XXX", "X.X", "XXX", "X.X", "XXX"),
    "9": ("XXX", "X.X", "XXX", "..X", "XXX"),
    " ": ("..", "..", "..", "..", ".."),
    "!": ("X", "X", "X", ".", "X"),
    "?": ("XX.", "..X", ".X.", "...", ".X."),
    ".": (".", ".", ".", ".", "X"),
    "-": ("...", "...", "XXX", "...", "..."),
}
