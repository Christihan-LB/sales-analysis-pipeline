import sqlite3
import pandas as pd
from .config import PROCESSED_DATA_DIR

DB_FILE = f"{PROCESSED_DATA_DIR}/ventas.db"


def save_to_db(df: pd.DataFrame, monthly: pd.DataFrame):
    """
    Save cleaned sales data and monthly revenue to SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    df.to_sql("ventas", conn, if_exists="replace", index=False)
    monthly.to_sql(
        "facturacion_mensual", conn, if_exists="replace", index=False
    )
    conn.commit()
    conn.close()


def get_top_products(limit=3):
    """
    Return SQL query to retrieve top N products by sales quantity.
    """
    query = f"""
    SELECT producto, SUM(cantidad) as total_vendida
    FROM ventas
    GROUP BY producto
    ORDER BY total_vendida DESC
    LIMIT {limit};
    """
    return query
