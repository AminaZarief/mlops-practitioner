import os

# Ensure project directories exist
os.makedirs('./data', exist_ok=True)
os.makedirs('./reports', exist_ok=True)
os.makedirs('./models', exist_ok=True)


print(os.getcwd())
parquet_path = './data/green_tripdata_2023-01.parquet'
report_path = './reports/module-1.md'
model_path = './models/baseline.pkl'