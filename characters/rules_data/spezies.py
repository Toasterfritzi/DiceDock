"""Spezies (Völker) – D&D 2024 deutsche Spielregeln."""

SPEZIES_DATEN = {
    'Aasimar': {
        'groesse': 'Mittel oder Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Celestische Resistenz', 'beschreibung': 'Resistenz gegen gleißenden und nekrotischen Schaden.'},
            {'name': 'Heilende Hände', 'beschreibung': 'Magische Aktion: Berühre eine Kreatur und heile (Übungsbonus × W4) TP. 1 Nutzung pro Langer Rast.'},
            {'name': 'Lichtbringer', 'beschreibung': 'Zaubertrick: Licht. Zauberattribut: Charisma.'},
            {'name': 'Celestische Offenbarung', 'beschreibung': 'Ab Stufe 3: Bonusaktion Transformation für 1 Minute (1/LR). Einmal pro Zug zusätzlicher Schaden = Übungsbonus. Du wählst die Art der Offenbarung.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Himmlische Flügel': [
                {'name': 'Himmlische Flügel', 'beschreibung': 'Während der Offenbarung erhältst du eine Flugbewegungsrate gleich deiner normalen Bewegungsrate.'},
            ],
            'Inneres Strahlen': [
                {'name': 'Inneres Strahlen', 'beschreibung': 'Während der Offenbarung strahlst du helles Licht aus und verursachst am Ende deines Zuges gleißenden Schaden bei nahen Feinden.'},
            ],
            'Nekrotische Spukgestalt': [
                {'name': 'Nekrotische Spukgestalt', 'beschreibung': 'Während der Offenbarung können Gegner, die dich sehen, verängstigt werden.'},
            ],
        },
    },
    'Drachenblütler': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Odemwaffe', 'beschreibung': 'Ersetzt einen Angriff. 4,5m Kegel oder 9m Linie (wähle bei jedem Einsatz). 1W10 Schaden (skaliert: 2W10 ab 5., 3W10 ab 11., 4W10 ab 17. Stufe). GES-Rettungswurf (SG 8 + KON-Mod + Übungsbonus). Übungsbonus Nutzungen pro Langer Rast.'},
            {'name': 'Drakonischer Flug', 'beschreibung': 'Ab Stufe 5: Bonusaktion, geisterhafte Flügel für 10 Minuten. Flugbewegungsrate = Bewegungsrate. 1 Nutzung pro Langer Rast.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Schwarzer Drache': [{'name': 'Drakonische Abstammung (Schwarz)', 'beschreibung': 'Odemwaffe richtet Säureschaden an. Resistenz gegen Säureschaden.'}],
            'Blauer Drache': [{'name': 'Drakonische Abstammung (Blau)', 'beschreibung': 'Odemwaffe richtet Blitzschaden an. Resistenz gegen Blitzschaden.'}],
            'Messingdrache': [{'name': 'Drakonische Abstammung (Messing)', 'beschreibung': 'Odemwaffe richtet Feuerschaden an. Resistenz gegen Feuerschaden.'}],
            'Bronzedrache': [{'name': 'Drakonische Abstammung (Bronze)', 'beschreibung': 'Odemwaffe richtet Blitzschaden an. Resistenz gegen Blitzschaden.'}],
            'Kupferdrache': [{'name': 'Drakonische Abstammung (Kupfer)', 'beschreibung': 'Odemwaffe richtet Säureschaden an. Resistenz gegen Säureschaden.'}],
            'Golddrache': [{'name': 'Drakonische Abstammung (Gold)', 'beschreibung': 'Odemwaffe richtet Feuerschaden an. Resistenz gegen Feuerschaden.'}],
            'Grüner Drache': [{'name': 'Drakonische Abstammung (Grün)', 'beschreibung': 'Odemwaffe richtet Giftschaden an. Resistenz gegen Giftschaden.'}],
            'Roter Drache': [{'name': 'Drakonische Abstammung (Rot)', 'beschreibung': 'Odemwaffe richtet Feuerschaden an. Resistenz gegen Feuerschaden.'}],
            'Silberdrache': [{'name': 'Drakonische Abstammung (Silber)', 'beschreibung': 'Odemwaffe richtet Kälteschaden an. Resistenz gegen Kälteschaden.'}],
            'Weißer Drache': [{'name': 'Drakonische Abstammung (Weiß)', 'beschreibung': 'Odemwaffe richtet Kälteschaden an. Resistenz gegen Kälteschaden.'}],
        },
    },
    'Elf': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Elfische Abstammung', 'beschreibung': 'Wähle eine Abstammung (Drow, Hochelf, Waldelf) für übernatürliche Fähigkeiten und Zauber.'},
            {'name': 'Feenblut', 'beschreibung': 'Vorteil auf Rettungswürfe gegen Bezauberung.'},
            {'name': 'Scharfe Sinne', 'beschreibung': 'Übung in einer Fertigkeit deiner Wahl: Motiv erkennen, Überlebenskunst oder Wahrnehmung.'},
            {'name': 'Trance', 'beschreibung': '4 Stunden tranceartige Meditation reichen für eine Lange Rast. Du bleibst dabei bei Bewusstsein.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Drow': [
                {'name': 'Drow-Abstammung', 'beschreibung': 'Dunkelsicht auf 36m erhöht. Zaubertrick: Tanzende Lichter. Ab Stufe 3: Feenfeuer (1/LR). Ab Stufe 5: Dunkelheit (1/LR). Zauberattribut: INT, WIS oder CHA (Wahl).'},
            ],
            'Hochelf': [
                {'name': 'Hochelf-Abstammung', 'beschreibung': 'Zaubertrick: Taschenspielerei (wechselbar nach Langer Rast). Ab Stufe 3: Magie entdecken (1/LR). Ab Stufe 5: Nebelschritt (1/LR). Zauberattribut: INT, WIS oder CHA (Wahl).'},
            ],
            'Waldelf': [
                {'name': 'Waldelf-Abstammung', 'beschreibung': 'Bewegungsrate auf 10m erhöht. Zaubertrick: Druidenkunst. Ab Stufe 3: Lange Schritte (1/LR). Ab Stufe 5: Spurloses Gehen (1/LR). Zauberattribut: INT, WIS oder CHA (Wahl).'},
            ],
        },
    },
    'Gnom': {
        'groesse': 'Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Gnomische Abstammung', 'beschreibung': 'Wähle eine Abstammung (Felsengnom oder Waldgnom) für übernatürliche Fähigkeiten.'},
            {'name': 'Gnomische Gerissenheit', 'beschreibung': 'Vorteil auf CHA-, INT- und WIS-Rettungswürfe.'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Felsengnom': [
                {'name': 'Felsengnom-Begabung', 'beschreibung': 'Zaubertricks: Ausbessern und Taschenspielerei. Taschenspielerei kann genutzt werden, um winzige Uhrwerkgeräte (RK 5, 1 TP) zu bauen. Bis zu 3 gleichzeitig, Haltbarkeit 8 Stunden. Zauberattribut: CHA, INT oder WIS (Wahl).'},
            ],
            'Waldgnom': [
                {'name': 'Waldgnom-Begabung', 'beschreibung': 'Zaubertrick: Einfache Illusion. Zauber: Mit Tieren sprechen (stets vorbereitet, Übungsbonus Nutzungen ohne Platz pro LR). Zauberattribut: CHA, INT oder WIS (Wahl).'},
            ],
        },
    },
    'Goliath': {
        'groesse': 'Mittel', 'geschwindigkeit': 10.5,
        'merkmale': [
            {'name': 'Große Gestalt', 'beschreibung': 'Ab Stufe 5: Bonusaktion, Größe wird Groß für 10 Minuten. Vorteil auf Stärkewürfe, +3m Bewegungsrate. 1 Nutzung pro Langer Rast.'},
            {'name': 'Kräftiger Körperbau', 'beschreibung': 'Vorteil auf Attributswürfe zum Beenden von Gepackt. Traglast gilt für nächsthöhere Größenkategorie.'},
            {'name': 'Riesische Abstammung', 'beschreibung': 'Wähle einen Vorzug (Übungsbonus Nutzungen pro LR).'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Frostriese': [{'name': 'Eiseskälte', 'beschreibung': '+1W6 Kälteschaden beim Treffer, Ziel verliert 3m Bewegung.'}],
            'Steinriese': [{'name': 'Felsenfestigkeit', 'beschreibung': 'Reaktion: 1W12+KON-Mod Schadensreduktion, wenn du Schaden nimmst.'}],
            'Feuerriese': [{'name': 'Feuersbrunst', 'beschreibung': '+1W10 Feuerschaden beim Treffer.'}],
            'Hügelriese': [{'name': 'Hügelsturz', 'beschreibung': 'Ziel nach einem Treffer umstoßen (Rettungswurf).'}],
            'Sturmriese': [{'name': 'Sturmdonner', 'beschreibung': 'Reaktion: Füge 1W8 Schall zu, wenn du getroffen wirst.'}],
            'Wolkenriese': [{'name': 'Wolkensprung', 'beschreibung': 'Bonusaktion: Teleportiere dich bis zu 9m weit.'}],
        },
    },
    'Halbling': {
        'groesse': 'Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Halblingsglück', 'beschreibung': 'Bei einer 1 auf dem W20: Wiederhole den Wurf (muss neues Ergebnis nehmen).'},
            {'name': 'Tapferkeit', 'beschreibung': 'Vorteil auf Rettungswürfe gegen Verängstigt.'},
            {'name': 'Halblingsgewandtheit', 'beschreibung': 'Kann sich durch Felder von größeren Kreaturen bewegen (nicht anhalten).'},
            {'name': 'Angeborene Verstohlenheit', 'beschreibung': 'Verstecken-Aktion möglich, wenn nur von einer mindestens eine Kategorie größeren Kreatur verdeckt.'},
        ],
        'tp_bonus': 0,
    },
    'Mensch': {
        'groesse': 'Mittel oder Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Einfallsreich', 'beschreibung': 'Erhalte Heldische Inspiration nach jeder Langen Rast.'},
            {'name': 'Geschickt', 'beschreibung': 'Übung in einer zusätzlichen Fertigkeit deiner Wahl.'},
            {'name': 'Vielseitig', 'beschreibung': 'Erhalte ein Herkunftstalent deiner Wahl (Begabt empfohlen).'},
        ],
        'tp_bonus': 0,
    },
    'Ork': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Adrenalinrausch', 'beschreibung': 'Bonusaktion: Spurt + temporäre TP in Höhe des Übungsbonus. Übungsbonus Nutzungen pro Kurzer oder Langer Rast.'},
            {'name': 'Dunkelsicht', 'beschreibung': '36m Dunkelsicht.'},
            {'name': 'Durchhaltevermögen', 'beschreibung': 'Bei 0 TP: Einmalig auf 1 TP bleiben (nicht bei direktem Tod). 1 Nutzung pro Langer Rast.'},
        ],
        'tp_bonus': 0,
    },
    'Tiefling': {
        'groesse': 'Mittel oder Klein', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Außerweltliche Präsenz', 'beschreibung': 'Zaubertrick: Thaumaturgie. Zauberattribut wie Unholdisches Erbe.'},
            {'name': 'Dunkelsicht', 'beschreibung': '18m Dunkelsicht.'},
            {'name': 'Unholdisches Erbe', 'beschreibung': 'Wähle ein Erbe (Abyssisch, Chthonisch, Infernalisch) für Resistenz und Zauber. Zauberattribut: CHA, INT oder WIS (Wahl).'},
        ],
        'tp_bonus': 0,
        'abstammungen': {
            'Abyssisch': [
                {'name': 'Abyssisches Erbe', 'beschreibung': 'Resistenz gegen Giftschaden. Zaubertrick: Gift versprühen. Ab Stufe 3: Strahl der Übelkeit (1/LR). Ab Stufe 5: Person festhalten (1/LR).'},
            ],
            'Chthonisch': [
                {'name': 'Chthonisches Erbe', 'beschreibung': 'Resistenz gegen nekrotischen Schaden. Zaubertrick: Kalte Hand. Ab Stufe 3: Falsches Leben (1/LR). Ab Stufe 5: Schwächestrahl (1/LR).'},
            ],
            'Infernalisch': [
                {'name': 'Infernalisches Erbe', 'beschreibung': 'Resistenz gegen Feuerschaden. Zaubertrick: Feuerpfeil. Ab Stufe 3: Höllischer Tadel (1/LR). Ab Stufe 5: Dunkelheit (1/LR).'},
            ],
        },
    },
    'Zwerg': {
        'groesse': 'Mittel', 'geschwindigkeit': 9.0,
        'merkmale': [
            {'name': 'Dunkelsicht', 'beschreibung': '36m Dunkelsicht.'},
            {'name': 'Zwergische Zähigkeit', 'beschreibung': '+1 TP pro Stufe.'},
            {'name': 'Zwergische Unverwüstlichkeit', 'beschreibung': 'Resistenz gegen Giftschaden. Vorteil auf Rettungswürfe gegen Vergiftet.'},
            {'name': 'Steingespür', 'beschreibung': 'Bonusaktion: Erschütterungssinn (18m Reichweite) auf Steinoberflächen für 10 Minuten. Übungsbonus Nutzungen pro Langer Rast.'},
        ],
        'tp_bonus': 1,  # +1 pro Stufe
    },
}
