import matplotlib.pyplot as plt
import pandas as pd
from .config import PROCESSED_DATA_DIR


def plot_revenue_per_month(monthly: pd.DataFrame):
    """
    Generate bar chart of monthly revenue and save as PNG.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(monthly["mes"], monthly["total"], color="skyblue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.title("Monthly Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    output_file = f"{PROCESSED_DATA_DIR}/grafico.png"
    plt.savefig(output_file)
    plt.close()
    return output_file
