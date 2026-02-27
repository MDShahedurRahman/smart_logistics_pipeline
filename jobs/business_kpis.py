from pyspark.sql.functions import sum, avg, desc
from config import GOLD_PATH, REPORT_PATH
from utils.helpers import ensure_dir


def run_kpi_job(spark):
    print("Generating KPIs...")
