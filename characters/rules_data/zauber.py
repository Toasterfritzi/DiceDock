"""
Zauberlisten – D&D 2024 (deutsche Spielregeln).
Jeder Zauber enthält: name, grad, schule, wirkzeit, reichweite, dauer, beschreibung.
Organisiert nach Klassen-Zauberlisten.
"""

# ── Zauberschulen ─────────────────────────────────────────────────────────────
SCHULEN = [
    'Bannmagie', 'Beschwörung', 'Divination', 'Illusion',
    'Nekromantie', 'Verwandlung', 'Verzauberung', 'Hervorrufung',
]

# ── Vollständige Zauberbeschreibungen ─────────────────────────────────────────
ZAUBER = {
    # ── GRAD 0 (Zaubertricks) ─────────────────────────────────────────────────
    'Boshafter Spott': {
        'grad': 0, 'schule': 'Verzauberung',
        'klassen': ['Barde'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Du beleidigst eine Kreatur. Sie muss einen Weisheitsrettungswurf bestehen oder 1W6 psychischen Schaden erleiden und hat Nachteil auf ihren nächsten Angriffswurf. Schaden steigt auf 2W6 (Stufe 5), 3W6 (Stufe 11), 4W6 (Stufe 17).',
    },
    'Dornenpeitsche': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Druide'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': 'Sofort',
        'beschreibung': 'Eine Ranke peitscht auf eine Kreatur. Trefferwurf: 1W6 Stichschaden. Bei Treffer: Ziel 3m zu dir heranziehen. Schaden steigt auf 2W6 (St.5), 3W6 (St.11), 4W6 (St.17).',
    },
    'Druidenkunst': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Druide'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': 'Sofort/1 Stunde',
        'beschreibung': 'Kleine Naturmanipulation: Wetter vorhersagen, Feuer entzünden/löschen, Pflanze sofort blühen lassen, oder Geruch/Ton erschaffen.',
    },
    'Eisige Hand': {
        'grad': 0, 'schule': 'Nekromantie',
        'klassen': ['Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W10 Kälteschaden. Schaden steigt auf 2W10 (St.5), 3W10 (St.11), 4W10 (St.17).',
    },
    'Elementarismus': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Druide', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': 'Sofort/1 Minute',
        'beschreibung': 'Kleine Elementarmanipulation: Feuer-, Wasser-, Erde- oder Lufteffekte. Z.B. Flamme entzünden, Wassertropfen beschwören, Steinbrocken verschieben, Windhauch erzeugen.',
    },
    'Feuerbolzen': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W10 Feuerschaden. Bei Treffer muss das Ziel einen Konstitutionsrettungswurf bestehen oder fängt Feuer (1W4 Feuerschaden zu Beginn seines nächsten Zuges). Schaden steigt mit Stufe.',
    },
    'Flammen erzeugen': {
        'grad': 0, 'schule': 'Beschwörung',
        'klassen': ['Druide'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst/18m (Wurf)', 'dauer': '10 Minuten',
        'beschreibung': 'Hält eine Flamme in der Hand (Licht 3m). Kann als Aktion geworfen werden: Trefferwurf 1W8 Feuerschaden (steigt mit Stufe).',
    },
    'Freunde': {
        'grad': 0, 'schule': 'Verzauberung',
        'klassen': ['Barde', 'Schurke (Arkaner Betrüger)', 'Zauberer', 'Hexenmeister', 'Magier'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Vorteil auf alle Charisma-Würfe gegen eine nicht-feindliche Kreatur. Nach Ablauf merkt die Kreatur, dass du Magie genutzt hast.',
    },
    'Froststrahl': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W8 Kälteschaden. Bei Treffer: Bewegungsrate des Ziels bis Beginn seines nächsten Zuges um 3m reduziert. Schaden steigt mit Stufe.',
    },
    'Geringe Illusion': {
        'grad': 0, 'schule': 'Illusion',
        'klassen': ['Barde', 'Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute',
        'beschreibung': 'Erschaffe ein Geräusch oder ein kleines unbewegliches sichtbares Bild (max. 1,5 Würfel). Aufdeckbar mit Nachforschungen gegen SG.',
    },
    'Heilige Flamme': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Göttliches Licht flammt auf. Ziel muss Geschicklichkeitsrettungswurf bestehen oder 1W8 Strahlenschaden erleiden. Keine Deckung hilft. Schaden steigt mit Stufe.',
    },
    'Klingenschutz': {
        'grad': 0, 'schule': 'Bannmagie',
        'klassen': ['Barde', 'Hexenmeister'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '1 Runde',
        'beschreibung': 'Bis Beginn deines nächsten Zuges: Wenn dich eine Kreatur in 1,5m mit einem Nahkampfangriff trifft, erleidet sie 1W6+CHA-Mod psychischen Schaden (Barde) oder nekrotischen/Kälteschaden (Hexenmeister).',
    },
    'Langstricher': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Druide', 'Waldläufer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '1 Stunde',
        'beschreibung': 'Eine Kreatur die du berührst bewegt sich heute durch unwegsames Gelände ohne Malus und lässt keine Spuren zurück. Schlechte Voraussetzungen (Wasser) hinterlassen keine Spur mehr.',
    },
    'Leitung': {
        'grad': 0, 'schule': 'Divination',
        'klassen': ['Kleriker', 'Druide'],
        'wirkzeit': 'Reaktion (wenn Verbündeter in 3m einen Wurf ablegt)', 'reichweite': '3m', 'dauer': 'Sofort',
        'beschreibung': 'Der Verbündete addiert 1W4 auf seinen soeben abgelegten Attributswurf, Angriffswurf oder Rettungswurf.',
    },
    'Licht': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Kleriker', 'Barde', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '1 Stunde',
        'beschreibung': 'Ein Objekt leuchtet wie eine Fackel (6m helles Licht, 6m Halbdunkel). Wirft auf einer feindlichen Kreatur: Geschicklichkeitsrettungswurf oder geblendet.',
    },
    'Magierhand': {
        'grad': 0, 'schule': 'Beschwörung',
        'klassen': ['Barde', 'Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute',
        'beschreibung': 'Erschaffe eine schwebende Hand (Geistige Kraft 10 Pfund). Sie kann Objekte manipulieren, Behälter öffnen/schließen, Gegenstände halten.',
    },
    'Nachricht': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Barde', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': '1 Runde',
        'beschreibung': 'Flüstere eine Nachricht an eine Kreatur. Nur sie hört sie. Sie kann flüstern und du hörst es zurück.',
    },
    'Resistenz': {
        'grad': 0, 'schule': 'Bannmagie',
        'klassen': ['Kleriker', 'Druide'],
        'wirkzeit': 'Reaktion (wenn Verbündeter in 3m einen RW ablegt)', 'reichweite': '3m', 'dauer': 'Sofort',
        'beschreibung': 'Der Verbündete addiert 1W4 auf seinen soeben abgelegten Rettungswurf.',
    },
    'Säurespritzer': {
        'grad': 0, 'schule': 'Beschwörung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Spritzer Säure: Ein oder mehrere Ziele (max. 2 im 1,5m Abstand) müssen Geschicklichkeitsrettungswurf bestehen oder 1W6 Säureschaden erleiden. Schaden steigt mit Stufe.',
    },
    'Schauerlicher Strahl': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W10 Kraftschaden. Schaden steigt auf 2W10 (St.5), 3W10 (St.11), 4W10 (St.17). Verbessert durch Anrufungen (z.B. Quälender Stoß: +CHA-Mod Schaden).',
    },
    'Schockgriff': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W8 Blitzschaden. Bei Treffer als metallgerüstete Kreatur: Nachteil auf nächsten Angriff bis Ende ihres Zuges. Schaden steigt mit Stufe.',
    },
    'Shillelagh': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Druide'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '1 Minute',
        'beschreibung': 'Dein Stab wird magisch. Nutze WEI statt STR für Angriff und Schaden. Schaden wird W8 (statt W6). Gilt als magisch.',
    },
    'Sorcerous Burst': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W8 Schaden (Schadenstyp nach Wahl: Säure, Blitz, Feuer, Kälte, Gift, Donner). Bei Ergebnis 8 auf einem Würfel: weiteren W8 hinzufügen. Schaden steigt mit Stufe.',
    },
    'Sternenstaub': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Barde', 'Druide'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Strahlendes Licht schlägt auf eine Kreatur. Trefferwurf: 1W8 strahlender Schaden. Ziel leuchtet bis Ende seiner nächsten Runde (kein Verstecken, Angriffe gegen es haben Vorteil). Schaden steigt mit Stufe.',
    },
    'Tanzende Lichter': {
        'grad': 0, 'schule': 'Illusion',
        'klassen': ['Barde', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Bis zu 4 fackellichtgroße Lichter schweben in der Reichweite. Bewege sie als Bonusaktion bis 18m.',
    },
    'Thaumaturgie': {
        'grad': 0, 'schule': 'Verwandlung',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute',
        'beschreibung': 'Erzeuge einen kleinen göttlichen Effekt: laute Stimme, flackernde Flammen, Boden beben, Augen leuchten, Türen auf-/zuschlagen, oder verändere Aussehen.',
    },
    'Totenberührung': {
        'grad': 0, 'schule': 'Nekromantie',
        'klassen': ['Hexenmeister', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W10 nekrotischen Schaden. Ziel kann bis Ende seines nächsten Zuges keine TP regenerieren. Schaden steigt mit Stufe.',
    },
    'True Strike': {
        'grad': 0, 'schule': 'Divination',
        'klassen': ['Barde', 'Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': 'Sofort',
        'beschreibung': 'Nahkampf- oder Fernkampfangriff mit deinem Zauberattribut (statt STR/GES). Trefferwurf: 1W6 Strahlenschaden. Schaden steigt mit Stufe.',
    },
    'Verschone die Toten': {
        'grad': 0, 'schule': 'Nekromantie',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute',
        'beschreibung': 'Bis zu 3 Untote mit NS 0 in Reichweite müssen WEI-Rettungswurf bestehen oder sind für die Dauer bezaubert (können dich nicht angreifen).',
    },
    'Wort des Glanzes': {
        'grad': 0, 'schule': 'Hervorrufung',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': 'Sofort',
        'beschreibung': 'Strahlendes Licht flackert. RW GES oder 1W6 Strahlenschaden (kein Trefferwurf nötig bei KO-bedingten Gegnern). Schaden steigt mit Stufe.',
    },

    # ── GRAD 1 ────────────────────────────────────────────────────────────────
    'Alarm': {
        'grad': 1, 'schule': 'Bannmagie',
        'klassen': ['Magier', 'Waldläufer'],
        'wirkzeit': '1 Minute (Ritual)', 'reichweite': '9m', 'dauer': '8 Stunden',
        'beschreibung': 'Setzt einen Alarm für einen Bereich (max. 6m Würfel). Wenn eine Kreatur eintritt: mentaler Signalton oder hörbarer Alarm.',
    },
    'Arme von Hadar': {
        'grad': 1, 'schule': 'Beschwörung',
        'klassen': ['Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (3m)', 'dauer': 'Sofort',
        'beschreibung': 'Tentakel aus der Dunkelheit: Alle Kreaturen in 3m um dich – KON-RW oder 2W6 nekrotischen Schaden (halb bei Erfolg). Bei Misserfolg können sie bis Ende ihres nächsten Zuges keine Reaktion nutzen.',
    },
    'Befehl': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Kleriker', 'Paladin', 'Barde'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': '1 Runde',
        'beschreibung': 'Sprich einen einwortigen Befehl: Annäherung, Fall nieder, Flieh, Halt, Komm her – Kreatur muss WEI-RW bestehen oder folgt dem Befehl. Keine Nutzung bei Befehlen gegen ihre Natur.',
    },
    'Brennende Hände': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (4,5m Kegel)', 'dauer': 'Sofort',
        'beschreibung': 'Feuerstrahl aus den Fingern: GES-RW oder 3W6 Feuerschaden (halb bei Erfolg). +1W6 pro höherem Grad.',
    },
    'Chaosbolzen': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 2W8+2W6 Schaden. Der Schadenstyp wird durch das höhere W8-Ergebnis bestimmt (2=Säure, 3=Blitz, 4=Feuer, 5=Kälte, 6=Gift, 7=Psychisch, 8=Donner). Bei Pasch-Würfeln springt er weiter.',
    },
    'Dissonantes Flüstern': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Barde'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Flüstere einen quälenden Ton: WEI-RW oder 3W6 psychischen Schaden und muss seine Reaktion nutzen um sich so weit wie möglich von dir zu bewegen. +1W6 pro höherem Grad.',
    },
    'Donnerwoge': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Barde', 'Druide', 'Magier', 'Paladin', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (4,5m Würfel)', 'dauer': 'Sofort',
        'beschreibung': 'Donnerwelle: KON-RW oder 2W8 Donnerschaden und 3m weggestoßen (halb, kein Stoß bei Erfolg). Lärm bis 90m hörbar. +1W8 pro höherem Grad.',
    },
    'Feenfeuer': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Barde', 'Druide'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Alle Kreaturen in einem 6m Würfel müssen GES-RW bestehen oder leuchten (violett, blau, grün oder gelb). Angriffe gegen leuchtende Kreaturen haben Vorteil.',
    },
    'Gift versprühen': {
        'grad': 1, 'schule': 'Beschwörung',
        'klassen': ['Druide', 'Waldläufer', 'Hexenmeister'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '9m', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 1W12 Giftschaden. Bei Treffer muss Ziel KON-RW bestehen oder ist vergiftet bis Ende seines nächsten Zuges. +1W12 pro höherem Grad.',
    },
    'Göttliche Gunst': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Paladin'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Deine Waffe strahlt göttliches Licht. Waffenangriffe verursachen +1W4 Strahlenschaden.',
    },
    'Gute Beeren': {
        'grad': 1, 'schule': 'Verwandlung',
        'klassen': ['Druide', 'Waldläufer'],
        'wirkzeit': '1 Minute', 'reichweite': 'Berührung', 'dauer': '24 Stunden',
        'beschreibung': 'Erzeuge bis zu 10 magische Beeren. Jede Beere heilt 1 TP und zählt als ausreichende Nahrung.',
    },
    'Hagel von Dornen': {
        'grad': 1, 'schule': 'Beschwörung',
        'klassen': ['Waldläufer'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': 'Konzentration 1 Min.',
        'beschreibung': 'Nächster Fernkampftreffer: Dornen schießen heraus. Ziel und Kreaturen in 1,5m – GES-RW oder 1W10 Stichschaden (halb bei Erfolg). +1W10 pro höherem Grad.',
    },
    'Heilendes Wort': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Barde', 'Kleriker', 'Druide'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Heile eine Kreatur um 2W4 + Zauberattributmod. TP. +2W4 pro höherem Grad.',
    },
    'Heldentum': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Barde', 'Paladin'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Berührte Kreatur wird immun gegen Furcht und erhält temp. TP (= Zauberattributmod.) zu Beginn jedes ihrer Züge.',
    },
    'Heiligtum': {
        'grad': 1, 'schule': 'Bannmagie',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '9m', 'dauer': '1 Minute',
        'beschreibung': 'Schütze eine Kreatur: Angreifer müssen WEI-RW bestehen oder müssen ein anderes Ziel wählen. Endet wenn Geschützte einen Angriff macht oder Zauber wirkt.',
    },
    'Höllischer Tadel': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Hexenmeister'],
        'wirkzeit': 'Reaktion (wenn Schaden erlitten)', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Angreifer muss GES-RW bestehen oder 2W10 Feuerschaden erleiden (halb bei Erfolg). +1W10 pro höherem Grad.',
    },
    'Identifizieren': {
        'grad': 1, 'schule': 'Divination',
        'klassen': ['Barde', 'Magier'],
        'wirkzeit': '1 Minute (Ritual)', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Erkenne Eigenschaften eines magischen Gegenstands oder Zaubers, der auf einer Kreatur wirkt.',
    },
    'Magisches Geschoss': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': 'Sofort',
        'beschreibung': 'Drei magische Pfeile treffen automatisch (kein Trefferwurf). Jeder: 1W4+1 Kraftschaden. +1 Pfeil pro höherem Grad.',
    },
    'Person bezaubern': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Barde', 'Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Stunde',
        'beschreibung': 'WEI-RW oder Kreatur ist bezaubert. Betrachtet dich als befreundeten Bekannten. Endet wenn Schaden erlitten. Ziel weiß danach Bescheid. +1 Ziel pro höherem Grad.',
    },
    'Rüstung des Agathys': {
        'grad': 1, 'schule': 'Bannmagie',
        'klassen': ['Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': '1 Stunde',
        'beschreibung': 'Erhalte 5 temporäre TP und frostige Aura. Wenn Nahkampfangriff temporäre TP trifft: Angreifer 5 Kälteschaden. +5 tempTP und +5 Schaden pro höherem Grad.',
    },
    'Schlaf': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Barde', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '27m', 'dauer': '1 Minute',
        'beschreibung': 'Würfle 5W8. Kreaturen mit den wenigsten TP (die Summe nicht überschreiten) schlafen ein (bewusstlos). Schaden weckt sie. Untodte/Immunität unberührt. +2W8 pro höherem Grad.',
    },
    'Segen': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Kleriker', 'Paladin'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Bis zu 3 Kreaturen deiner Wahl addieren 1W4 auf alle Angriffswürfe und Rettungswürfe. +1 Kreatur pro höherem Grad.',
    },
    'Sengender Schlag': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Paladin'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '1 Konzentration Min.',
        'beschreibung': 'Nächster Waffenangriff: +1W8 Feuerschaden. Getroffenes Ziel leuchtet (Nacht: Angriffe mit Vorteil bis Ende seines nächsten Zuges). +1W8 pro höherem Grad.',
    },
    'Schild': {
        'grad': 1, 'schule': 'Bannmagie',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Reaktion (beim Treffer)', 'reichweite': 'Selbst', 'dauer': '1 Runde',
        'beschreibung': '+5 auf RK (bis Beginn deines nächsten Zuges, inkl. jetzt). Immun gegen Magisches Geschoss bis dahin.',
    },
    'Schild des Glaubens': {
        'grad': 1, 'schule': 'Bannmagie',
        'klassen': ['Kleriker', 'Paladin'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '18m', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': '+2 auf RK einer Kreatur deiner Wahl.',
    },
    'Tasha\'s unaufhaltsames Gelächter': {
        'grad': 1, 'schule': 'Verzauberung',
        'klassen': ['Barde', 'Magier'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Ziel muss WEI-RW bestehen oder wird bis Ende des Zaubers von Gelächter geschüttelt (liegend, Nachteil auf STR-Würfe). Wiederholt Rettungswurf am Ende jedes Zuges.',
    },
    'Tiere sprechen': {
        'grad': 1, 'schule': 'Divination',
        'klassen': ['Barde', 'Druide', 'Waldläufer'],
        'wirkzeit': '1 Minute (Ritual)', 'reichweite': 'Selbst', 'dauer': '10 Minuten',
        'beschreibung': 'Verstehe und kommuniziere mit Tieren. Tiere sind nicht zwangsläufig hilfsbereit.',
    },
    'Wunden heilen': {
        'grad': 1, 'schule': 'Hervorrufung',
        'klassen': ['Barde', 'Kleriker', 'Druide', 'Paladin', 'Waldläufer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Berührte Kreatur erhält 2W8 + Zauberattributmod. TP. Funktioniert nicht an Untoten/Konstrukten. +2W8 pro höherem Grad.',
    },
    'Wunden verursachen': {
        'grad': 1, 'schule': 'Nekromantie',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Trefferwurf: 2W10 + Zauberattributmod. nekrotischen Schaden. +2W10 pro höherem Grad.',
    },
    'Zeichen des Jägers': {
        'grad': 1, 'schule': 'Divination',
        'klassen': ['Waldläufer'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '27m', 'dauer': '1 Stunde (Konz.)',
        'beschreibung': 'Bezeichne eine Kreatur. Angriffe gegen sie: +1W6 Schaden. Du weißt immer wo sie ist (falls in Reichweite). Wenn sie stirbt: Als Bonusaktion neues Ziel bezeichnen. +Dauer pro höherem Grad.',
    },

    # ── GRAD 2 ────────────────────────────────────────────────────────────────
    'Augenschmaus': {
        'grad': 2, 'schule': 'Illusion',
        'klassen': ['Barde', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': 'Erschaffe bis zu 4 Illusionsobjekte (max. 1,5m Würfel je). Beweglich auf Befehl.',
    },
    'Dunkelheit': {
        'grad': 2, 'schule': 'Hervorrufung',
        'klassen': ['Hexenmeister', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': 'Magische Dunkelheit (3m Radius). Kein Licht, auch keine magische Helligkeit unter Grad 2, durchdringt sie. Kreaturen mit Dunkelsicht sehen nicht hindurch.',
    },
    'Entdecker\'s Rasthaus': {
        'grad': 2, 'schule': 'Beschwörung',
        'klassen': ['Barde', 'Magier'],
        'wirkzeit': '10 Minuten (Ritual)', 'reichweite': '9m', 'dauer': '8 Stunden',
        'beschreibung': 'Erschaffe extradimensionale Unterkunft für 8 Stunden (bis zu 9 Personen, einfache Kost und Ruhe).',
    },
    'Entsenden': {
        'grad': 2, 'schule': 'Divination',
        'klassen': ['Barde', 'Kleriker', 'Magier'],
        'wirkzeit': 'Aktion', 'reichweite': 'Unbegrenzt', 'dauer': '1 Runde',
        'beschreibung': 'Sende eine 25-Wörter-Nachricht an eine bekannte Kreatur. Sie kann mit 25 Wörtern antworten.',
    },
    'Feuerklinge': {
        'grad': 2, 'schule': 'Hervorrufung',
        'klassen': ['Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Bonusaktion', 'reichweite': 'Selbst', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': 'Beschwöre feurige Klinge (1W6 Feuerschaden + Zauberattributmod., zündet wenn treffe). +2W6 auf Stufe 4, 6 und 8.',
    },
    'Geisterwächter': {
        'grad': 3, 'schule': 'Beschwörung',
        'klassen': ['Kleriker'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (4,5m)', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': 'Geister schweben um dich. Feindliche Kreaturen in 4,5m haben halbe Bewegungsrate. Wenn sie in den Bereich eintreten oder dort starten: WEI-RW oder 3W8 Strahlen-/Nekrotischen Schaden (halb Erfolg). +1W8 pro höherem Grad.',
    },
    'Unsichtbarkeit': {
        'grad': 2, 'schule': 'Illusion',
        'klassen': ['Barde', 'Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '1 Stunde (Konz.)',
        'beschreibung': 'Eine Kreatur wird unsichtbar. Endet wenn Angriff oder Zauberwirken. +1 Kreatur pro höherem Grad.',
    },
    'Mondstrahl': {
        'grad': 2, 'schule': 'Hervorrufung',
        'klassen': ['Druide'],
        'wirkzeit': 'Aktion', 'reichweite': '45m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Silberweißer Strahl (1,5m Zylinder). Kreaturen im Strahl: KON-RW oder 2W10 Strahlenschaden (halb bei Erfolg). Gestaltwandler haben Nachteil. Strahl beweglich (Bonusaktion). +1W10 pro höherem Grad.',
    },
    'Rindenhaut': {
        'grad': 2, 'schule': 'Verwandlung',
        'klassen': ['Druide'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '8 Stunden',
        'beschreibung': 'RK des Ziels wird mindestens 16 (wenn keine Rüstung). Gibt zusätzlich temporäre TP (WEI-Mod × PB, min 1).',
    },
    'Scorching Ray (Sengende Strahlen)': {
        'grad': 2, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '36m', 'dauer': 'Sofort',
        'beschreibung': 'Erschaffe 3 Feuerstrahlen. Jeder: Trefferwurf 2W6 Feuerschaden. +1 Strahl pro höherem Grad.',
    },
    'Spurlos gehen': {
        'grad': 2, 'schule': 'Illusion',
        'klassen': ['Druide', 'Waldläufer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': '1 Stunde (Konz.)',
        'beschreibung': 'Bis zu 10 Kreaturen in 9m um dich: Geschicklichkeitswürfe auf Heimlichkeit +10. Spurlose Bewegung möglich.',
    },

    # ── GRAD 3 ────────────────────────────────────────────────────────────────
    'Blitz': {
        'grad': 3, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (27m Linie)', 'dauer': 'Sofort',
        'beschreibung': 'Blitz (27m Linie, 1,5m breit): GES-RW oder 8W6 Blitzschaden (halb Erfolg). +1W6 pro höherem Grad.',
    },
    'Fliegen': {
        'grad': 3, 'schule': 'Verwandlung',
        'klassen': ['Magier', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': '10 Minuten (Konz.)',
        'beschreibung': 'Kreatur kann fliegen (Flugrate 18m). +1 Ziel pro höherem Grad.',
    },
    'Feuerball': {
        'grad': 3, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '45m', 'dauer': 'Sofort',
        'beschreibung': 'Feuerexplosion (6m Radius): GES-RW oder 8W6 Feuerschaden (halb bei Erfolg). +1W6 pro höherem Grad.',
    },
    'Gegenzauber': {
        'grad': 3, 'schule': 'Bannmagie',
        'klassen': ['Magier', 'Zauberer', 'Hexenmeister', 'Barde'],
        'wirkzeit': 'Reaktion (wenn Kreatur in 18m zaubert)', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Unterbrich einen Zauber von Grad 3 oder niedriger automatisch. Gegen höhere Grade: Zauberattributmod.+Übungsbonus gegen SG 10+Grad des Zaubers.',
    },
    'Hast': {
        'grad': 3, 'schule': 'Verwandlung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Kreatur verdoppelt Bewegungsrate, +2 RK, Vorteil auf GES-RW, und eine Zusatzaktion (Angriff/Spurt/Rückzug/Verstecken/Objekt nutzen) pro Runde. Nach Ende: Erschöpfung 1 Runde.',
    },
    'Hunger von Hadar': {
        'grad': 3, 'schule': 'Beschwörung',
        'klassen': ['Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '45m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Schwarze Kugel (1,8m Radius) aus dem Nichts: totale Dunkelheit, eisige Tentakel. Kreaturen im Bereich: KON-RW am Ende ihres Zuges oder 2W6 Kälteschaden (halb bei Erfolg). Start im Bereich: GES-RW oder 2W6 Säureschaden.',
    },
    'Massenheilung Wort': {
        'grad': 3, 'schule': 'Hervorrufung',
        'klassen': ['Kleriker', 'Barde'],
        'wirkzeit': 'Bonusaktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Bis zu 6 Kreaturen heilen 2W4+Zauberattributmod. TP. +1W4 pro höherem Grad.',
    },
    'Revivify': {
        'grad': 3, 'schule': 'Nekromantie',
        'klassen': ['Kleriker', 'Paladin'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Erwecke eine Kreatur die in der letzten Minute gestorben ist mit 1 TP. Keine Wiederherstellung fehlender Körperteile.',
    },
    'Zauber bannen': {
        'grad': 3, 'schule': 'Bannmagie',
        'klassen': ['Kleriker', 'Druide', 'Magier', 'Paladin', 'Waldläufer', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Beende Zauber auf einer Kreatur. Zauber ≤ Grad 3: automatisch. Höhere Grade: Zauberattributmod.+ÜB gegen SG 10+Grad des Zaubers.',
    },

    # ── GRAD 4 ────────────────────────────────────────────────────────────────
    'Bannung': {
        'grad': 4, 'schule': 'Bannmagie',
        'klassen': ['Kleriker', 'Magier', 'Paladin', 'Zauberer', 'Hexenmeister'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Bis zu 2 Kreaturen müssen CHA-RW bestehen oder werden gebannt. Einheimische auf fremde Ebene: permanent. +1 Kreatur pro höherem Grad.',
    },
    'Gestalt wandeln': {
        'grad': 4, 'schule': 'Verwandlung',
        'klassen': ['Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '9m', 'dauer': '1 Stunde (Konz.)',
        'beschreibung': 'Verwandle eine Kreatur in ein anderes Tier (NS ≤ Stufe/4, min. NS 1). Rettet alle Rettungswürfe mit eigenen Werten, verliert Klassenmerkmale.',
    },
    'Phantomkiller': {
        'grad': 4, 'schule': 'Illusion',
        'klassen': ['Magier', 'Barde'],
        'wirkzeit': 'Aktion', 'reichweite': '27m', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Ziel erleidet schreckliche Halluzinationen. WEI-RW oder 4W10 psychischen Schaden und erschreckt. Jede Runde: weiterer WEI-RW oder weitere 4W10 psychischen Schaden.',
    },
    'Zauberschloss': {
        'grad': 4, 'schule': 'Bannmagie',
        'klassen': ['Magier'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Bis Aufgehoben',
        'beschreibung': 'Schließe einen Eingang magisch ab. Nur du (oder Passwort) kannst ihn öffnen. "Durchstoßen" mit Nagel-Zauber-Schlag.',
    },

    # ── GRAD 5 ────────────────────────────────────────────────────────────────
    'Auferstehung': {
        'grad': 5, 'schule': 'Nekromantie',
        'klassen': ['Kleriker', 'Paladin', 'Barde'],
        'wirkzeit': '1 Stunde', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Erwecke eine Kreatur (max. 10 Jahre tot) mit vollen TP. Langwierige Aktivität, Kreatur ist für 4 Tage erschöpft.',
    },
    'Eisiger Sturm': {
        'grad': 4, 'schule': 'Hervorrufung',
        'klassen': ['Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '90m', 'dauer': 'Sofort',
        'beschreibung': 'Hagelkörner (6m Radius, 12m hoch): GES-RW oder 2W8 Kälteschaden + 4W6 Streifschaden (Körperlich). Bereich wird schwieriges Gelände. +1W8 Kälteschaden pro höherem Grad.',
    },
    'Feuerseele': {
        'grad': 5, 'schule': 'Hervorrufung',
        'klassen': ['Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': '10 Minuten',
        'beschreibung': 'Du wirst zu einer Feuerkugel: Flugrate, Feuerschaden-Immunität, Lichtemission, jede Kreatur die dich berührt oder trifft erleidet 1W10 Feuerschaden.',
    },
    'Konjuration Elementar': {
        'grad': 5, 'schule': 'Beschwörung',
        'klassen': ['Druide', 'Magier'],
        'wirkzeit': '1 Minute', 'reichweite': '27m', 'dauer': '1 Stunde (Konz.)',
        'beschreibung': 'Beschwöre einen NS 5-Elementar (Feuer, Erde, Wasser, Luft) als Verbündeten.',
    },

    # ── GRAD 6 ────────────────────────────────────────────────────────────────
    'Kettenschlag': {
        'grad': 6, 'schule': 'Hervorrufung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '27m', 'dauer': 'Sofort',
        'beschreibung': 'Blitz springt zwischen 4 Zielen: Trefferwurf je 10W8 Blitzschaden.',
    },
    'Sunbeam': {
        'grad': 6, 'schule': 'Hervorrufung',
        'klassen': ['Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (18m Linie)', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Sonnenstrahl (18m×1,5m): KON-RW oder 6W8 Strahlenschaden + blind. Jede Runde als Aktion neu ausrichten.',
    },

    # ── GRAD 7 ────────────────────────────────────────────────────────────────
    'Ebenenverschiebung': {
        'grad': 7, 'schule': 'Beschwörung',
        'klassen': ['Kleriker', 'Druide', 'Magier', 'Hexenmeister', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Ziel muss CHA-RW bestehen oder wird auf eine andere Ebene teleportiert. Freiwillig auch möglich (für bis zu 8 Kreaturen).',
    },
    'Finger des Todes': {
        'grad': 7, 'schule': 'Nekromantie',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Ziel: KON-RW oder 7W8+30 nekrotischen Schaden (halb bei Erfolg). Stirbt das Ziel: erhebt als Zombie unter deiner Kontrolle.',
    },

    # ── GRAD 8 ────────────────────────────────────────────────────────────────
    'Mächtiges Wort des Sterbens': {
        'grad': 8, 'schule': 'Nekromantie',
        'klassen': ['Kleriker', 'Barde'],
        'wirkzeit': 'Aktion', 'reichweite': '18m', 'dauer': 'Sofort',
        'beschreibung': 'Töte sofort eine Kreatur mit 100 TP oder weniger (kein Rettungswurf). Über 100 TP: 10W10 nekrotischer Schaden.',
    },
    'Sonnenlicht': {
        'grad': 8, 'schule': 'Hervorrufung',
        'klassen': ['Druide', 'Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst (18m Radius)', 'dauer': '1 Minute (Konz.)',
        'beschreibung': 'Helles Sonnenlicht (18m Radius): Untote/Lichtempfindliche haben Nachteil auf Angriffe. Vampire und Ähnliche können nicht regenerieren.',
    },

    # ── GRAD 9 ────────────────────────────────────────────────────────────────
    'Wunsch': {
        'grad': 9, 'schule': 'Beschwörung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': 'Sofort',
        'beschreibung': 'Der mächtigste Zauber. Dupliziere jeden anderen Zauber (bis Grad 8) ohne Materialkomponenten oder wünsche eine Realitätsveränderung. Risikoreich bei Missbrauch (Stress, nie mehr Wunsch möglich).',
    },
    'Zeitstillstand': {
        'grad': 9, 'schule': 'Verwandlung',
        'klassen': ['Magier', 'Zauberer'],
        'wirkzeit': 'Aktion', 'reichweite': 'Selbst', 'dauer': 'Sofort',
        'beschreibung': 'Zeit hält an. 1W4+1 Runden handeln, während alle anderen erstarrt sind. Jede Interaktion mit einer anderen Kreatur beendet den Zauber.',
    },
    'Wahres Auferstehungswort': {
        'grad': 9, 'schule': 'Nekromantie',
        'klassen': ['Kleriker', 'Druide'],
        'wirkzeit': '1 Stunde', 'reichweite': 'Berührung', 'dauer': 'Sofort',
        'beschreibung': 'Erwecke jede Kreatur (selbst wenn der Körper zerstört war) zu vollem Leben. Keine Altersbeschränkung. Kreatur wählt neues Volk falls sie will.',
    },
}

# ── Zauberlisten nach Klasse ──────────────────────────────────────────────────
def get_zauberliste(klasse: str) -> dict[int, list[str]]:
    """Gibt alle Zauber einer Klasse gruppiert nach Grad zurück."""
    result: dict[int, list[str]] = {}
    for name, data in ZAUBER.items():
        if klasse in data.get('klassen', []):
            grad = data['grad']
            result.setdefault(grad, []).append(name)
    for grad in result:
        result[grad].sort()
    return result


# ── Zauberlisten (vorberechnet) ───────────────────────────────────────────────
ZAUBERLISTEN = {
    klasse: get_zauberliste(klasse)
    for klasse in [
        'Barde', 'Kleriker', 'Druide', 'Magier',
        'Paladin', 'Waldläufer', 'Hexenmeister', 'Zauberer',
    ]
}
