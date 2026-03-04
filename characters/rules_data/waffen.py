WAFFEN_DATEN = {
    # Einfache Nahkampfwaffen
    'Keule': {'schaden': '1d4', 'schadenstyp': 'wucht', 'eigenschaften': ['leicht'], 'meisterung': 'Slow'},
    'Dolch': {'schaden': '1d4', 'schadenstyp': 'stich', 'eigenschaften': ['finesse', 'leicht', 'wurfwaffe'], 'meisterung': 'Nick'},
    'Großer Knüppel': {'schaden': '1d8', 'schadenstyp': 'wucht', 'eigenschaften': ['zweihändig'], 'meisterung': 'Topple'},
    'Handaxt': {'schaden': '1d6', 'schadenstyp': 'hieb', 'eigenschaften': ['leicht', 'wurfwaffe'], 'meisterung': 'Vex'},
    'Wurfspeer': {'schaden': '1d6', 'schadenstyp': 'stich', 'eigenschaften': ['wurfwaffe'], 'meisterung': 'Slow'},
    'Leichter Hammer': {'schaden': '1d4', 'schadenstyp': 'wucht', 'eigenschaften': ['leicht', 'wurfwaffe'], 'meisterung': 'Nick'},
    'Streitkolben': {'schaden': '1d6', 'schadenstyp': 'wucht', 'eigenschaften': [], 'meisterung': 'Sap'},
    'Kampfstab': {'schaden': '1d6', 'schadenstyp': 'wucht', 'eigenschaften': ['vielseitig (1d8)'], 'meisterung': 'Topple'},
    'Sichel': {'schaden': '1d4', 'schadenstyp': 'hieb', 'eigenschaften': ['leicht'], 'meisterung': 'Nick'},
    'Speer': {'schaden': '1d6', 'schadenstyp': 'stich', 'eigenschaften': ['wurfwaffe', 'vielseitig (1d8)'], 'meisterung': 'Sap'},
    
    # Einfache Fernkampfwaffen
    'Leichte Armbrust': {'schaden': '1d8', 'schadenstyp': 'stich', 'eigenschaften': ['munition', 'fernkampf', 'zweihändig'], 'meisterung': 'Slow'},
    'Kurzbogen': {'schaden': '1d6', 'schadenstyp': 'stich', 'eigenschaften': ['munition', 'fernkampf', 'zweihändig'], 'meisterung': 'Vex'},
    'Schleuder': {'schaden': '1d4', 'schadenstyp': 'wucht', 'eigenschaften': ['munition', 'fernkampf'], 'meisterung': 'Slow'},
    
    # Kriegsnahkampfwaffen
    'Streitaxt': {'schaden': '1d8', 'schadenstyp': 'hieb', 'eigenschaften': ['vielseitig (1d10)'], 'meisterung': 'Topple'},
    'Flegel': {'schaden': '1d8', 'schadenstyp': 'wucht', 'eigenschaften': [], 'meisterung': 'Sap'},
    'Gleve': {'schaden': '1d10', 'schadenstyp': 'hieb', 'eigenschaften': ['schwer', 'reichweite', 'zweihändig'], 'meisterung': 'Graze'},
    'Hellebarde': {'schaden': '1d10', 'schadenstyp': 'hieb', 'eigenschaften': ['schwer', 'reichweite', 'zweihändig'], 'meisterung': 'Cleave'},
    'Großaxt': {'schaden': '1d12', 'schadenstyp': 'hieb', 'eigenschaften': ['schwer', 'zweihändig'], 'meisterung': 'Cleave'},
    'Zweihänder': {'schaden': '2d6', 'schadenstyp': 'hieb', 'eigenschaften': ['schwer', 'zweihändig'], 'meisterung': 'Graze'},
    'Pike': {'schaden': '1d10', 'schadenstyp': 'stich', 'eigenschaften': ['schwer', 'reichweite', 'zweihändig'], 'meisterung': 'Push'},
    'Langschwert': {'schaden': '1d8', 'schadenstyp': 'hieb', 'eigenschaften': ['vielseitig (1d10)'], 'meisterung': 'Sap'},
    'Morgenstern': {'schaden': '1d8', 'schadenstyp': 'stich', 'eigenschaften': [], 'meisterung': 'Sap'},
    'Rapier': {'schaden': '1d8', 'schadenstyp': 'stich', 'eigenschaften': ['finesse'], 'meisterung': 'Vex'},
    'Krummsäbel': {'schaden': '1d6', 'schadenstyp': 'hieb', 'eigenschaften': ['finesse', 'leicht'], 'meisterung': 'Nick'},
    'Kurzschwert': {'schaden': '1d6', 'schadenstyp': 'stich', 'eigenschaften': ['finesse', 'leicht'], 'meisterung': 'Vex'},
    'Kriegshammer': {'schaden': '1d8', 'schadenstyp': 'wucht', 'eigenschaften': ['vielseitig (1d10)'], 'meisterung': 'Topple'},
    'Peitsche': {'schaden': '1d4', 'schadenstyp': 'hieb', 'eigenschaften': ['finesse', 'reichweite'], 'meisterung': 'Slow'},
    
    # Kriegsfernkampfwaffen
    'Handarmbrust': {'schaden': '1d6', 'schadenstyp': 'stich', 'eigenschaften': ['munition', 'fernkampf', 'leicht'], 'meisterung': 'Vex'},
    'Schwere Armbrust': {'schaden': '1d10', 'schadenstyp': 'stich', 'eigenschaften': ['munition', 'fernkampf', 'schwer', 'zweihändig'], 'meisterung': 'Push'},
    'Langbogen': {'schaden': '1d8', 'schadenstyp': 'stich', 'eigenschaften': ['munition', 'fernkampf', 'schwer', 'zweihändig'], 'meisterung': 'Slow'},
}

