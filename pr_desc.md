🎯 **What:** The `_get_builder_json_data` function in `characters/views.py` was too complex and lengthy, building `klassen_json`, `hintergruende_json`, and `spezies_json` all inline within one function. I split these out into three smaller helper functions (`_format_klassen_data`, `_format_hintergruende_data`, and `_format_spezies_data`).

💡 **Why:** Splitting this function into separate pieces dramatically improves code readability and maintainability. These helper functions do not depend on each other and they make `_get_builder_json_data` much cleaner. The `@functools.lru_cache(maxsize=1)` caching remains on the top-level method to ensure no loss of performance.

✅ **Verification:** Verified the code health fix visually using `git diff`, and verified there are no syntax errors via `python -m py_compile`. Finally, I ran the full Django test suite (`SECRET_KEY=dummy DEBUG=True python manage.py test`), which completed successfully with no broken logic.

✨ **Result:** Improved modularity and readability by abstracting generation details into purpose-specific functions while preserving caching and logical behavior.
