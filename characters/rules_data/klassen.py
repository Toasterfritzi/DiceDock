"""
Klassendaten – D&D 2024 (deutsche Spielregeln).
Jede Klasse enthält: Trefferwürfel, Rettungswürfe, Rüstungen, Waffen,
wählbare Fertigkeiten, Zauberattribut und Features pro Stufe.
"""

# Alle Fertigkeiten für Klassen die beliebig wählen (Barde)
FERTIGKEITEN_ALLE = [
    'Akrobatik', 'Arkane Kunde', 'Athletik', 'Auftreten', 'Einschüchtern',
    'Fingerfertigkeit', 'Geschichte', 'Heilkunde', 'Heimlichkeit',
    'Mit Tieren umgehen', 'Motiv erkennen', 'Nachforschungen', 'Naturkunde',
    'Religion', 'Täuschung', 'Überlebenskunst', 'Überzeugen', 'Wahrnehmung',
]

KLASSEN_DATEN = {
    'Barbar': {
        'trefferwuerfel': 'd12',
        'rettungswuerfe': ['Stärke', 'Konstitution'],
        'ruestungen': ['Leichte Rüstung', 'Mittelschwere Rüstung', 'Schilde'],
        'waffen': ['Einfache Waffen', 'Kriegswaffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': [
            'Athletik', 'Mit Tieren umgehen', 'Einschüchtern',
            'Naturkunde', 'Überlebenskunst', 'Wahrnehmung',
        ],
        'zauberattribut': None,
        'zaubertyp': None,
        'features': {
            1: [
                {'name': 'Kampfrausch', 'beschreibung': 'Bonusaktion. Vorteil auf Stärkewürfe/Rettungswürfe. Schadensbonus (+2). Resistenz gegen Hieb-, Stich-, Wuchtschaden. 2 Nutzungen pro Langer Rast.'},
                {'name': 'Rüstungslose Verteidigung', 'beschreibung': 'RK = 10 + Geschicklichkeitsmod. + Konstitutionsmod. (ohne Rüstung).'},
                {'name': 'Waffenmeisterung', 'beschreibung': 'Beherrsche 2 Waffenarten.'},
            ],
            2: [
                {'name': 'Achtloses Angreifen', 'beschreibung': 'Vorteil auf eigene Nahkampfangriffe, aber Gegner haben auch Vorteil auf dich.'},
                {'name': 'Gefahrensinn', 'beschreibung': 'Vorteil auf Geschicklichkeitsrettungswürfe gegen sichtbare Effekte.'},
            ],
            3: [
                {'name': 'Barbarische Unterklasse', 'beschreibung': 'Wähle einen Pfad (Unterklasse).'},
                {'name': 'Urinstinkt', 'beschreibung': 'Kampfrausch kann für erweiterte Sinne genutzt werden.'},
            ],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [
                {'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion.'},
                {'name': 'Schnelle Bewegung', 'beschreibung': '+3 Meter Bewegungsrate (ohne Schwere Rüstung).'},
            ],
            7: [{'name': 'Instinktives Vorstürmen', 'beschreibung': 'Bewegung bei Kampfrausch-Aktivierung.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            9: [{'name': 'Brutaler Schlag', 'beschreibung': 'Tausche Vorteil gegen Spezialeffekte + Extra-Schaden.'}],
            11: [{'name': 'Unbändiger Zorn', 'beschreibung': 'Bei 0 TP: Rettungswurf (SG 10) um auf 1 TP zu bleiben.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            15: [{'name': 'Anhaltender Zorn', 'beschreibung': 'Kampfrausch endet nur bei Bewusstlosigkeit oder wenn du ihn beendest.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Urgewalt', 'beschreibung': 'Stärke und Konstitution steigen um +4 (Maximum 25).'}],
        },
        'unterklassen': {
            'Berserker': {
                3: [{'name': 'Raserei', 'beschreibung': 'Extra Schaden beim ersten Treffer pro Runde im Kampfrausch.'}],
                6: [{'name': 'Sinnloser Zorn', 'beschreibung': 'Immun gegen Furcht und Bezauberung im Kampfrausch.'}],
                10: [{'name': 'Vergeltung', 'beschreibung': 'Reaktion: Angriff gegen Angreifer.'}],
                14: [{'name': 'Einschüchternde Präsenz', 'beschreibung': 'Schüchtere Gegner ein.'}],
            },
            'Wildes Herz': {
                3: [{'name': 'Tiergeist', 'beschreibung': 'Wähle Bär (Resistenz), Adler (Spurt) oder Wolf (Vorteil für Verbündete) im Kampfrausch.'}],
                6: [{'name': 'Aspekt des Tieres', 'beschreibung': 'Zusätzlicher passiver Bonus durch Tiergeist.'}],
                10: [{'name': 'Geisterwandler', 'beschreibung': 'Wechsle Tiergeist bei Kampfrausch-Aktivierung.'}],
                14: [{'name': 'Totemische Kraft', 'beschreibung': 'Mächtiger Tierbonus.'}],
            },
            'Weltenbaum': {
                3: [{'name': 'Vitalität des Baumes', 'beschreibung': 'Temporäre Trefferpunkte bei Kampfrausch-Aktivierung.'}],
                6: [{'name': 'Äste des Baumes', 'beschreibung': 'Ziehe Gegner zu dir heran.'}],
                10: [{'name': 'Schlagende Wurzeln', 'beschreibung': 'Erhöhte Reichweite im Kampfrausch.'}],
                14: [{'name': 'Reise durch den Baum', 'beschreibung': 'Teleportation über den Weltenbaum.'}],
            },
            'Eiferer': {
                3: [{'name': 'Göttlicher Zorn', 'beschreibung': 'Extra Strahlender oder Nekrotischer Schaden im Kampfrausch.'}],
                6: [{'name': 'Fanatischer Fokus', 'beschreibung': 'Wiederhole einen fehlgeschlagenen Rettungswurf.'}],
                10: [{'name': 'Eifriger Krieger', 'beschreibung': 'Wenn du stirbst: Bleibe im Kampf (0 TP, Kampfrausch hält dich).'}],
                14: [{'name': 'Zorn jenseits des Todes', 'beschreibung': 'Kampfrausch verhindert Tod.'}],
            },
        },
    },

    'Barde': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Geschicklichkeit', 'Charisma'],
        'ruestungen': ['Leichte Rüstung'],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 3,
        'fertigkeiten_auswahl': FERTIGKEITEN_ALLE,  # Barden wählen beliebige 3
        'zauberattribut': 'charisma',
        'zaubertyp': 'vollzauberwirker',
        'features': {
            1: [
                {'name': 'Bardische Inspiration', 'beschreibung': 'Bonusaktion. Gib Verbündetem 1W6. Kann auf Attributswürfe, Angriffe oder Rettungswürfe addiert werden. Anzahl = Charismamodifikator (mind. 1) pro Langer Rast.'},
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Charisma. Fokus: Musikinstrument.'},
            ],
            2: [
                {'name': 'Multitalent', 'beschreibung': 'Halber Übungsbonus auf alle Fertigkeitswürfe ohne Übung.'},
            ],
            3: [
                {'name': 'Bardische Unterklasse', 'beschreibung': 'Wähle eine Schule (Unterklasse).'},
                {'name': 'Expertisen', 'beschreibung': 'Wähle 2 Fertigkeiten für doppelten Übungsbonus.'},
            ],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Quell der Inspiration', 'beschreibung': 'Bardische Inspiration regeneriert bei Kurzer Rast. Würfel wird W8.'}],
            6: [{'name': 'Gegenzauber', 'beschreibung': 'Reaktion. Vorteil gegen Furcht/Bezauberung für dich und Gefährten.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            10: [{'name': 'Magische Entdeckungen', 'beschreibung': 'Wähle 2 Zauber von irgendeiner Zauberliste (Druide, Kleriker, Magier).'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            18: [{'name': 'Überlegene Inspiration', 'beschreibung': 'Bei Kampfbeginn ohne Inspiration: Erhalte 1 zurück.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Schule des Wissens': {
                3: [{'name': 'Schneidende Worte', 'beschreibung': 'Nutze Bardische Inspiration, um gegnerische Würfe zu senken.'}],
                6: [{'name': 'Zusätzliche Magische Entdeckungen', 'beschreibung': 'Wähle 2 weitere Zauber von beliebigen Listen.'}],
            },
            'Schule des Tanzes': {
                3: [{'name': 'Blendende Beinarbeit', 'beschreibung': 'RK = 10 + Geschicklichkeitsmod. + Charismamod. Unbewaffneter Schlag als Bonusaktion.'}],
                6: [{'name': 'Tandem-Beinarbeit', 'beschreibung': 'Bardische Inspiration auf Initiative.'}],
            },
            'Schule des Wagemuts': {
                3: [{'name': 'Kampf-Inspiration', 'beschreibung': 'Bardische Inspiration kann auf Schaden oder Rüstungsklasse addiert werden.'}],
                6: [{'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion. Kann einen Angriff durch einen Zaubertrick ersetzen.'}],
            },
            'Schule des Zauberbanns': {
                3: [{'name': 'Mantel der Inspiration', 'beschreibung': 'Temporäre TP + Bewegung für Gefährten.'}],
                6: [{'name': 'Mantel der Erhabenheit', 'beschreibung': 'Befehl als Bonusaktion ohne Zauberplatz.'}],
            },
        },
    },

    'Kleriker': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Weisheit', 'Charisma'],
        'ruestungen': ['Leichte Rüstung', 'Mittelschwere Rüstung', 'Schilde'],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': [
            'Geschichte', 'Motiv erkennen', 'Heilkunde', 'Überzeugen', 'Religion',
        ],
        'zauberattribut': 'wisdom',
        'zaubertyp': 'vollzauberwirker',
        'features': {
            1: [
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Weisheit. Fokus: Heiliges Symbol.'},
                {'name': 'Göttlicher Orden', 'beschreibung': 'Wähle Beschützer (Schwere Rüstung & Kriegswaffen) oder Thaumaturg (2 Wissen-Fertigkeiten).'},
            ],
            2: [{'name': 'Göttliche Macht kanalisieren', 'beschreibung': '2 Nutzungen. Göttlicher Funke (Heilen/Schaden) oder Untote vertreiben.'}],
            3: [{'name': 'Kleriker-Unterklasse', 'beschreibung': 'Wähle eine Domäne (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Untote versengen', 'beschreibung': 'Vertriebene Untote erleiden zusätzlichen Schaden.'}],
            6: [{'name': 'Gesegnetes Schlagen', 'beschreibung': 'Bonus auf Zauber-Zaubertricks oder Waffenangriffe.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            10: [{'name': 'Göttliche Intervention', 'beschreibung': 'Rufe deine Gottheit um Hilfe an (Spezialeffekt ohne Kosten).'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Domäne des Lebens': {
                3: [{'name': 'Jünger des Lebens', 'beschreibung': 'Heilzauber heilen zusätzliche Trefferpunkte.'}],
                6: [{'name': 'Bewahrung des Lebens', 'beschreibung': 'Kanalisiere Göttliche Macht, um mehrere Verbündete zu heilen.'}],
            },
            'Domäne des Lichts': {
                3: [{'name': 'Schützendes Aufflammen', 'beschreibung': 'Reaktion: Nachteil auf Angriff gegen dich oder Verbündeten.'}],
                6: [{'name': 'Glanz der Morgendämmerung', 'beschreibung': 'Kanalisiere Göttliche Macht für Lichtschaden im Umkreis.'}],
            },
            'Domäne der List': {
                3: [{'name': 'Segen des Listigen', 'beschreibung': 'Zusätzliche Domänen-Zauber.'}],
                6: [{'name': 'Duplikat beschwören', 'beschreibung': 'Kanalisiere Göttliche Macht, um ein Illusions-Duplikat zu erschaffen.'}],
            },
            'Domäne des Krieges': {
                3: [{'name': 'Kriegspriester', 'beschreibung': 'Bonusaktion: Zusätzlicher Waffenangriff.'}],
                6: [{'name': 'Geführter Schlag', 'beschreibung': 'Kanalisiere Göttliche Macht für +10 auf Trefferwurf.'}],
            },
        },
    },

    'Druide': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Intelligenz', 'Weisheit'],
        'ruestungen': ['Leichte Rüstung', 'Mittelschwere Rüstung', 'Schilde'],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': [
            'Arkane Kunde', 'Mit Tieren umgehen', 'Naturkunde',
            'Überlebenskunst', 'Wahrnehmung', 'Religion', 'Heilkunde',
        ],
        'zauberattribut': 'wisdom',
        'zaubertyp': 'vollzauberwirker',
        'features': {
            1: [
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Weisheit. Fokus: Druidischer Fokus.'},
                {'name': 'Druidisch', 'beschreibung': 'Geheimsprache der Druiden.'},
                {'name': 'Tiergestalt', 'beschreibung': 'Bonusaktion: Verwandle dich in ein Tier (NS ¼). Hält Übungsbonus Stunden.'},
            ],
            2: [{'name': 'Wilder Gefährte', 'beschreibung': 'Nutze Tiergestalt, um „Vertrauten finden" zu wirken.'}],
            3: [{'name': 'Druiden-Unterklasse', 'beschreibung': 'Wähle einen Zirkel (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Urschlag', 'beschreibung': 'Schaden in Tierform zählt als magisch.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            10: [{'name': 'Elementarer Zorn', 'beschreibung': 'Füge Kälte-, Feuer- oder Blitzschaden zu Angriffen hinzu.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Zirkel des Landes': {
                3: [{'name': 'Land-Region', 'beschreibung': 'Wähle Region (Arktis, Wüste etc.) für Zusatz-Zauber. Tiergestalt regeneriert Zauberplätze.'}],
                6: [{'name': 'Landschreiter', 'beschreibung': 'Schwieriges Gelände kostet keine zusätzliche Bewegung.'}],
            },
            'Zirkel des Mondes': {
                3: [{'name': 'Kampf-Tiergestalt', 'beschreibung': 'Bonusaktion-Verwandlung. Erhöhte RK. Heilung mit Zauberplätzen.'}],
                6: [{'name': 'Urschlag (Mond)', 'beschreibung': 'Angriffe in Tierform zählen als magisch.'}],
            },
            'Zirkel des Meeres': {
                3: [{'name': 'Zorn des Meeres', 'beschreibung': 'Aura, die Gegner wegstößt und Kälteschaden verursacht.'}],
                6: [{'name': 'Wächter des Meeres', 'beschreibung': 'Schwimmrate und Unterwasseratmung.'}],
            },
            'Zirkel der Sterne': {
                3: [{'name': 'Sternenform', 'beschreibung': 'Wähle Sternbild: Bogenschütze (Fernkampf), Kelch (Heilung) oder Drache (Konzentration).'}],
                6: [{'name': 'Kosmisches Omen', 'beschreibung': 'Reaktion: Beeinflusse Würfe von Verbündeten oder Gegnern.'}],
            },
        },
    },

    'Kämpfer': {
        'trefferwuerfel': 'd10',
        'rettungswuerfe': ['Stärke', 'Konstitution'],
        'ruestungen': ['Alle Rüstungen', 'Schilde'],
        'waffen': ['Einfache Waffen', 'Kriegswaffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': [
            'Akrobatik', 'Athletik', 'Geschichte', 'Motiv erkennen',
            'Einschüchtern', 'Überlebenskunst', 'Wahrnehmung', 'Mit Tieren umgehen',
        ],
        'zauberattribut': None,
        'zaubertyp': None,
        'features': {
            1: [
                {'name': 'Kampfstil', 'beschreibung': 'Wähle ein Kampfstil-Talent (z.B. Bogenschießen, Verteidigung, Duellieren).'},
                {'name': 'Durchschnaufen', 'beschreibung': 'Bonusaktion: Heile 1W10 + Stufe. Übungsbonus Nutzungen pro Kurzer/Langer Rast.'},
                {'name': 'Waffenmeisterung', 'beschreibung': 'Beherrsche 3 Waffenarten gleichzeitig.'},
            ],
            2: [
                {'name': 'Aktionsschub', 'beschreibung': 'Eine zusätzliche Aktion in diesem Zug. 1 Nutzung pro Kurzer/Langer Rast.'},
                {'name': 'Taktischer Verstand', 'beschreibung': 'Nutze Durchschnaufen, um Bonus auf Fertigkeitswürfe zu erhalten.'},
            ],
            3: [{'name': 'Kämpfer-Unterklasse', 'beschreibung': 'Wähle eine Spezialisierung (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion.'}],
            6: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            9: [{'name': 'Unbeugsam', 'beschreibung': 'Wiederhole einen fehlgeschlagenen Rettungswurf mit Bonus = Stufe.'}],
            11: [{'name': 'Zusätzlicher Angriff (2)', 'beschreibung': 'Drei Angriffe pro Angriffsaktion.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            14: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Zusätzlicher Angriff (3)', 'beschreibung': 'Vier Angriffe pro Angriffsaktion.'}],
        },
        'unterklassen': {
            'Champion': {
                3: [{'name': 'Verbesserter Kritischer Treffer', 'beschreibung': 'Kritischer Treffer bei 19-20.'}],
                6: [{'name': 'Bemerkenswerter Athlet', 'beschreibung': 'Wiederholung von Würfen bei Heldentaten.'}],
                10: [{'name': 'Überlegener Kritischer Treffer', 'beschreibung': 'Kritischer Treffer bei 18-20.'}],
                14: [{'name': 'Überlebender', 'beschreibung': 'Regeneriere TP am Anfang deines Zuges.'}],
            },
            'Kampfmeister': {
                3: [{'name': 'Überlegenheitswürfel', 'beschreibung': '4 Überlegenheitswürfel (W8). Manöver: Entwaffnen, Parieren etc.'}],
                6: [{'name': 'Schüler des Krieges', 'beschreibung': 'Zusätzliche Werkzeug- oder Fertigkeitsübung.'}],
                10: [{'name': 'Verbesserte Überlegenheitswürfel', 'beschreibung': 'Überlegenheitswürfel werden W10.'}],
                14: [{'name': 'Unnachgiebig', 'beschreibung': 'Erhalte einen Überlegenheitswürfel bei Initiative zurück.'}],
            },
            'Psi-Krieger': {
                3: [{'name': 'Psionische Kraft', 'beschreibung': 'Psionische Energiewürfel für Schutz, Schaden und Bewegung.'}],
                6: [{'name': 'Telekinetischer Adept', 'beschreibung': 'Verbesserte psionische Fähigkeiten.'}],
                10: [{'name': 'Beschützende Schilde', 'beschreibung': 'Psionischer Schutz für Verbündete.'}],
                14: [{'name': 'Telekinetischer Meister', 'beschreibung': 'Telekinese als Aktion.'}],
            },
            'Mystischer Ritter': {
                3: [{'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Intelligenz. Schule der Bannmagie und Hervorrufung.'}],
                6: [{'name': 'Waffenbindung', 'beschreibung': 'Binde eine Waffe magisch an dich.'}],
                10: [{'name': 'Arkaner Schlag', 'beschreibung': 'Füge Zauberschaden zu Waffenangriffen hinzu.'}],
                14: [{'name': 'Verbesserter Kriegszauber', 'beschreibung': 'Wirke Zauber und greife an.'}],
            },
        },
    },
}

# Merge remaining classes from teil2
from .klassen_teil2 import KLASSEN_DATEN_TEIL2
KLASSEN_DATEN.update(KLASSEN_DATEN_TEIL2)
