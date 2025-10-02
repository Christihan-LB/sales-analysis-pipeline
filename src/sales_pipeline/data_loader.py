import pandas as pd
from ..config import VENTAS_FILE


def load_sales_data() -> pd.DataFrame:
    """
    Load the sales CSV file from data/raw.
    """
    try:
        df = pd.read_csv(VENTAS_FILE)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {VENTAS_FILE}")
