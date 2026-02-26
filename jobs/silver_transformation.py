from pyspark.sql.functions import col, to_date, datediff
from config import BRONZE_PATH, SILVER_PATH
from utils.helpers import ensure_dir
from utils.validators import validate_positive_values


def run_silver_job(spark):
    print("Running Silver Transformation...")

    ensure_dir(SILVER_PATH)

    df = spark.read.parquet(BRONZE_PATH)

    df = validate_positive_values(df)

    transformed = (
        df.dropDuplicates(["shipment_id"])
        .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
        .withColumn("delivery_date", to_date(col("delivery_date"), "yyyy-MM-dd"))
        .withColumn("delivery_days",
                    datediff(col("delivery_date"), col("order_date")))
    )

    return transformed
