# DiceDock Agent Instructions (AGENTS.md)

Welcome, Agent! This file contains important guidelines and architectural context for working on the DiceDock project. Please read and adhere to these rules when interacting with the codebase.

## 1. Project Overview & Environment

*   **Project:** DiceDock, a Django 5.2.11 web application for D&D 5e character management.
*   **Database:** `django.db.backends.sqlite3`
*   **Python Version:** Python 3.12.12 (managed via pyenv).
*   **Network Restriction:** The development sandbox has **restricted network access**. `pip install` cannot download packages from external repositories. Do not try to install external packages unless they are available locally or explicitly requested. Use `pip install -r requirements.txt` if needed, but be aware of the restriction.
*   **Setup:** A `build.sh` script automates environment setup, including dependency installation, static asset collection (`collectstatic`), and database migrations.

## 2. Testing

*   **Test Command:** ALWAYS run tests using:
    `SECRET_KEY=dummy DEBUG=True python manage.py test`
*   **Important Note on `DEBUG=True`:** Setting `DEBUG=True` is **required** during testing to prevent `SECURE_SSL_REDIRECT` from causing `302 -> 301` redirect assertion failures.
*   **Test Locations:**
    *   Unit tests for the `characters` app are in `characters/tests.py` (e.g., `CharacterCreationTest`, `UserRegisterFormTest`, `CharacterModelTest`, `CharacterLevelupTest`, `DashboardViewTest`, `ASILogicTest`).
    *   Security and environment variable tests (like parsing `ALLOWED_HOSTS`) are in `characters/tests_security.py`.
*   **Form Validation Testing:** When testing password mismatches in forms (like `UserRegisterForm`), verify using `form.non_field_errors()` as errors are raised as non-field `ValidationError`s in the `clean()` method.

## 3. Architecture & Code Patterns

*   **Imports:** Organize Python imports according to PEP 8 (Standard library, third-party, then local; alphabetized).
*   **Database Optimizations:**
    *   Use `.only()` to restrict database fetching to essential fields when querying models (e.g., in the `dashboard` view: `id`, `name`, `level`, `image`, `race`, `character_class`, `current_hp`, `max_hp`). Avoid loading heavy text and JSON fields unnecessarily.
    *   Avoid redundant `.exists()` checks before `.get()`. Just use `.get()` and catch the `ObjectDoesNotExist` exception to reduce query overhead.
    *   Persistent DB connections are enabled (`CONN_MAX_AGE=600`, `CONN_HEALTH_CHECKS=True`). Scripts like `benchmark_db.py` and `test_db.py` are available for testing connection latency and performance.
*   **Models:**
    *   The `Character` model uses `JSONField` to store `inventory`, `weapons`, `proficiencies`, and `spell_slots`.
    *   Ability modifiers (e.g., `strength_mod`) are calculated dynamically via `@property` methods using the D&D 5e formula: `(score - 10) // 2`.
*   **Business Logic:**
    *   **Leveling:** `character.experience` must strictly be checked against `character.max_experience` before allowing a level up increment.
    *   **ASI Levels:** The `_get_asi_levels` function determines Ability Score Improvement levels using case-insensitive substring matching for classes like 'fighter'/'kämpfer' and 'rogue'/'schurke'.
    *   **Backgrounds:** The 'Soldier' background grants a +2 Strength bonus and sets starting Gold to 0.
*   **AJAX:** Endpoints (like `update_character_stat`) process JSON payloads parsed via `json.loads(request.body)` and return `JsonResponse` objects.

## 4. Security & Configuration

*   **Secrets & Settings:**
    *   `SECRET_KEY` is loaded from the environment and must be explicitly set (raises `ImproperlyConfigured` otherwise).
    *   `ALLOWED_HOSTS` is parsed from a comma-separated environment variable (handling whitespace and empty strings) and automatically appends `RENDER_EXTERNAL_HOSTNAME` for Render deployments.
    *   `DEBUG` mode is dynamically controlled by the `RENDER` environment variable (True locally, False in Render).
*   **Cookies & HTTPS:** Session and CSRF cookies are strictly configured with `SECURE=True`, `HTTPONLY=True`, and `SAMESITE='Lax'`. `SECURE_PROXY_SSL_HEADER` and `SECURE_SSL_REDIRECT = not DEBUG` are used.
*   **Authentication:** Django's built-in password validators are enabled.

## 5. Frontend & UI

*   **Language:** The project documentation (`README.md`) and presumably the UI text target German-speaking end-users (players).
*   **Styling:** Tailwind CSS is used via CDN. The design system features a dark-mode, neon, and glassmorphism aesthetic.
*   **Notifications:** The Django `messages` framework is used for UI notifications. These are rendered as fixed top-right glassmorphism toasts in `characters/templates/characters/base.html` and styled with Tailwind CSS (handling tags like 'error' and 'success').
*   **Images:** `Pillow` is required for handling image uploads.
*   **Static Files:** GZip compression is enabled (`django.middleware.gzip.GZipMiddleware`), positioned explicitly after `WhiteNoiseMiddleware` for optimal static file serving.
