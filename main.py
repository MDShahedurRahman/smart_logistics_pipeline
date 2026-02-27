from utils.spark_session import get_spark_session

from jobs.bronze_ingestion import run_bronze_job
from jobs.silver_transformation import run_silver_job
from jobs.sla_detection import run_sla_detection
from jobs.risk_scoring import run_risk_scoring
from jobs.gold_star_schema import run_gold_job
from jobs.business_kpis import run_kpi_job


def main():
    spark = get_spark_session()

    run_bronze_job(spark)


if __name__ == "__main__":
    main()
