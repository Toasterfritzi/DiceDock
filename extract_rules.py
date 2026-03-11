import fitz

def extract_text(pdf_path, output_txt):
    try:
        doc = fitz.open(pdf_path)
        pages_text = [
            f"--- PAGE {page_num + 1} ---\n{page.get_text()}\n"
            for page_num, page in enumerate(doc)
        ]
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.writelines(pages_text)
        print(f"Successfully extracted text to {output_txt}")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except fitz.FileDataError as e:
        print(f"Error: Invalid PDF file - {e}")
    except OSError as e:
        print(f"Error: OS error occurred - {e}")

if __name__ == "__main__":
    extract_text('D-D - Spielregeln_compressed.pdf', 'full_rules.txt')