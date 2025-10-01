# Execution Guide - Docker

## 1. Build the image
```bash
docker build -t sales-analysis .
```

## 2. Run the container

```bash
docker run --rm -v $(pwd)/data:/app/data sales-analysis
```

-	The container will:
-	Process the CSV file from data/raw/ventas.csv.
-	Save analysis results into data/processed/sales.db.
-	Generate the plot at data/processed/grafico.png.
