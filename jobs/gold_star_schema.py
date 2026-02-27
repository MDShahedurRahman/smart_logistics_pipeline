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

    fact_shipments = df.select(
        "shipment_id",
        "customer_id",
        "warehouse_id",
        "destination_city",
        "weight_kg",
        "shipping_cost",
        "delivery_days",
        "sla_breach",
        "risk_score"
    )

    dim_customer.write.mode("overwrite").parquet(GOLD_PATH + "dim_customer/")
    dim_warehouse.write.mode("overwrite").parquet(GOLD_PATH + "dim_warehouse/")
    fact_shipments.write.mode("overwrite").parquet(
        GOLD_PATH + "fact_shipments/")

    print("Gold Completed.")
