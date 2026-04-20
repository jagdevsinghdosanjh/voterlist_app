import re

def detect_part_from_filename(filename: str) -> str:
    """
    Extract a 3-digit part number from filename, e.g. 175 from '14_175.pdf'.
    """
    m = re.search(r'(\d{3})', filename)
    return m.group(1) if m else ""
