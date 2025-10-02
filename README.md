# 📊 Sales Analysis Project

## 📌 Overview
This project performs a **sales analysis** using Python, including data cleaning, exploratory analysis, database persistence, visualization, and automated testing.  

The dataset provided is located in [`data/raw/ventas.csv`](data/raw/ventas.csv) with the following columns:  

- `fecha` — Date of the sale  
- `producto` — Product name  
- `cantidad` — Quantity sold  
- `precio_unitario` — Price per unit  

---

## ✨ Features
- ✅ Data loading and cleaning (removes nulls and invalid rows).  
- ✅ Adds new column `total = cantidad * precio_unitario`.  
- ✅ Analysis:
  - Most sold product by quantity.  
  - Product with the highest total revenue.  
  - Monthly total revenue.  
- ✅ Persistence in **SQLite** database (`data/processed/sales.db`).  
- ✅ SQL query example to get **Top 3 most sold products**.  
- ✅ Visualization of monthly revenue (`data/processed/grafico.png`).  
- ✅ Automated test with **pytest** for the calculation of `total`.  

---

## 🚀 Execution Options

You can run this project in **two different ways**:

### 🔹 Option 1 — Local environment (venv / Conda)
See detailed steps in [docs/execution_local.md](docs/execution_local.md).  

Quick start:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run analysis
python -m src.main
```
### 🔹 Option 2 — Docker

See detailed steps in docs/execution_docker.md.

Quick start:
```bash
docker build -t sales-analysis .
docker run --rm -v $(pwd)/data:/app/data sales-analysis
```

⸻

## 📊 Results
-	Database: data/processed/sales.db
-	Graph: data/processed/grafico.png

Example SQL query for the Top 3 most sold products (see docs/database.md and also in query.sql file):
```sql
SELECT producto, SUM(cantidad) as total_vendida
FROM ventas
GROUP BY producto
ORDER BY total_vendida DESC
LIMIT 3;
```
To connect to the database run the following command:
```bash
sqlite3 data/processed/ventas.db
```
⸻

## 🧪 Testing

See docs/testing.md for full instructions.

Run all tests with:
```bash
pytest
```

⸻

📂 Project Structure
```
sales-analysis/
├── data/
│   ├── raw/            # Input CSV file(s)
│   │   └── ventas.csv
│   └── processed/      # Database and generated graphics
├── docs/               # Extended documentation
│   ├── index.md
│   ├── execution_local.md
│   ├── execution_docker.md
│   ├── database.md
│   └── testing.md
├── src/                # Source code
│   ├── sales_pipeline/
│   │   └── __init__.py
│   │   └── data_loader.py
│   │   └── preprocessing.py
│   │   └── analysis.py
│   │   └── db.py
│   │   └── visualization.py
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── tests/              # Unit tests
│   ├── __init__.py
│   └── test_processing.py
├── Dockerfile
├── docker-compose.yml
├── environment.yml
├── requirements.txt
├── pytest.ini
├── README.md
├── LICENSE
└── query.sql
```

⸻

## 📖 Extended Documentation

For detailed guides, see the docs/ folder:
-	Execution with venv/Conda
-	Execution with Docker
-	Database usage
-	Testing guide
