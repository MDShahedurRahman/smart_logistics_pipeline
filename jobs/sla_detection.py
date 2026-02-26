from pyspark.sql.functions import when, col
from config import SILVER_PATH, SLA_PATH, SLA_THRESHOLD_DAYS
from utils.helpers import ensure_dir


def run_sla_detection(spark):

    return flagged
