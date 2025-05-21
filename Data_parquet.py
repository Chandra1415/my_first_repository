import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'salary': [70000, 80000, 65000, 72000, 85000]
}

df = pd.DataFrame(data)
df.to_parquet('sample_data.parquet', index=False)
