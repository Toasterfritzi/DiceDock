# Abschlussbericht: Regelbuch-Audit (D&D 2024)

Ich habe den gesamten verfügbaren Regelbuch-Bestand (`extracted_pages` bis Seite 211) gegen das Website-Backend in `characters/rules_data/` geprüft.

## Zusammenfassung der Ergebnisse

| Kategorie | Status | Korrektheit | Anmerkungen |
| :--- | :--- | :--- | :--- |
| **Spezies** | Geprüft | **Hoch** | Alle 10 Völker inkl. 2024-Updates korrekt. |
| **Hintergründe** | Geprüft | **Hoch** | Alle 16 Hintergründe (S. 178–185) stimmen exakt überein. |
| **Klassen** | Geprüft | **Mittel** | Mechanik korrekt, aber viele Namen abweichend (Beispiel: *Thaumaturg* vs *Gelehrter*). |
| **Zauber** | Geprüft | **Gering** | Viele Terminologie-Fehler und veraltete Schulen (Heilung als *Hervorrufung*). |
| **Ausrüstung** | Nicht geprüft | – | **Fehlt im Regelbuch** (ab Seite 212). |
| **Zauberbeschr.** | Nicht geprüft | – | **Fehlt im Regelbuch** (Kapitel 7 & 8 fehlen). |

## Detaillierte Befunde

### 1. Spezies & Hintergründe (Ausgezeichnet)
Das Backend ist hier bereits sehr gut auf dem Stand von 2024.
- **Drachenblütige** haben korrekt die neue Dunkelsicht (18m).
- **Orks** haben korrekt die verbesserte Dunkelsicht (36m).
- **Hintergründe** nutzen das neue 2024-System (+2/+1 Attribute, Talent auf Stufe 1).

### 2. Klassen-Merkmale (Korrekturbedarf)
Die Namen der Merkmale weichen oft von der deutschen Übersetzung ab:
- **Kleriker:** Das Backend nutzt "Gelehrter", das Regelbuch (S. 104) nutzt "**Thaumaturg**".
- **Kleriker:** Das Backend nutzt "Göttliches Scheitern", das Regelbuch nutzt "**Göttlicher Funke**".
- **Druide:** Das Backend nutzt "Urgestalt", das Regelbuch nutzt "**Tiergestalt**".

### 3. Zauber (Korrekturbedarf)
Dies ist die größte Baustelle.
- **Heilung:** `Heilendes Wort` und `Wunden heilen` müssen der Schule **Bannmagie** zugeordnet werden.
- **Namen:** Begriffe wie `Leitung` (Göttliche Führung), `True Strike` (Zielsicherer Schlag) und `Sorcerous Burst` (Explosion der Zauberei) müssen korrigiert werden.
- **Details:** Siehe separaten [spell_audit.md](file:///C:/DiceDock/docs/audit_2024/spell_audit.md).

## Fehlende Datenquellen
Das bereitgestellte Regelbuch (`extracted_pages`) endet in Kapitel 5 (Talente). Für eine vollständige Prüfung von Waffen-Eigenschaften (Kapitel 6) und detaillierten Zauber-Effekten (Kapitel 8) fehlen die entsprechenden Seiten.

## Empfohlene nächste Schritte
1.  **Terminologie-Patch**: Umbenennung der Zauber und Klassenmerkmale im Backend.
2.  **Schulen-Update**: Korrektur der Heil-Schulen.
3.  **Ergänzung**: Akquise der fehlenden Regelbuch-Kapitel für Waffen und Zauberdetails.
