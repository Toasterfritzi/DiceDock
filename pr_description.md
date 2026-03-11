🎯 **What:** The code health issue addressed
Appended `# noqa: E800` to a comment in `characters/image_utils.py` to suppress a false positive where linter tools like `flake8-eradicate` incorrectly flagged valid documentation as commented-out code.

💡 **Why:** How this improves maintainability
This fixes a false linter positive, ensuring that valid comments that explain "why" (in this case, why 512x512 is used) are preserved, while also maintaining clean CI/CD checks.

✅ **Verification:** How you confirmed the change is safe
Ran `flake8` and `eradicate` manually, which both previously flagged the code. Verified that `# noqa: E800` resolves the issue. Ran the full `python manage.py test` suite to ensure no syntax errors or functionality breakages.

✨ **Result:** The improvement achieved
The codebase is now clean of false linter warnings in `image_utils.py` without losing valuable code context documentation.
