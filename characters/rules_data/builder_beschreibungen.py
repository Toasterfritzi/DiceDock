"""
Beschreibungstexte für den interaktiven Charakter-Builder.
Enthält Flavor-Texte, Vorteile und Bildpfade für Klassen, Unterklassen und Hintergründe.
"""

KLASSEN_BESCHREIBUNGEN = {
    'Barbar': {
        'beschreibung': 'Ein wilder Krieger, der im Kampf in einen unbändigen Zorn gerät.',
        'vorteile': ['Enorme Zähigkeit', 'Hoher Nahkampfschaden', 'Kampfrausch'],
        'bild': 'images/classes/barbar.png',
    },
    'Barde': {
        'beschreibung': 'Ein inspirierender Magiewirker, der die Kraft der Musik und Worte nutzt.',
        'vorteile': ['Vielseitig', 'Unterstützt Verbündete', 'Starke soziale Fertigkeiten'],
        'bild': 'images/classes/barde.png',
    },
    'Kleriker': {
        'beschreibung': 'Ein priesterlicher Diener einer Gottheit, der Wunder und Heilung wirkt.',
        'vorteile': ['Hervorragende Heilung', 'Göttliche Unterstützung', 'Gute Rüstungen'],
        'bild': 'images/classes/kleriker.png',
    },
    'Druide': {
        'beschreibung': 'Ein Hüter der Natur, der sich in Tiere verwandeln kann.',
        'vorteile': ['Tiergestalt-Verwandlung', 'Naturmagie', 'Hohe Vielseitigkeit'],
        'bild': 'images/classes/druide.png',
    },
    'Kämpfer': {
        'beschreibung': 'Ein Meister der Waffen und Rüstungen mit überlegener Technik.',
        'vorteile': ['Zusätzliche Angriffe', 'Aktionsschub', 'Extrem anpassbar'],
        'bild': 'images/classes/kaempfer.png',
    },
    'Mönch': {
        'beschreibung': 'Ein Kampfkünstler, der seinen Körper durch innere Energie perfektioniert.',
        'vorteile': ['Schnelle Bewegungen', 'Viele Angriffe', 'Rüstungslose Verteidigung'],
        'bild': 'images/classes/moench.png',
    },
    'Paladin': {
        'beschreibung': 'Ein heiliger Ritter, der durch einen Eid göttliche Macht entfesselt.',
        'vorteile': ['Starker Nahkampf', 'Göttliches Niederstrecken', 'Schützende Auren'],
        'bild': 'images/classes/paladin.png',
    },
    'Waldläufer': {
        'beschreibung': 'Ein Grenzgänger und Jäger, der die Wildnis beherrscht.',
        'vorteile': ['Fernkampf-Spezialist', 'Tierbegleiter oder Waldmagie', 'Gute Spurensuche'],
        'bild': 'images/classes/waldlaeufer.png',
    },
    'Schurke': {
        'beschreibung': 'Ein Meister der List, der Heimlichkeit und Präzision nutzt.',
        'vorteile': ['Hinterhältige Angriffe', 'Viele Fertigkeiten', 'Meisterhafte List'],
        'bild': 'images/classes/schurke.png',
    },
    'Zauberer': {
        'beschreibung': 'Ein Magiewirker, dessen Macht in seinem eigenen Blut liegt.',
        'vorteile': ['Mächtige Metamagie', 'Spontanes Zaubern', 'Hohe magische Kraft'],
        'bild': 'images/classes/zauberer.png',
    },
    'Hexenmeister': {
        'beschreibung': 'Ein Paktierer mit einer mächtigen Wesenheit für dunkle Gaben.',
        'vorteile': ['Regeneriert Zauber bei kurzer Rast', 'Mächtige Anrufungen', 'Paktgaben'],
        'bild': 'images/classes/hexenmeister.png',
    },
    'Magier': {
        'beschreibung': 'Ein Gelehrter der arkanen Künste, der Zauber aus Büchern studiert.',
        'vorteile': ['Riesige Zauberauswahl', 'Hohe Spezialisierung', 'Arkane Erholung'],
        'bild': 'images/classes/magier.png',
    },
}

