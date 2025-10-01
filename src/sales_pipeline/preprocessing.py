import pandas as pd


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean sales data:
    - Drop duplicates
    - Remove null values
    - Filter negative quantities
    - Convert 'fecha' to datetime
    - Add 'total' = cantidad * precio_unitario
    """
    df = df.drop_duplicates()
    df = df.dropna()

    if "cantidad" in df.columns:
        df = df[df["cantidad"] >= 0]

    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df = df.dropna(subset=["fecha"])

    if "cantidad" in df.columns and "precio_unitario" in df.columns:
        df["total"] = df["cantidad"] * df["precio_unitario"]

    return df
