from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings — values come from env vars (MLOPS_*) or defaults."""

    parquet_path: str = "./data/green_tripdata_2023-01.parquet"
    model_path: str = "./models/baseline.pkl"
    report_path: str = "./reports/module-1.md"

    model_config = {"env_prefix": "MLOPS_"}
