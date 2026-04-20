import re
from .text_cleaner import normalize_whitespace

EPIC_PATTERN = r'(SDO|HZF)\w+'

def split_blocks(page_text: str):
    """
    Split a page into voter blocks using EPIC IDs as anchors.
    """
    text = normalize_whitespace(page_text)
    parts = re.split(rf'(?={EPIC_PATTERN})', text)

    blocks = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if re.search(EPIC_PATTERN, part):
            blocks.append(part)
    return blocks
