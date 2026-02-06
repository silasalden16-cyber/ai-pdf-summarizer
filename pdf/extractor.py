import fitz  # PyMuPDF
from typing import List, Dict
import pymupdf4llm

def extract_content(pdf_path: str):
    # This preserves tables and headers as Markdown
    md_text = pymupdf4llm.to_markdown(pdf_path)
    return md_text

def extract_text_by_page(pdf_path: str) -> List[Dict]:
    """
    Extract text from a PDF file page by page.

    Returns:
        A list of dictionaries:
        [
            {"page": 1, "text": "..."},
            {"page": 2, "text": "..."}
        ]
    """
    doc = fitz.open(pdf_path)
    pages = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        text = page.get_text()

        cleaned_text = text.strip()

        if cleaned_text:  # skip empty pages
            pages.append({
                "page": page_index + 1,
                "text": cleaned_text
            })

    doc.close()
    return pages