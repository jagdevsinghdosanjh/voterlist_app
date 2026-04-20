import pdfplumber

def extract_pages(pdf_file):
    """
    Returns a list of text strings, one per page.
    """
    pages_text = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            pages_text.append(text)
    return pages_text
