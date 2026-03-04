"""Spezies (Völker) – D&D 2024 deutsche Spielregeln."""

SPEZIES_DATEN = {
    'Aasimar': {
        'groesse': 'Mittel oder Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Himmlische Resistenz', 'beschreibung': 'Resistenz gegen Nekrotischen und Strahlenschaden.'},
            {'name': 'Heilende Hände', 'beschreibung': 'Aktion: Heile (Übungsbonus × W4) TP. 1 Nutzung pro Langer Rast.'},
            {'name': 'Lichtbringer', 'beschreibung': 'Zaubertrick: Licht.'},
            {'name': 'Himmlische Offenbarung', 'beschreibung': 'Ab Stufe 3: Bonusaktion Transformation (Flügel, Strahlen o.ä.) für 1 Minute.'},
        ],
        'tp_bonus': 0,
    },
    'Drachenblütler': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Drachensippe', 'beschreibung': 'Wähle Elementtyp (Feuer, Kälte, Blitz, Gift, Säure) für Odemwaffe und Resistenz.'},
            {'name': 'Odemwaffe', 'beschreibung': 'Aktion (ersetzt einen Angriff). 4,5m Kegel oder 9m Linie. Schaden skaliert mit Stufe. Übungsbonus Nutzungen pro Langer Rast.'},
            {'name': 'Resistenz', 'beschreibung': 'Resistenz gegen den gewählten Elementtyp.'},
            {'name': 'Flug', 'beschreibung': 'Ab Stufe 5: Fliegen für 10 Minuten. 1 Nutzung pro Langer Rast.'},
        ],
        'tp_bonus': 0,
    },
    'Elf': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Feenblut', 'beschreibung': 'Vorteil auf Rettungswürfe gegen Bezauberung. Immun gegen magischen Schlaf.'},
            {'name': 'Trance', 'beschreibung': '4 Stunden Schlaf reichen für eine Lange Rast.'},
            {'name': 'Geschärfte Sinne', 'beschreibung': 'Übung in Wahrnehmung.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Drow': [
                {'name': 'Drow-Magie', 'beschreibung': 'Zaubertrick: Tanzende Lichter. Ab Stufe 3: Dunkelheit (1/LR).'},
            ],
            'Hochelf': [
                {'name': 'Magier-Zaubertrick', 'beschreibung': 'Wähle einen Magier-Zaubertrick. Wechselbar nach Langer Rast.'},
            ],
            'Waldelf': [
                {'name': 'Schnelle Füße', 'beschreibung': 'Bewegungsrate 10,5m (statt 9m).'},
                {'name': 'Waldelf-Magie', 'beschreibung': 'Zaubertrick: Langstricher. Ab Stufe 5: Spurlos gehen (1/LR).'},
            ],
        },
    },
    'Gnom': {
        'groesse': 'Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Gnom-Schlauheit', 'beschreibung': 'Vorteil auf INT-, WIS- und CHA-Rettungswürfe gegen Magie.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Felsgnom': [
                {'name': 'Werkzeugbau-Begabung', 'beschreibung': 'Bastele kleine Gegenstände (Feuerstein, Musikdose etc.).'},
            ],
            'Waldgnom': [
                {'name': 'Natürlicher Illusionist', 'beschreibung': 'Zaubertrick: Geringe Illusion. Spreche mit kleinen Tieren.'},
            ],
        },
    },
    'Goliath': {
        'groesse': 'Mittel', 'geschwindigkeit': 10.5,
        'merkmale': [
            {'name': 'Riesen-Erbe', 'beschreibung': 'Wähle Vorfahre (Steingigant, Feuergigant etc.) für verschiedene Boni. Übungsbonus Nutzungen pro Langer Rast.'},
            {'name': 'Große Statur', 'beschreibung': 'Zählt als eine Kategorie größer für Tragekapazität.'},
            {'name': 'Steinernes Fell', 'beschreibung': 'Reaktion: Reduziere erlittenen Schaden um 1W12 + Konstitutionsmod.'},
        ],
        'tp_bonus': 0,
    },
    'Halbling': {
        'groesse': 'Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Glückspilz', 'beschreibung': 'Bei einer 1 auf dem W20: Wiederhole den Wurf (muss neues Ergebnis nehmen).'},
            {'name': 'Mutig', 'beschreibung': 'Vorteil auf Rettungswürfe gegen Furcht.'},
            {'name': 'Halbling-Gewandtheit', 'beschreibung': 'Kann durch Felder von größeren Kreaturen ziehen.'},
            {'name': 'Natürliche Verborgenheit', 'beschreibung': 'Kann sich hinter größeren Kreaturen verstecken.'},
        ],
        'tp_bonus': 0,
    },
    'Mensch': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Vielseitig', 'beschreibung': 'Erhalte ein zusätzliches Herkunftstalent.'},
            {'name': 'Geschickt', 'beschreibung': 'Übung in einer zusätzlichen Fertigkeit deiner Wahl.'},
            {'name': 'Inspirierende Gegenwart', 'beschreibung': 'Erhalte Inspiration nach jeder Langen Rast.'},
        ],
        'tp_bonus': 0,
    },
    'Ork': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Adrenalinrausch', 'beschreibung': 'Bonusaktion: Spurt + temporäre TP erhalten. Übungsbonus Nutzungen pro Langer Rast.'},
            {'name': 'Standhaftigkeit', 'beschreibung': 'Bei 0 TP: Einmalig auf 1 TP bleiben. 1 Nutzung pro Langer Rast.'},
            {'name': 'Große Statur', 'beschreibung': 'Zählt als eine Kategorie größer für Tragekapazität.'},
        ],
        'tp_bonus': 0,
    },
    'Tiefling': {
        'groesse': 'Mittel oder Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Andauernde Resistenz', 'beschreibung': 'Resistenz gegen Feuerschaden.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Infernal': [
                {'name': 'Infernale Magie', 'beschreibung': 'Zaubertrick: Feuerbolzen. Ab Stufe 3: Höllischer Tadel (1/LR).'},
            ],
            'Abyssal': [
                {'name': 'Abyssale Magie', 'beschreibung': 'Zaubertrick: Gift versprühen. Ab Stufe 3: Strahl des Siechtums (1/LR).'},
            ],
            'Chthonisch': [
                {'name': 'Chthonische Magie', 'beschreibung': 'Zaubertrick: Eisige Hand. Ab Stufe 3: Falsches Leben (1/LR).'},
            ],
        },
    },
    'Zwerg': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '36m Dunkelsicht (verbessert in 2024!).'},
            {'name': 'Zwergen-Zähigkeit', 'beschreibung': '+1 TP pro Stufe.'},
            {'name': 'Zwergen-Resistenz', 'beschreibung': 'Vorteil auf Rettungswürfe gegen Gift. Resistenz gegen Giftschaden.'},
            {'name': 'Steingespür', 'beschreibung': 'Bonusaktion: Erschütterungssinn auf Steinböden für 10 Minuten.'},
        ],
        'tp_bonus': 1,  # +1 pro Stufe
    },
}
