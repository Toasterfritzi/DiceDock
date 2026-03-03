"""Remaining classes: Mönch, Paladin, Waldläufer, Schurke, Zauberer, Hexenmeister, Magier."""

KLASSEN_DATEN_TEIL2 = {
    'Mönch': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Stärke', 'Geschicklichkeit'],
        'ruestungen': [],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': ['Akrobatik', 'Athletik', 'Geschichte', 'Motiv erkennen', 'Religion', 'Heimlichkeit'],
        'zauberattribut': None, 'zaubertyp': None,
        'features': {
            1: [
                {'name': 'Kampfkünste', 'beschreibung': 'Kampfkunst-Würfel (W6). Nutze Geschicklichkeit statt Stärke. Bonusaktion: Unbewaffneter Schlag.'},
                {'name': 'Rüstungslose Verteidigung', 'beschreibung': 'RK = 10 + Geschicklichkeitsmod. + Weisheitsmod.'},
            ],
            2: [
                {'name': 'Fokus', 'beschreibung': 'Fokuspunkte (= Stufe). Geduldige Verteidigung (BA Ausweichen), Windschritt (BA Rückzug/Spurt), Stakkato der Schläge (2 BA-Schläge).'},
                {'name': 'Rüstungslose Bewegung', 'beschreibung': '+3m Bewegungsrate (ohne Rüstung).'},
            ],
            3: [
                {'name': 'Mönchs-Unterklasse', 'beschreibung': 'Wähle eine Tradition (Unterklasse).'},
                {'name': 'Geschosse abwehren', 'beschreibung': 'Reaktion: Reduziere Schaden von Fernkampfangriffen.'},
            ],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [
                {'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion.'},
                {'name': 'Betäubender Schlag', 'beschreibung': 'Nutze Fokuspunkt, um Gegner zu betäuben (KON-RW).'},
            ],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            10: [{'name': 'Reinheit des Körpers', 'beschreibung': 'Immun gegen Gift und Krankheit.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            14: [{'name': 'Diamantene Seele', 'beschreibung': 'Übung in allen Rettungswürfen.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Offene Hand': {
                3: [{'name': 'Technik der Offenen Hand', 'beschreibung': 'Stakkato der Schläge: Umwerfen, Wegstoßen oder Reaktion des Gegners unterbinden.'}],
                6: [{'name': 'Ganzheit des Körpers', 'beschreibung': 'Heile dich selbst (3× Stufe TP). 1/LR.'}],
            },
            'Elemente': {
                3: [{'name': 'Elementare Reichweite', 'beschreibung': 'Angriffe auf Distanz (4,5m). Wähle Schadenstyp (Säure, Kälte, Feuer, Blitz, Donner).'}],
                6: [{'name': 'Elementarer Ausbruch', 'beschreibung': 'Flächenschaden im Nahbereich.'}],
            },
            'Gnade': {
                3: [{'name': 'Hände der Heilung', 'beschreibung': 'Heile Verbündete mit Fokuspunkten.'},
                 {'name': 'Hände des Leids', 'beschreibung': 'Füge Nekrotischen Schaden mit Fokuspunkten zu.'}],
                6: [{'name': 'Arzt-Berührung', 'beschreibung': 'Heile Zustände (Vergiftet, Betäubt etc.).'}],
            },
            'Schatten': {
                3: [{'name': 'Schattengestalt', 'beschreibung': 'Dunkelsicht 18m. Zauber: Dunkelheit, Stille etc. mit Fokuspunkten.'}],
                6: [{'name': 'Schattenschritt', 'beschreibung': 'Teleportiere 18m von Schatten zu Schatten als Bonusaktion.'}],
            },
        },
    },

    'Paladin': {
        'trefferwuerfel': 'd10',
        'rettungswuerfe': ['Weisheit', 'Charisma'],
        'ruestungen': ['Alle Rüstungen', 'Schilde'],
        'waffen': ['Einfache Waffen', 'Kriegswaffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': ['Athletik', 'Motiv erkennen', 'Einschüchtern', 'Überzeugen', 'Religion', 'Heilkunde'],
        'zauberattribut': 'charisma', 'zaubertyp': 'halbzauberwirker',
        'features': {
            1: [
                {'name': 'Handauflegen', 'beschreibung': 'Heile TP aus einem Pool (5 × Stufe). Aktion.'},
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Charisma. Fokus: Heiliges Symbol.'},
                {'name': 'Waffenmeisterung', 'beschreibung': 'Beherrsche 2 Waffenarten.'},
            ],
            2: [
                {'name': 'Göttliches Niederstrecken', 'beschreibung': 'Nutze Zauberplatz für +2W8 Strahlenschaden (+1W8 pro höherem Grad).'},
                {'name': 'Kampfstil', 'beschreibung': 'Wähle ein Kampfstil-Talent.'},
            ],
            3: [
                {'name': 'Paladin-Unterklasse', 'beschreibung': 'Wähle einen Eid (Unterklasse).'},
                {'name': 'Untote vertreiben', 'beschreibung': 'Kanalisiere Göttliche Macht, um Untote zu vertreiben.'},
            ],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion.'}],
            6: [{'name': 'Aura des Schutzes', 'beschreibung': '+Charismamod. auf Rettungswürfe für dich und Gefährten (3m Radius).'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Eid der Hingabe': {
                3: [{'name': 'Heilige Waffe', 'beschreibung': 'Kanalisiere Göttliche Macht: +Charismamod. auf Trefferwurf für 1 Minute.'}],
                6: [{'name': 'Aura der Hingabe', 'beschreibung': 'Du und Gefährten im 3m-Radius sind immun gegen Furcht.'}],
            },
            'Eid der Rache': {
                3: [{'name': 'Gelöbnis der Feindschaft', 'beschreibung': 'Vorteil auf Angriffe gegen ein gewähltes Ziel.'}],
                6: [{'name': 'Unnachgiebige Verfolgung', 'beschreibung': 'Bonus-Bewegung wenn Ziel sich bewegt.'}],
            },
            'Eid der Uralten': {
                3: [{'name': 'Zorn der Natur', 'beschreibung': 'Kanalisiere Göttliche Macht für Naturzauber.'}],
                6: [{'name': 'Aura der Behütung', 'beschreibung': 'Resistenz gegen Zauberschaden für dich und Gefährten (3m).'}],
            },
            'Eid des Ruhms': {
                3: [{'name': 'Erlesener Athlet', 'beschreibung': 'Bonusaktion: Vorteil auf Athletik/Akrobatik + Bonus auf Sprungweite.'}],
                6: [{'name': 'Aura der Schnelligkeit', 'beschreibung': '+3m Bewegungsrate für dich und Gefährten (3m Radius).'}],
            },
        },
    },

    'Waldläufer': {
        'trefferwuerfel': 'd10',
        'rettungswuerfe': ['Stärke', 'Geschicklichkeit'],
        'ruestungen': ['Leichte Rüstung', 'Mittelschwere Rüstung', 'Schilde'],
        'waffen': ['Einfache Waffen', 'Kriegswaffen'],
        'fertigkeiten_anzahl': 3,
        'fertigkeiten_auswahl': ['Athletik', 'Heimlichkeit', 'Mit Tieren umgehen', 'Motiv erkennen', 'Nachforschungen', 'Naturkunde', 'Überlebenskunst', 'Wahrnehmung'],
        'zauberattribut': 'wisdom', 'zaubertyp': 'halbzauberwirker',
        'features': {
            1: [
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Weisheit. Fokus: Druidischer Fokus.'},
                {'name': 'Erzfeind', 'beschreibung': 'Zeichen des Jägers stets vorbereitet. Übungsbonus-mal kostenlos wirken.'},
                {'name': 'Waffenmeisterung', 'beschreibung': 'Beherrsche 2 Waffenarten.'},
            ],
            2: [
                {'name': 'Geschickte Erkundung', 'beschreibung': 'Expertise in 1 Fertigkeit + Zusatzsprachen.'},
                {'name': 'Kampfstil', 'beschreibung': 'Wähle ein Kampfstil-Talent.'},
            ],
            3: [{'name': 'Waldläufer-Unterklasse', 'beschreibung': 'Wähle eine Spezialisierung (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Zusätzlicher Angriff', 'beschreibung': 'Zwei Angriffe pro Angriffsaktion.'}],
            6: [{'name': 'Vagabund', 'beschreibung': '+3m Bewegungsrate + Kletter-/Schwimmrate.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            14: [{'name': 'Naturschleier', 'beschreibung': 'Bonusaktion: Unsichtbarkeit bis Ende deines nächsten Zugs.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Jäger': {
                3: [{'name': 'Beute des Jägers', 'beschreibung': 'Wähle: Hordenbrecher (Nachbar-Schaden), Koloss-Schlächter (+1W8 gegen Verwundete) oder Riesentöter (+1W8 gegen Große+).'}],
                6: [{'name': 'Defensive Taktiken', 'beschreibung': 'Wähle: Flucht vor der Horde, Vielseitige Verteidigung oder Stahlerner Wille.'}],
            },
            'Herr der Tiere': {
                3: [{'name': 'Urbegleiter', 'beschreibung': 'Beschwöre ein Tier des Landes, der Lüfte oder des Meeres als Begleiter.'}],
                7: [{'name': 'Außergewöhnliches Training', 'beschreibung': 'Dein Begleiter kann Ausweichen als Bonusaktion nutzen.'}],
            },
            'Düsterpirscher': {
                3: [
                    {'name': 'Furchterregender Lauerjäger', 'beschreibung': 'Bonus auf Initiative (WEI-Mod). Zusatzschaden und Extra-Bewegung im 1. Zug.'},
                    {'name': 'Schattensicht', 'beschreibung': 'Dunkelsicht 18m.'},
                ],
                7: [{'name': 'Eiserner Verstand', 'beschreibung': 'Zusätzlicher Rettungswurf bei Furcht.'}],
            },
            'Feenwanderer': {
                3: [
                    {'name': 'Außerweltlicher Glanz', 'beschreibung': 'Addiere Weisheitsmod. auf Charisma-Würfe.'},
                    {'name': 'Grässliche Schläge', 'beschreibung': 'Extra Psychischer Schaden (1W4) bei Waffentreffern.'},
                ],
                7: [{'name': 'Bezaubernder Blick', 'beschreibung': 'Bezaubere Gegner als Reaktion.'}],
            },
        },
    },

    'Schurke': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Geschicklichkeit', 'Intelligenz'],
        'ruestungen': ['Leichte Rüstung'],
        'waffen': ['Einfache Waffen', 'Kriegswaffen mit Finesse'],
        'fertigkeiten_anzahl': 4,
        'fertigkeiten_auswahl': ['Akrobatik', 'Athletik', 'Täuschung', 'Motiv erkennen', 'Einschüchtern', 'Nachforschungen', 'Wahrnehmung', 'Auftreten', 'Überzeugen', 'Heimlichkeit', 'Fingerfertigkeit'],
        'zauberattribut': None, 'zaubertyp': None,
        'features': {
            1: [
                {'name': 'Hinterhältiger Angriff', 'beschreibung': '+1W6 Schaden bei Vorteil oder Verbündetem am Ziel. Skaliert bis +10W6.'},
                {'name': 'Diebessprache', 'beschreibung': 'Geheimsprache der Diebe.'},
                {'name': 'Expertisen', 'beschreibung': 'Wähle 2 Fertigkeiten für doppelten Übungsbonus.'},
                {'name': 'Waffenmeisterung', 'beschreibung': 'Beherrsche 2 Waffenarten.'},
            ],
            2: [{'name': 'Listige Aktion', 'beschreibung': 'Bonusaktion für Spurt, Rückzug oder Verstecken.'}],
            3: [{'name': 'Schurken-Unterklasse', 'beschreibung': 'Wähle eine Spezialisierung (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Unheimliches Ausweichen', 'beschreibung': 'Reaktion: Halbiere Schaden eines Angriffs.'}],
            7: [{'name': 'Entrinnen', 'beschreibung': 'Kein Schaden bei bestandenem GES-RW, halber bei Misserfolg.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            10: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            11: [{'name': 'Zuverlässiges Talent', 'beschreibung': 'Würfel von 9 oder niedriger zählen als 10 bei geübten Fertigkeiten.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Dieb': {
                3: [
                    {'name': 'Flinke Finger', 'beschreibung': 'Bonusaktion für Fingerfertigkeit oder Gegenstand nutzen.'},
                    {'name': 'Kletteraffe', 'beschreibung': 'Kletterrate = Bewegungsrate.'},
                ],
                6: [{'name': 'Heimlicher Angriff', 'beschreibung': 'Vorteil auf Angriffe gegen Gegner die dich nicht bemerken.'}],
            },
            'Assassine': {
                3: [
                    {'name': 'Meuchelmörder', 'beschreibung': 'Vorteil gegen Gegner, die noch nicht dran waren. Automatischer Krit bei Überraschung.'},
                    {'name': 'Tödlicher Schlag', 'beschreibung': 'Extra Schaden bei Überraschungsangriffen.'},
                ],
                6: [{'name': 'Infiltrationsexperte', 'beschreibung': 'Erstelle falsche Identitäten.'}],
            },
            'Arkaner Betrüger': {
                3: [
                    {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Intelligenz.'},
                    {'name': 'Magierhandstreich', 'beschreibung': 'Unsichtbare Magierhand für Taschendiebstahl etc.'},
                ],
                6: [{'name': 'Vielseitiger Betrüger', 'beschreibung': 'Vorteil auf Angriffe nach Zauberwirken.'}],
            },
            'Seelenmesser': {
                3: [
                    {'name': 'Psionische Kraft', 'beschreibung': 'Psionische Energiewürfel für Kommunikation und Fertigkeit.'},
                    {'name': 'Psychische Klingen', 'beschreibung': 'Manifestiere Klingen aus psychischer Energie als Waffen.'},
                ],
                6: [{'name': 'Geist des Seelenmessers', 'beschreibung': 'Teleportation nach Angriff.'}],
            },
        },
    },

    'Zauberer': {
        'trefferwuerfel': 'd6',
        'rettungswuerfe': ['Konstitution', 'Charisma'],
        'ruestungen': [],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': ['Arkane Kunde', 'Täuschung', 'Motiv erkennen', 'Einschüchtern', 'Überzeugen', 'Religion'],
        'zauberattribut': 'charisma', 'zaubertyp': 'vollzauberwirker',
        'features': {
            1: [
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Charisma. Fokus: Arkaner Fokus.'},
                {'name': 'Angeborener Zauber', 'beschreibung': 'Bonusaktion: Erhöhe Zauber-SG und Trefferchance für 1 Minute. Übungsbonus Nutzungen pro LR.'},
            ],
            2: [
                {'name': 'Metamagie', 'beschreibung': 'Wähle 2 Optionen (z.B. Beschleunigter Zauber, Distanz-Zauber, Sorgfältiger Zauber).'},
                {'name': 'Magie anzapfen', 'beschreibung': 'Zauberpunkte (= Stufe). Nutze für Metamagie oder Zauberplätze erstellen.'},
            ],
            3: [{'name': 'Zauberer-Unterklasse', 'beschreibung': 'Wähle einen Ursprung (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            5: [{'name': 'Zauberkraft-Erholung', 'beschreibung': 'Regeneriere Zauberpunkte bei Kurzer Rast.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Drachenblut-Linie': {
                3: [{'name': 'Drachen-Resistenz', 'beschreibung': 'RK = 13+GES-Mod (ohne Rüstung). Extra-TP (+1 pro Stufe). Wähle Drachenfarbe für Schadenstyp.'}],
                6: [{'name': 'Elementare Affinität', 'beschreibung': 'Addiere CHA-Mod auf Schaden des Drachentyps. Resistenz gegen Drachentyp.'}],
            },
            'Wilde Magie': {
                3: [
                    {'name': 'Woge Wilder Magie', 'beschreibung': 'Zufallseffekte beim Zaubern (Wilde-Magie-Tabelle).'},
                    {'name': 'Gezeiten des Chaos', 'beschreibung': 'Erzwinge Vorteil oder Nachteil auf einen Wurf.'},
                ],
                6: [{'name': 'Genesung der Magie', 'beschreibung': 'Erhalte Zauberpunkte bei Wilder Magie zurück.'}],
            },
            'Aberrante Übereinkunft': {
                3: [{'name': 'Psionisches Zaubern', 'beschreibung': 'Wirke bestimmte Zauber ohne verbale/somatische Komponenten.'}],
                6: [{'name': 'Psychische Abwehr', 'beschreibung': 'Resistenz gegen psychischen Schaden. Vorteil gegen Bezauberung/Furcht.'}],
            },
            'Uhrwerk-Spross': {
                3: [{'name': 'Ordnung regenerieren', 'beschreibung': 'Schilde aus kosmischer Ordnung. Reduziere Schaden für dich oder Verbündete.'}],
                6: [{'name': 'Bastion der Ordnung', 'beschreibung': 'Schütze Verbündete mit Ordnungsmagie.'}],
            },
        },
    },

    'Hexenmeister': {
        'trefferwuerfel': 'd8',
        'rettungswuerfe': ['Weisheit', 'Charisma'],
        'ruestungen': ['Leichte Rüstung'],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': ['Arkane Kunde', 'Täuschung', 'Geschichte', 'Einschüchtern', 'Motiv erkennen', 'Naturkunde', 'Religion'],
        'zauberattribut': 'charisma', 'zaubertyp': 'paktmagie',
        'features': {
            1: [
                {'name': 'Paktmagie', 'beschreibung': 'Zauberattribut: Charisma. Zauberplätze regenerieren bei Kurzer Rast.'},
                {'name': 'Geheimnisvolle Anrufungen', 'beschreibung': 'Wähle 2 Anrufungen (z.B. Quälender Stoß: +CHA auf Eldritch Blast).'},
                {'name': 'Paktgabe', 'beschreibung': 'Wähle: Klinge (Waffe beschwören), Kette (Vertrauter) oder Buch (Zusatz-Zaubertricks/Rituale).'},
            ],
            3: [{'name': 'Hexenmeister-Unterklasse', 'beschreibung': 'Wähle einen Schutzherrn (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            11: [{'name': 'Mystisches Arkanum', 'beschreibung': 'Wähle einen Zauber 6. Grads; 1× pro LR ohne Platz wirken.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Unhold': {
                3: [{'name': 'Segen des Dunklen', 'beschreibung': 'Temporäre TP bei Kill (CHA-Mod + Stufe).'}],
                6: [{'name': 'Eigenes Glück erzwingen', 'beschreibung': 'Addiere W10 auf Fertigkeitswurf oder Rettungswurf. 1/KR.'}],
            },
            'Großer Alter': {
                3: [{'name': 'Erwachte Telepathie', 'beschreibung': 'Telepathische Kommunikation (Reichweite = 1,5× Stufe m).'}],
                6: [{'name': 'Psychischer Schutz', 'beschreibung': 'Resistenz gegen psychischen Schaden.'}],
            },
            'Erzfee': {
                3: [{'name': 'Nebeliger Entzug', 'beschreibung': 'Bonusaktion: Teleportation (18m) nach Zauberwirken.'}],
                6: [{'name': 'Betörende Abwehr', 'beschreibung': 'Immun gegen Bezauberung. Bezauberer wird stattdessen bezaubert.'}],
            },
            'Celestischer': {
                3: [{'name': 'Heilendes Licht', 'beschreibung': 'Bonusaktion: Heile Verbündeten (W6en = CHA-Mod + 1). Pool regeneriert bei LR.'}],
                6: [{'name': 'Strahlende Seele', 'beschreibung': 'Resistenz gegen Strahlenschaden. Addiere CHA-Mod auf Strahlungs-/Feuerschaden.'}],
            },
        },
    },

    'Magier': {
        'trefferwuerfel': 'd6',
        'rettungswuerfe': ['Intelligenz', 'Weisheit'],
        'ruestungen': [],
        'waffen': ['Einfache Waffen'],
        'fertigkeiten_anzahl': 2,
        'fertigkeiten_auswahl': ['Arkane Kunde', 'Geschichte', 'Motiv erkennen', 'Naturkunde', 'Religion', 'Heilkunde'],
        'zauberattribut': 'intelligence', 'zaubertyp': 'vollzauberwirker',
        'features': {
            1: [
                {'name': 'Zauberwirken', 'beschreibung': 'Zauberattribut: Intelligenz. Fokus: Arkaner Fokus. Nutzt Zauberbuch.'},
                {'name': 'Arkane Erholung', 'beschreibung': 'Regeneriere Zauberplätze (Summe der Grade = halbe Stufe) bei Kurzer Rast. 1/LR.'},
                {'name': 'Ritualwirken', 'beschreibung': 'Kann Zauber als Rituale wirken, wenn sie im Buch stehen.'},
            ],
            2: [{'name': 'Gelehrter', 'beschreibung': 'Expertise in einer Wissens-Fertigkeit (z.B. Arkane Kunde).'}],
            3: [{'name': 'Magier-Unterklasse', 'beschreibung': 'Wähle eine Schule (Unterklasse).'}],
            4: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            8: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            12: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            16: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            18: [{'name': 'Zaubermeisterschaft', 'beschreibung': 'Wähle einen Zauber 1. und 2. Grads; beliebig oft ohne Platz wirken.'}],
            19: [{'name': 'Attributsverbesserung', 'beschreibung': '+2 auf ein Attribut, +1 auf zwei Attribute oder ein Talent.'}],
            20: [{'name': 'Epische Gabe', 'beschreibung': 'Wähle ein Talent der Stufe 20.'}],
        },
        'unterklassen': {
            'Schule der Hervorrufung': {
                3: [{'name': 'Zauber formen', 'beschreibung': 'Schütze Gefährten vor dem Schaden deiner Flächenzauber.'}],
                6: [{'name': 'Mächtige Zaubertricks', 'beschreibung': 'Halber Schaden bei Zaubertricks auch bei bestandenem Rettungswurf.'}],
            },
            'Schule der Abjuration': {
                3: [{'name': 'Arkane Station', 'beschreibung': 'Magischer Schild, der Schaden absorbiert (2× Magier-Stufe + INT-Mod TP).'}],
                6: [{'name': 'Projektion der Station', 'beschreibung': 'Schütze Verbündete mit deiner Arkanen Station.'}],
            },
            'Schule der Erkenntnis': {
                3: [{'name': 'Voraussicht', 'beschreibung': 'Würfle 2W20 nach LR. Ersetze später eigene oder gegnerische Würfe damit.'}],
                6: [{'name': 'Experten-Seher', 'beschreibung': 'Erkenntniszauber kosten weniger Ressourcen.'}],
            },
            'Schule der Illusion': {
                3: [{'name': 'Verbesserte Illusion', 'beschreibung': 'Illusionszauber werden mächtiger und überzeugender.'}],
                6: [{'name': 'Formbare Illusionen', 'beschreibung': 'Ändere aktive Illusionszauber als Aktion.'}],
            },
        },
    },
}
