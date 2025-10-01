from pathlib import Path

# Paths for project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Files
VENTAS_FILE = RAW_DATA_DIR / "ventas.csv"