WAFFEN_MEISTERUNGEN = {
    'Cleave': {
        'name': 'Spalten',
        'beschreibung': 'Wenn du eine Kreatur triffst, kannst du einen zweiten Angriff gegen eine andere Kreatur in deiner Reichweite ausführen (einmal pro Zug).'
    },
    'Graze': {
        'name': 'Streifen',
        'beschreibung': 'Wenn du einen Angriff verfehlst, erleidet das Ziel trotzdem Schaden in Höhe deines Attributsmodifikators (Minimum 0).'
    },
    'Nick': {
        'name': 'Ritzen',
        'beschreibung': 'Du kannst den zusätzlichen Angriff der Eigenschaft "Leicht" als Teil deiner Angriffsaktion ausführen (statt als Bonusaktion).'
    },
    'Push': {
        'name': 'Stoßen',
        'beschreibung': 'Wenn du eine Kreatur triffst, kannst du sie bis zu 3 Meter von dir wegschieben.'
    },
    'Sap': {
        'name': 'Schwächen',
        'beschreibung': 'Wenn du eine Kreatur triffst, hat sie Nachteil auf ihren nächsten Angriffswurf vor dem Beginn deines nächsten Zuges.'
    },
    'Slow': {
        'name': 'Verlangsamen',
        'beschreibung': 'Wenn du eine Kreatur triffst, reduziert sich ihre Bewegungsrate um 3 Meter bis zum Beginn deines nächsten Zuges.'
    },
    'Topple': {
        'name': 'Umwerfen',
        'beschreibung': 'Wenn du eine Kreatur triffst, muss sie einen KON-Rettungswurf (SG 8 + ÜB + Attributsmod) bestehen oder wird liegend.'
    },
    'Vex': {
        'name': 'Ärgern',
        'beschreibung': 'Wenn du eine Kreatur triffst, hast du Vorteil auf deinen nächsten Angriffswurf gegen dieses Ziel vor dem Ende deines nächsten Zuges.'
    },
}
