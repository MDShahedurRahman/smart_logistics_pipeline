from pyspark.sql.functions import col, to_date, datediff
from config import BRONZE_PATH, SILVER_PATH
from utils.helpers import ensure_dir
from utils.validators import validate_positive_values


def run_silver_job(spark):

    return transformed
