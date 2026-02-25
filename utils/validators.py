from pyspark.sql.functions import col


def validate_positive_values(df):
    return df.filter(
        (col("weight_kg") > 0) &
        (col("shipping_cost") >= 0)
    )
