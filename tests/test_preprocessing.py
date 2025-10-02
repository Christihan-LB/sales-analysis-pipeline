import pandas as pd
from src.sales_pipeline.preprocessing import clean_sales_data


def test_total_column_is_correct():
    df = pd.DataFrame({
        "fecha": ["2023-01-01"],
        "producto": ["TestProduct"],
        "cantidad": [2],
        "precio_unitario": [500]
    })

    df_clean = clean_sales_data(df)
    assert "total" in df_clean.columns
    assert df_clean["total"].iloc[0] == 1000
