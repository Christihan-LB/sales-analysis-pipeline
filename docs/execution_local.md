# Execution Guide - Local Environment (venv / Conda)

## 1. Setup with Python virtual environment (venv)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## 2. Setup with Conda

```bash
conda create -n sales_analysis python=3.11 -y
conda activate sales_analysis
pip install -r requirements.txt
```
## 3. Run the analysis

```bash
python src/main.py
```

-	This will:
-	Load and clean the data.
-	Perform the analysis.
-	Save results into the database data/processed/sales.db.
-	Generate the plot data/processed/grafico.png.
