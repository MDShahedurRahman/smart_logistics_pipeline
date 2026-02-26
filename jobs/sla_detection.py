from pyspark.sql.functions import when, col
from config import SILVER_PATH, SLA_PATH, SLA_THRESHOLD_DAYS
from utils.helpers import ensure_dir


def run_sla_detection(spark):
    print("Running SLA Detection...")

    ensure_dir(SLA_PATH)

    df = spark.read.parquet(SILVER_PATH)

    flagged = df.withColumn(
        "sla_breach",
        when(col("delivery_days") > SLA_THRESHOLD_DAYS, "BREACH")
    )

    return flagged
