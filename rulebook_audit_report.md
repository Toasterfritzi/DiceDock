# Audit Report: D&D 2024 Rulebook vs. DiceDock Codebase

This report documents the discrepancies between the transcribed German D&D 2024 rulebook and the current implementation in the DiceDock codebase (`characters/rules_data/`).

## 1. Systemic Discrepancies

### Background Attribute System
- **Rulebook:** Each background provides a set of **three** attributes. Players choose either (+2 / +1) or (+1 / +1 / +1) among these three.
- **Codebase:** Backgrounds are hardcoded with a `primary` and `secondary` attribute, effectively limiting players to two specific attributes.
- **Impact:** Significant loss of flexibility and non-compliance with 2024 character creation rules.

### Feature Scaling
- **Bardische Inspiration:** Code uses `Übungsbonus` for uses per day. Rulebook explicitly states `Charismamodifikator`.
- **Ork Dunkelsicht:** Code has 18m. Rulebook has **36m**.
- **Zwerg Dunkelsicht:** Rulebook has 36m (Code is correct here, but this is a change from 5e).

## 2. Species Audit (Kapitel 4)

| Species | Code Status | Discrepancies / Gaps |
| :--- | :--- | :--- |
| **Aasimar** | Inaccurate | Terminology mismatches (`Lichtträger` vs `Lichtbringer`). Missing sub-choices for `Celestische Offenbarung`. |
| **Drachenblütiger** | Inaccurate | Name mismatch (`Drachenblütiger` vs `Drachenblütler`). Missing `Dunkelsicht`. |
| **Elf** | Inaccurate | Skill proficiency is forced to `Wahrnehmung` (Rulebook allows choice of three). Missing multiple sub-species spells (*Feenfeuer*, *Magie entdecken*, etc.). |
| **Gnom** | Inaccurate | Felsengnom clockwork mechanics are vague and missing required cantrips. Waldgnom talk-to-animal trait is too generic. |
| **Goliath** | **Incorrect** | Speed mismatch (9m in code vs **10,5m** in book). Missing Level 5 transformation (`Große Gestalt`). Missing 2024 ancestor choices (Riesische Abstammung). |
| **Halbling** | Mostly Correct | Sub-species (Starkherz/Leichtfuß) features from 5e are **absent** from the 2024 base features (Matches rulebook, but code might still have 5e sub-races). |
| **Mensch** | Inaccurate | Missing 'Klein' size option. Trait name `Einfallsreich` vs `Inspirierende Gegenwart`. |
| **Ork** | Inaccurate | Dunkelsicht is 18m in code (should be 36m). Code includes `Große Statur` which is not in the 2024 rulebook for Orks. |
| **Zwerg** | Mostly Correct | Terminology: `Zwergische Unverwüstlichkeit` vs `Zwergen-Resistenz`. |

## 3. Background Audit (Kapitel 4)

| Background | Code Status | Discrepancies / Gaps |
| :--- | :--- | :--- |
| **Adeliger** | Inaccurate | Missing Intelligence as attribute option. |
| **Akolyth** | Inaccurate | Missing Charisma as attribute option. Talent name mismatch. |
| **Bauer** | **Incorrect** | Mismatched Talent (`Zäh` vs `Robust`). Mismatched Tool (specific vs generic). |
| **Einsiedler** | **CRITICAL** | Mismatched Talent! Rulebook says **`Heiler`**, Code says **`Magie-Adept`**. |
| **Händler** | **Incorrect** | Mismatched Skill (`Mit Tieren umgehen` vs `Motiv erkennen`). |
| **Handwerker** | **Incorrect** | Mismatched Talent (`Handwerker` vs `Robust`). |
| **Krimineller** | **Incorrect** | Mismatched Skill (`Fingerfertigkeit` vs `Täuschung`). |
| **Reisender** | **Incorrect** | Mismatched Tool (`Diebeswerkzeug` vs `Navigationsbesteck`). |
| **Wegfinder** | **CRITICAL** | Mismatched Talent! Rulebook says **`Eingeweihter der Magie`**, Code says **`Glückspilz`**. Mismatched Skills. |

## 4. Class Audit (Early Levels)

- **Barde**:
    - **Bardische Inspiration**: Uses are based on Charisma-Mod in the book, but Übungsbonus in the code.
    - **Zauber**: Rulebook provides lists of "Recommended Spells" which are not reflected in the code's defaults.
- **Paladin**:
    - Generally matches, but terminology like `Waffenmeisterung` (Level 1) is a 2024 addition that is correctly present but might need detail verification.

## 5. Talents Audit (Summary)

- **Terminology**: A pervasive mismatch between 2024 names and older/placeholder names:
    - `Zäh` vs `Robust`
    - `Eingeweihter der Magie` vs `Magie-Adept`
    - `Wilder Angreifer` vs `Robust` (for Soldier)
- **New Talents**: Most talents from Pages 200-211 (Epische Gaben, Kampfstile, Herkunftstalente) are **entirely missing** from the rules data files.

## Conclusion

The codebase is currently in a state that reflects a mix of D&D 5e (2014) rules, playtest rules, and early 2024 drafts. It requires significant updates to match the final German 2024 rulebook, especially regarding Background choices, Species trait ranges (Dunkelsicht), and the expanded Talent system.
