import fitz
import sys

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
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text('D-D - Spielregeln_compressed.pdf', 'full_rules.txt')
