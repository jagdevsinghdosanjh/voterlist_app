import io
import streamlit as st
import pandas as pd

from modules.pdf_reader import extract_pages
from modules.part_detector import detect_part_from_filename
from modules.row_builder import build_rows_from_pages
from modules.ward_merger import merge_parts
from modules.excel_writer import dataframe_to_excel_bytes

st.set_page_config(page_title="Voter List → Excel", layout="wide")

st.title("Voter List → Excel Generator")

st.markdown("Upload **one or more Part PDFs** for a Ward (e.g., 14/175, 14/176, 14/185...).")

uploaded_files = st.file_uploader(
    "Upload Part PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

ac_no = st.text_input("AC Number", value="14")

if uploaded_files and ac_no:
    all_dfs = []

    for file in uploaded_files:
        st.write(f"Processing: **{file.name}**")
        part_no = detect_part_from_filename(file.name)

        pages_text = extract_pages(file)
        rows = build_rows_from_pages(pages_text, ac_no=ac_no, part_no=part_no)

        if not rows:
            st.warning(f"No rows parsed from {file.name}")
            continue

        df = pd.DataFrame(rows)
        all_dfs.append(df)

        st.write(f"Preview for Part {part_no}:")
        st.dataframe(df.head())

    if all_dfs:
        ward_df = merge_parts(all_dfs)
        ward_df.insert(0, "Sr.No in Ward No", range(1, len(ward_df) + 1))

        st.subheader("Combined Ward Data")
        st.dataframe(ward_df.head(100))

        excel_bytes = dataframe_to_excel_bytes(ward_df)

        st.download_button(
            label="Download Ward Excel",
            data=excel_bytes,
            file_name="ward_voters.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.error("No data extracted from the uploaded PDFs.")
