from .block_splitter import split_blocks
from .field_parser import (
    parse_code,
    parse_mc,
    parse_house,
    parse_age,
    parse_gender,
    parse_name_and_relative,
)
from .relation_parser import parse_relation_from_line

def build_rows_from_pages(pages_text, ac_no: str, part_no: str):
    """
    Build structured rows from all pages of a Part PDF.
    """
    rows = []

    for page_text in pages_text:
        blocks = split_blocks(page_text)
        for block in blocks:
            ac, part, serial = parse_code(block)

            # If code not found in block, fall back to provided AC/Part
            if not ac:
                ac = ac_no
            if not part:
                part = part_no

            name, relative = parse_name_and_relative(block)
            mc = parse_mc(block)
            house = parse_house(block)
            age = parse_age(block)
            gender = parse_gender(block)

            # Relation: try from name/relative lines
            relation = ""
            if name:
                relation = parse_relation_from_line(name)
            if not relation and relative:
                relation = parse_relation_from_line(relative)

            if not serial:
                # if serial not found, we still keep row but serial blank
                serial = ""

            if not mc and not name:
                # skip empty garbage blocks
                continue

            rows.append({
                "AC-No": ac,
                "Part No": part,
                "Sr No in Part No": serial,
                "Name": name,
                "Relative": relative,
                "Relation": relation,
                "House": house,
                "Age": age,
                "Gender": gender,
                "MC No": mc,
            })

    return rows
