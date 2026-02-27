from config import RISK_PATH, GOLD_PATH
from utils.helpers import ensure_dir


def run_gold_job(spark):
    print("Running Gold Layer...")

    ensure_dir(GOLD_PATH)

    df = spark.read.parquet(RISK_PATH)

    dim_customer = df.select("customer_id").dropDuplicates()

    dim_warehouse = df.select(
        "warehouse_id",
        "origin_city"
    ).dropDuplicates()
