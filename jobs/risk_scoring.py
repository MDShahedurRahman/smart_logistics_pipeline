from pyspark.sql.functions import when, col
from config import SLA_PATH, RISK_PATH
from utils.helpers import ensure_dir


def run_risk_scoring(spark):
    print("Running Risk Scoring...")

    ensure_dir(RISK_PATH)

    df = spark.read.parquet(SLA_PATH)

    scored = df.withColumn(
        "risk_score"
    )

    return scored
