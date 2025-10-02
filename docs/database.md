# Database Usage

The project saves analysis results in an SQLite database located at:

data/processed/sales.db

## Example queries

### Top 3 most sold products
```sql
SELECT producto, SUM(cantidad) as total_vendida
FROM ventas
GROUP BY producto
ORDER BY total_vendida DESC
LIMIT 3;
```

### Total monthly revenue
```sql
SELECT strftime('%Y-%m', fecha) AS mes,
       SUM(total) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY mes;
```