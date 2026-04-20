def parse_relation_from_line(line: str) -> str:
    """
    Infer relation (Father/Husband/Mother) from Punjabi/English hints in a line.
    """
    l = line.lower()

    # Punjabi / Hindi hints
    if "ਪਤਨੀ" in l or "wife" in l:
        return "Husband"
    if "ਪੁੱਤਰ" in l or "son of" in l:
        return "Father"
    if "ਬੇਟੀ" in l or "ਧੀ" in l or "daughter of" in l:
        return "Father"
    if "mother of" in l:
        return "Mother"

    return ""
