🧪 [testing improvement] Add unit tests for extract_rules.py

🎯 **What:**
The `extract_text` function in `extract_rules.py` was previously untested. This PR introduces a new test file, `test_extract_rules.py`, that leverages `unittest.mock` to fully isolate the function from file system operations and the PyMuPDF (`fitz`) external dependency.

📊 **Coverage:**
*   **Happy Path:** Verifies that a valid PDF object is iterated correctly, formatting the output properly, writing it to the specified file handle, and printing a success message.
*   **Error Paths:** Tests all three exception handlers correctly by simulating their failure triggers:
    *   `FileNotFoundError`: Simulated when `fitz.open()` cannot find the file.
    *   `fitz.FileDataError`: Simulated when `fitz.open()` encounters an invalid PDF format.
    *   `OSError`: Simulated when the OS write operation fails (e.g., due to a full disk or lack of permissions).

✨ **Result:**
The `extract_rules.py` text extraction script is now fully tested with deterministic tests that require no external dummy files to execute, dramatically improving the project's overall test reliability and coverage.
