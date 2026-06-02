last_load_date = "2026-01-01"

query = f"""
SELECT *
FROM sales
WHERE updated_date > '{last_load_date}'
"""