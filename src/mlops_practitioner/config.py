import os

from mlops_practitioner.settings import Settings

settings = Settings()
# Ensure project directories exist

os.makedirs(os.path.dirname(settings.model_path), exist_ok=True)
os.makedirs(os.path.dirname(settings.parquet_path),exist_ok=True)
os.makedirs(os.path.dirname(settings.report_path),exist_ok=True)




report_path = settings.report_path
parquet_path = settings.parquet_path
model_path = settings.model_path