UNTERKLASSEN_BESCHREIBUNGEN = {
    # --- Barbar ---
    'Berserker': {
        'klasse': 'Barbar',
        'beschreibung': 'Konzentriert sich auf reine Gewalt und zusätzliche Angriffe im Zorn.',
        'bild': 'images/subclasses/berserker.png',
    },
    'Wildes Herz': {
        'klasse': 'Barbar',
        'beschreibung': 'Nutzt die Geister von Tieren (Bär, Adler, Wolf) für Schutz oder Angriff.',
        'bild': 'images/subclasses/wildes_herz.png',
    },
    'Weltenbaum': {
        'klasse': 'Barbar',
        'beschreibung': 'Beschwört die Kraft der Natur und kann Gegner auf Distanz kontrollieren.',
        'bild': 'images/subclasses/weltenbaum.png',
    },
    'Eiferer': {
        'klasse': 'Barbar',
        'beschreibung': 'Ein göttlich inspirierter Krieger, der den Tod im Kampf verachtet.',
        'bild': 'images/subclasses/eiferer.png',
    },
    # --- Barde ---
    'Schule des Wissens': {
        'klasse': 'Barde',
        'beschreibung': 'Fokus auf zusätzliche Zauber und das Stören von Gegnern.',
        'bild': 'images/subclasses/schule_des_wissens.png',
    },
    'Schule des Tanzes': {
        'klasse': 'Barde',
        'beschreibung': 'Nutzt Bewegung und unbewaffneten Kampf zur Unterstützung.',
        'bild': 'images/subclasses/schule_des_tanzes.png',
    },
    'Schule des Wagemuts': {
        'klasse': 'Barde',
        'beschreibung': 'Ein kampfbetonter Barde, der Gefährten direkt im Getümmel inspiriert.',
        'bild': 'images/subclasses/schule_des_wagemuts.png',
    },
    'Schule des Zauberbanns': {
        'klasse': 'Barde',
        'beschreibung': 'Nutzt Bezauberungen und Befehle, um das Schlachtfeld zu kontrollieren.',
        'bild': 'images/subclasses/schule_des_zauberbanns.png',
    },
    # --- Kleriker ---
    'Domäne des Lebens': {
        'klasse': 'Kleriker',
        'beschreibung': 'Der ultimative Heiler, der die Lebenskraft seiner Gruppe stärkt.',
        'bild': 'images/subclasses/domaene_des_lebens.png',
    },
    'Domäne des Lichts': {
        'klasse': 'Kleriker',
        'beschreibung': 'Nutzt die brennende Macht der Sonne für hohen Strahlungsschaden.',
        'bild': 'images/subclasses/domaene_des_lichts.png',
    },
    'Domäne der List': {
        'klasse': 'Kleriker',
        'beschreibung': 'Spezialisiert auf Täuschung, Illusionen und lautloses Vorgehen.',
        'bild': 'images/subclasses/domaene_der_list.png',
    },
    'Domäne des Krieges': {
        'klasse': 'Kleriker',
        'beschreibung': 'Kämpft an vorderster Front mit zusätzlichen Waffenangriffen.',
        'bild': 'images/subclasses/domaene_des_krieges.png',
    },
    # --- Druide ---
    'Zirkel des Landes': {
        'klasse': 'Druide',
        'beschreibung': 'Vertieft die Verbindung zur Umwelt für zusätzliche Zauberkraft.',
        'bild': 'images/subclasses/zirkel_des_landes.png',
    },
    'Zirkel des Mondes': {
        'klasse': 'Druide',
        'beschreibung': 'Spezialist für Tierverwandlung – stärkere Formen und Heilung im Kampf.',
        'bild': 'images/subclasses/zirkel_des_mondes.png',
    },
    'Zirkel des Meeres': {
        'klasse': 'Druide',
        'beschreibung': 'Nutzt die stürmische Kraft der Ozeane zur Verteidigung.',
        'bild': 'images/subclasses/zirkel_des_meeres.png',
    },
    'Zirkel der Sterne': {
        'klasse': 'Druide',
        'beschreibung': 'Nutzt Konstellationen für Fernkampf, Heilung oder Konzentration.',
        'bild': 'images/subclasses/zirkel_der_sterne.png',
    },
    # --- Kämpfer ---
    'Champion': {
        'klasse': 'Kämpfer',
        'beschreibung': 'Einfach und effektiv – konzentriert sich auf kritische Treffer und Athletik.',
        'bild': 'images/subclasses/champion.png',
    },
    'Kampfmeister': {
        'klasse': 'Kämpfer',
        'beschreibung': 'Ein Taktiker, der Spezialmanöver nutzt, um den Kampf zu lenken.',
        'bild': 'images/subclasses/kampfmeister.png',
    },
    'Psi-Krieger': {
        'klasse': 'Kämpfer',
        'beschreibung': 'Nutzt die Kraft des Geistes für Schutz und zusätzliche Angriffe.',
        'bild': 'images/subclasses/psi_krieger.png',
    },
    'Mystischer Ritter': {
        'klasse': 'Kämpfer',
        'beschreibung': 'Kombiniert Kampfkunst mit Magieschulen der Zerstörung und Abwehr.',
        'bild': 'images/subclasses/mystischer_ritter.png',
    },
    # --- Mönch ---
    'Offene Hand': {
        'klasse': 'Mönch',
        'beschreibung': 'Meister des unbewaffneten Kampfes und der Kontrolle von Gegnern.',
        'bild': 'images/subclasses/offene_hand.png',
    },
    'Elemente': {
        'klasse': 'Mönch',
        'beschreibung': 'Kanalisiert elementare Kräfte für Angriffe auf höhere Reichweite.',
        'bild': 'images/subclasses/elemente.png',
    },
    'Gnade': {
        'klasse': 'Mönch',
        'beschreibung': 'Ein Wanderer zwischen Leben und Tod, der heilen oder Leid zufügen kann.',
        'bild': 'images/subclasses/gnade.png',
    },
    'Schatten': {
        'klasse': 'Mönch',
        'beschreibung': 'Nutzt Dunkelheit und Teleportation für heimliche Angriffe.',
        'bild': 'images/subclasses/schatten.png',
    },
    # --- Paladin ---
    'Eid der Hingabe': {
        'klasse': 'Paladin',
        'beschreibung': 'Der klassische Ritter in strahlender Rüstung – Schutz und Wahrheit.',
        'bild': 'images/subclasses/eid_der_hingabe.png',
    },
    'Eid der Rache': {
        'klasse': 'Paladin',
        'beschreibung': 'Ein unerbittlicher Verfolger, der seine Feinde bis in den Tod jagt.',
        'bild': 'images/subclasses/eid_der_rache.png',
    },
    'Eid der Uralten': {
        'klasse': 'Paladin',
        'beschreibung': 'Ein Beschützer des Lichts und der Natur mit magischer Abwehr.',
        'bild': 'images/subclasses/eid_der_uralten.png',
    },
    'Eid des Ruhms': {
        'klasse': 'Paladin',
        'beschreibung': 'Ein heroischer Athlet, der durch Taten und Schnelligkeit glänzt.',
        'bild': 'images/subclasses/eid_des_ruhms.png',
    },
    # --- Waldläufer ---
    'Jäger': {
        'klasse': 'Waldläufer',
        'beschreibung': 'Spezialisiert auf das Töten bestimmter Gegnertypen.',
        'bild': 'images/subclasses/jaeger.png',
    },
    'Herr der Tiere': {
        'klasse': 'Waldläufer',
        'beschreibung': 'Kämpft Seite an Seite mit einem treuen Tierbegleiter.',
        'bild': 'images/subclasses/herr_der_tiere.png',
    },
    'Düsterpirscher': {
        'klasse': 'Waldläufer',
        'beschreibung': 'Ein Meister des Hinterhalts, besonders effektiv in der ersten Kampfrunde.',
        'bild': 'images/subclasses/duesterpirscher.png',
    },
    'Feenwanderer': {
        'klasse': 'Waldläufer',
        'beschreibung': 'Nutzt die Magie des Feenwilds für psychischen Schaden und Manipulation.',
        'bild': 'images/subclasses/feenwanderer.png',
    },
    # --- Schurke ---
    'Dieb': {
        'klasse': 'Schurke',
        'beschreibung': 'Fokus auf Beweglichkeit, Klettern und die Nutzung von Gegenständen im Kampf.',
        'bild': 'images/subclasses/dieb.png',
    },
    'Assassine': {
        'klasse': 'Schurke',
        'beschreibung': 'Ein Spezialist für tödliche Überraschungsangriffe und Infiltration.',
        'bild': 'images/subclasses/assassine.png',
    },
    'Arkaner Betrüger': {
        'klasse': 'Schurke',
        'beschreibung': 'Kombiniert Diebeskunst mit Illusions- und Verzauberungsmagie.',
        'bild': 'images/subclasses/arkaner_betrueger.png',
    },
    'Seelenmesser': {
        'klasse': 'Schurke',
        'beschreibung': 'Erschafft Waffen aus reiner psychischer Energie.',
        'bild': 'images/subclasses/seelenmesser.png',
    },
    # --- Zauberer ---
    'Drachenblut-Linie': {
        'klasse': 'Zauberer',
        'beschreibung': 'Zähigkeit und Elementarschaden durch das Erbe der Drachen.',
        'bild': 'images/subclasses/drachenblut_linie.png',
    },
    'Wilde Magie': {
        'klasse': 'Zauberer',
        'beschreibung': 'Unvorhersehbare arkane Wogen, die Chaos auf dem Schlachtfeld stiften.',
        'bild': 'images/subclasses/wilde_magie.png',
    },
    'Aberrante Übereinkunft': {
        'klasse': 'Zauberer',
        'beschreibung': 'Nutzt psionische Magie und Gedankenmanipulation.',
        'bild': 'images/subclasses/aberrante_uebereinkunft.png',
    },
    'Uhrwerk-Spross': {
        'klasse': 'Zauberer',
        'beschreibung': 'Nutzt die kosmische Ordnung zum Schutz vor Chaos und Schaden.',
        'bild': 'images/subclasses/uhrwerk_spross.png',
    },
    # --- Hexenmeister ---
    'Unhold': {
        'klasse': 'Hexenmeister',
        'beschreibung': 'Erhält Lebenskraft durch das Töten von Feinden.',
        'bild': 'images/subclasses/unhold.png',
    },
    'Großer Alter': {
        'klasse': 'Hexenmeister',
        'beschreibung': 'Nutzt Telepathie und psychische Kräfte zur Manipulation.',
        'bild': 'images/subclasses/grosser_alter.png',
    },
    'Erzfee': {
        'klasse': 'Hexenmeister',
        'beschreibung': 'Fokus auf Teleportation, Bezauberung und flüchtige Magie.',
        'bild': 'images/subclasses/erzfee.png',
    },
    'Celestischer': {
        'klasse': 'Hexenmeister',
        'beschreibung': 'Verbindet Paktmagie mit heilender göttlicher Kraft.',
        'bild': 'images/subclasses/celestischer.png',
    },
    # --- Magier ---
    'Schule der Hervorrufung': {
        'klasse': 'Magier',
        'beschreibung': 'Erzeugt mächtige Elementarexplosionen, ohne Gefährten zu treffen.',
        'bild': 'images/subclasses/schule_der_hervorrufung.png',
    },
    'Schule der Abjuration': {
        'klasse': 'Magier',
        'beschreibung': 'Fokus auf magische Barrieren und den Schutz der Gruppe.',
        'bild': 'images/subclasses/schule_der_abjuration.png',
    },
    'Schule der Erkenntnis': {
        'klasse': 'Magier',
        'beschreibung': 'Kann die Zukunft vorausahnen und Würfelergebnisse beeinflussen.',
        'bild': 'images/subclasses/schule_der_erkenntnis.png',
    },
    'Schule der Illusion': {
        'klasse': 'Magier',
        'beschreibung': 'Erschafft täuschend echte Bilder zur Verwirrung der Feinde.',
        'bild': 'images/subclasses/schule_der_illusion.png',
    },
}

