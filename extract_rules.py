import fitz
import sys

def extract_text(pdf_path, output_txt):
    try:
        doc = fitz.open(pdf_path)
        with open(output_txt, 'w', encoding='utf-8') as f:
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                f.write(f"--- PAGE {page_num + 1} ---\n")
                f.write(text)
                f.write("\n")
        print(f"Successfully extracted text to {output_txt}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text('D-D - Spielregeln_compressed.pdf', 'full_rules.txt')
