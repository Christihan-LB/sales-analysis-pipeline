from .sales_pipeline.data_loader import load_sales_data
from .sales_pipeline.preprocessing import clean_sales_data
from .sales_pipeline.analysis import product_most_sold, product_highest_revenue, revenue_per_month   # noqa: E501
from .sales_pipeline.db import save_to_db, get_top_products
from .sales_pipeline.visualization import plot_revenue_per_month


def main():
    # 1. Load data
    df = load_sales_data()
    print(f"Loaded rows: {df.shape[0]}")

    # 2. Clean data
    df_clean = clean_sales_data(df)
    print(f"Cleaned rows: {df_clean.shape[0]}")

    # 3. Analysis
    top_product = product_most_sold(df_clean)
    top_revenue = product_highest_revenue(df_clean)
    monthly = revenue_per_month(df_clean)

    print(f"Most sold product: {top_product}")
    print(f"Highest revenue product: {top_revenue}")
    print("Monthly revenue:")
    print(monthly)

    # 4. DB persistence
    save_to_db(df_clean, monthly)
    print("Data saved in SQLite (data/processed/ventas.db)")

    print("SQL query for top 3 products:")
    print(get_top_products(3))

    # 5. Visualization
    output_file = plot_revenue_per_month(monthly)
    print(f"Chart saved to: {output_file}")


if __name__ == "__main__":
    main()