HINTERGRUND_BESCHREIBUNGEN = {
    'Adeliger': {
        'beschreibung': 'Du wurdest in Reichtum und Privilegien geboren und kennst die Etikette der Oberschicht.',
        'bild': 'images/backgrounds/adeliger.png',
    },
    'Akolyth': {
        'beschreibung': 'Du hast dein Leben dem Dienst in einem Tempel und dem Studium heiliger Texte gewidmet.',
        'bild': 'images/backgrounds/akolyth.png',
    },
    'Bauer': {
        'beschreibung': 'Du kennst die harte Arbeit auf dem Feld und hast eine enge Verbindung zum einfachen Volk.',
        'bild': 'images/backgrounds/bauer.png',
    },
    'Einsiedler': {
        'beschreibung': 'Du hast lange Zeit in Abgeschiedenheit gelebt und dabei tiefe spirituelle Erkenntnisse gewonnen.',
        'bild': 'images/backgrounds/einsiedler.png',
    },
    'Händler': {
        'beschreibung': 'Du bist ein Reisender des Marktes, geschickt im Verhandeln und Feilschen um Gold.',
        'bild': 'images/backgrounds/haendler.png',
    },
    'Handwerker': {
        'beschreibung': 'Dein Leben bestand aus harter Arbeit in einer Werkstatt und der Perfektionierung deines Handwerks.',
        'bild': 'images/backgrounds/handwerker.png',
    },
    'Krimineller': {
        'beschreibung': 'Du hast gelernt, außerhalb des Gesetzes zu überleben, sei es durch Diebstahl oder List.',
        'bild': 'images/backgrounds/krimineller.png',
    },
    'Reisender': {
        'beschreibung': 'Du bist weit gewandert und hast viele Kulturen kennengelernt; deine Heimat ist der Weg.',
        'bild': 'images/backgrounds/reisender.png',
    },
    'Scharlatan': {
        'beschreibung': 'Du bist ein Meister der Täuschung, der mit falschen Identitäten und Tricks seinen Weg geht.',
        'bild': 'images/backgrounds/scharlatan.png',
    },
    'Schreiber': {
        'beschreibung': 'Dein Leben war dem Kopieren von Dokumenten und dem Bewahren von Wissen gewidmet.',
        'bild': 'images/backgrounds/schreiber.png',
    },
    'Seemann': {
        'beschreibung': 'Die Weite des Ozeans ist dein Zuhause; du beherrschst Schiffe und kennst die Gefahren der See.',
        'bild': 'images/backgrounds/seemann.png',
    },
    'Soldat': {
        'beschreibung': 'Du wurdest für den Krieg ausgebildet und hast in einer Armee oder Stadtwache gedient.',
        'bild': 'images/backgrounds/soldat.png',
    },
    'Unterhaltungskünstler': {
        'beschreibung': 'Du lebst für den Applaus und weißt, wie man ein Publikum mit Musik oder Akrobatik fesselt.',
        'bild': 'images/backgrounds/unterhaltungskuenstler.png',
    },
    'Wache': {
        'beschreibung': 'Du hast die Tore und Mauern bemannt und gelernt, Gefahren frühzeitig zu erkennen.',
        'bild': 'images/backgrounds/wache.png',
    },
    'Wegfinder': {
        'beschreibung': 'Du führst Reisende sicher durch gefährliches Gelände und kennst jeden Pfad in der Wildnis.',
        'bild': 'images/backgrounds/wegfinder.png',
    },
    'Weiser': {
        'beschreibung': 'Ein Gelehrter, der Jahre mit dem Studium von Büchern und wissenschaftlichen Rätseln verbracht hat.',
        'bild': 'images/backgrounds/weiser.png',
    },
}
