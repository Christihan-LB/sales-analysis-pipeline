# Testing Guide

## Run all tests
```bash
pytest
```
Run with detailed output

```bash
pytest -v
```

What is tested?
-	Calculation of the total column (cantidad * precio_unitario).
-	Ensuring data cleaning removes invalid rows (e.g., negative quantities).