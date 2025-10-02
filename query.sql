SELECT producto, SUM(cantidad) as total_vendida
FROM ventas
GROUP BY producto
ORDER BY total_vendida DESC
LIMIT 3;