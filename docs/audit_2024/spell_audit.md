# Audit-Bericht: Zauber (D&D 2024)

Dieser Bericht dokumentiert die Diskrepanzen zwischen dem deutschen D&D 2024 Regelbuch und der Zauber-Implementierung in `characters/rules_data/zauber.py`.

## 1. Terminologie-Abweichungen (Deutsch 2024)

| Zauber (Regelbuch) | Zauber (Backend) | Status |
| :--- | :--- | :--- |
| **Göttliche Führung** | Leitung | **Falsch** |
| **Verschonung der Sterbenden** | Verschone die Toten | **Abweichend** |
| **Wort des Strahlens** | Wort des Glanzes | **Abweichend** |
| **Gehässiger Spott** | Boshafter Spott | **Abweichend** |
| **Zielsicherer Schlag** | True Strike | **Englisch** (Falsch) |
| **Explosion der Zauberei** | Sorcerous Burst | **Englisch** (Falsch) |
| **Elementalismus** | Elementarismus | **Abweichend** |
| **Heldenmut** | Heldentum | **Abweichend** |
| **Sternenfunke** | Sternenstaub | **Abweichend** |
| **Lange Schritte** | Langstricher | **Abweichend** |
| **Totenläuten** | Totenberührung | **Abweichend** |

## 2. Schulen-Änderungen (D&D 2024)
Die 2024 Edition ordnet viele Heilzauber der Schule **Bannmagie** zu.

- **Heilendes Wort:** Regelbuch: **Bannmagie**. Backend: *Hervorrufung*.
- **Wunden heilen:** Regelbuch: **Bannmagie**. Backend: *Hervorrufung*.
- **Massen-Heilendes Wort:** Regelbuch: **Bannmagie**. Backend: *Hervorrufung*.

## 3. Mechanische Unterschiede
- **Göttliche Führung (Guidance):** Das Backend implementiert dies als **Reaktion**. Das extrahierte Regelbuch (S. 96/98) listet es jedoch mit **K** (Konzentration). 
  - *Hinweis:* Auch wenn die PHB 2024 Final die Reaktion nutzt, weichen die vorliegenden deutschen Seiten davon ab.

## Empfehlung
Alle Zaubernamen und Schulen sollten an die offizielle deutsche 2024-Übersetzung angepasst werden.
