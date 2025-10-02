import pandas as pd


def product_most_sold(df: pd.DataFrame) -> str:
    """
    Return product with highest quantity sold.
    """
    return df.groupby("producto")["cantidad"].sum().idxmax()


def product_highest_revenue(df: pd.DataFrame) -> str:
    """
    Return product with highest revenue.
    """
    return df.groupby("producto")["total"].sum().idxmax()


def revenue_per_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return DataFrame with monthly revenue totals.
    """
    df_to_group = df.copy()
    df_to_group["mes"] = df_to_group["fecha"].dt.to_period("M")
    monthly = df_to_group.groupby("mes")["total"].sum().reset_index()
    monthly["mes"] = monthly["mes"].astype(str)
    return monthly
