import unittest
from unittest.mock import patch, mock_open, MagicMock
import fitz
from extract_rules import extract_text
import os

class TestExtractRules(unittest.TestCase):

    @patch('extract_rules.fitz.open')
    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_extract_text_success(self, mock_print, mock_file, mock_fitz_open):
        # Setup mock doc
        mock_doc = MagicMock()
        mock_page1 = MagicMock()
        mock_page1.get_text.return_value = "Page 1 Text"
        mock_page2 = MagicMock()
        mock_page2.get_text.return_value = "Page 2 Text"

        # Make the mock doc iterable like a list of pages
        mock_doc.__iter__.return_value = iter([mock_page1, mock_page2])

        mock_fitz_open.return_value = mock_doc

        extract_text('dummy.pdf', 'output.txt')

        mock_fitz_open.assert_called_once_with('dummy.pdf')
        mock_file.assert_called_once_with('output.txt', 'w', encoding='utf-8')

        # Check what was written
        handle = mock_file()
        handle.writelines.assert_called_once()
        args = handle.writelines.call_args[0][0]

        self.assertEqual(len(args), 2)
        self.assertEqual(args[0], "--- PAGE 1 ---\nPage 1 Text\n")
        self.assertEqual(args[1], "--- PAGE 2 ---\nPage 2 Text\n")

        mock_print.assert_called_once_with("Successfully extracted text to output.txt")

    @patch('extract_rules.fitz.open')
    @patch('builtins.print')
    def test_extract_text_file_not_found(self, mock_print, mock_fitz_open):
        mock_fitz_open.side_effect = FileNotFoundError("File dummy.pdf not found")

        extract_text('dummy.pdf', 'output.txt')

        mock_print.assert_called_once()
        self.assertIn("Error: File not found", mock_print.call_args[0][0])

    @patch('extract_rules.fitz.open')
    @patch('builtins.print')
    def test_extract_text_file_data_error(self, mock_print, mock_fitz_open):
        mock_fitz_open.side_effect = fitz.FileDataError("Invalid PDF")

        extract_text('dummy.pdf', 'output.txt')

        mock_print.assert_called_once()
        self.assertIn("Error: Invalid PDF file", mock_print.call_args[0][0])

    @patch('extract_rules.fitz.open')
    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_extract_text_os_error_on_write(self, mock_print, mock_file, mock_fitz_open):
        mock_doc = MagicMock()
        mock_doc.__iter__.return_value = iter([])
        mock_fitz_open.return_value = mock_doc

        mock_file.side_effect = OSError("Disk full")

        extract_text('dummy.pdf', 'output.txt')

        mock_print.assert_called_once()
        self.assertIn("Error: OS error occurred", mock_print.call_args[0][0])

if __name__ == '__main__':
    unittest.main()
