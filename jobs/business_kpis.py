from pyspark.sql.functions import sum, avg, desc
from config import GOLD_PATH, REPORT_PATH
from utils.helpers import ensure_dir


def run_kpi_job(spark):
    print("Generating KPIs...")

    ensure_dir(REPORT_PATH)

    fact = spark.read.parquet(GOLD_PATH + "fact_shipments/")

    revenue = (
        fact.groupBy("destination_city")
        .agg(sum("shipping_cost").alias("total_revenue"))
        .orderBy(desc("total_revenue"))
    )

    avg_delivery = (
        fact.groupBy("destination_city")
        .agg(avg("delivery_days").alias("avg_delivery_days"))
    )

    revenue.show()
    avg_delivery.show()

    revenue.write.mode("overwrite").csv(
        REPORT_PATH + "revenue_by_city/",
        header=True
    )
