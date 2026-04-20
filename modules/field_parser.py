import re

gender_map = {
    "ਇਸਤਰੀ": "Female",
    "ਪੁੱਰਸ਼": "Male",
    "Female": "Female",
    "Male": "Male",
}

def parse_code(block: str):
    """
    Parse AC/Part/Serial like 14/175/788 from block.
    """
    m = re.search(r'(\d{2})/(\d{3})/(\d+)', block)
    if not m:
        return None, None, None
    return m.group(1), m.group(2), m.group(3)

def parse_mc(block: str):
    m = re.search(r'(SDO|HZF)\w+', block)
    return m.group(0) if m else ""

def parse_house(block: str):
    m = re.search(r'ਘਰ ਨੰ[: ]+([0-9A-Za-z/]+)', block)
    if not m:
        m = re.search(r'House[: ]+([0-9A-Za-z/]+)', block, flags=re.IGNORECASE)
    return m.group(1) if m else ""

def parse_age(block: str):
    m = re.search(r'ਉਮਰ[: ]+(\d+)', block)
    if not m:
        m = re.search(r'Age[: ]+(\d+)', block, flags=re.IGNORECASE)
    return m.group(1) if m else ""

def parse_gender(block: str):
    m = re.search(r'ਲਿੰਗ[: ]+(\S+)', block)
    if not m:
        m = re.search(r'Gender[: ]+(\w+)', block, flags=re.IGNORECASE)
    if not m:
        return ""
    raw = m.group(1)
    return gender_map.get(raw, raw)

def parse_name_and_relative(block: str):
    """
    Very simple heuristic: after EPIC line, next lines are name and relative.
    You can refine this later with more samples.
    """
    lines = [l.strip() for l in block.split("\n") if l.strip()]
    # find EPIC line index
    epic_idx = None
    for i, line in enumerate(lines):
        if re.search(r'(SDO|HZF)\w+', line):
            epic_idx = i
            break

    name = ""
    relative = ""

    if epic_idx is not None:
        if epic_idx + 1 < len(lines):
            name = lines[epic_idx + 1]
        if epic_idx + 2 < len(lines):
            relative = lines[epic_idx + 2]

    return name, relative
