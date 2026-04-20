import io
import pandas as pd

def dataframe_to_excel_bytes(df: pd.DataFrame) -> bytes:
    """
    Convert DataFrame to Excel bytes for download.
    """
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()
