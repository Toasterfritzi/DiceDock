"""Zauberplatz-Tabelle – D&D 2024."""

# Zauberplätze pro Stufe für Vollzauberwirker (Barde, Kleriker, Druide, Zauberer, Magier)
VOLLZAUBERWIRKER = {
    1:  {1: 2},
    2:  {1: 3},
    3:  {1: 4, 2: 2},
    4:  {1: 4, 2: 3},
    5:  {1: 4, 2: 3, 3: 2},
    6:  {1: 4, 2: 3, 3: 3},
    7:  {1: 4, 2: 3, 3: 3, 4: 1},
    8:  {1: 4, 2: 3, 3: 3, 4: 2},
    9:  {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    10: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
    11: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
    12: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1},
    13: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
    14: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1},
    15: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
    16: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1},
    17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1},
    18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 1, 7: 1, 8: 1, 9: 1},
    19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 1, 8: 1, 9: 1},
    20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 1},
}

# Halbzauberwirker (Paladin, Waldläufer): halbe Stufe → Slots
HALBZAUBERWIRKER = {
    1:  {},
    2:  {1: 2},
    3:  {1: 3},
    4:  {1: 3},
    5:  {1: 4, 2: 2},
    6:  {1: 4, 2: 2},
    7:  {1: 4, 2: 3},
    8:  {1: 4, 2: 3},
    9:  {1: 4, 2: 3, 3: 2},
    10: {1: 4, 2: 3, 3: 2},
    11: {1: 4, 2: 3, 3: 3},
    12: {1: 4, 2: 3, 3: 3},
    13: {1: 4, 2: 3, 3: 3, 4: 1},
    14: {1: 4, 2: 3, 3: 3, 4: 1},
    15: {1: 4, 2: 3, 3: 3, 4: 2},
    16: {1: 4, 2: 3, 3: 3, 4: 2},
    17: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    18: {1: 4, 2: 3, 3: 3, 4: 3, 5: 1},
    19: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
    20: {1: 4, 2: 3, 3: 3, 4: 3, 5: 2},
}

# Hexenmeister: Paktmagie (alle Slots gleichen Grads)
PAKTMAGIE = {
    1:  {'anzahl': 1, 'grad': 1},
    2:  {'anzahl': 2, 'grad': 1},
    3:  {'anzahl': 2, 'grad': 2},
    4:  {'anzahl': 2, 'grad': 2},
    5:  {'anzahl': 2, 'grad': 3},
    6:  {'anzahl': 2, 'grad': 3},
    7:  {'anzahl': 2, 'grad': 4},
    8:  {'anzahl': 2, 'grad': 4},
    9:  {'anzahl': 2, 'grad': 5},
    10: {'anzahl': 2, 'grad': 5},
    11: {'anzahl': 3, 'grad': 5},
    12: {'anzahl': 3, 'grad': 5},
    13: {'anzahl': 3, 'grad': 5},
    14: {'anzahl': 3, 'grad': 5},
    15: {'anzahl': 3, 'grad': 5},
    16: {'anzahl': 3, 'grad': 5},
    17: {'anzahl': 4, 'grad': 5},
    18: {'anzahl': 4, 'grad': 5},
    19: {'anzahl': 4, 'grad': 5},
    20: {'anzahl': 4, 'grad': 5},
}

ZAUBERPLATZ_TABELLE = {
    'vollzauberwirker': VOLLZAUBERWIRKER,
    'halbzauberwirker': HALBZAUBERWIRKER,
    'paktmagie': PAKTMAGIE,
}
