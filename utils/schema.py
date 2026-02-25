from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType,
    DoubleType
)


def shipment_schema():
    return StructType([
        StructField("shipment_id", IntegerType(), True),
        StructField("customer_id", StringType(), True),
        StructField("warehouse_id", StringType(), True),
        StructField("origin_city", StringType(), True),
        StructField("destination_city", StringType(), True),
        StructField("weight_kg", DoubleType(), True),
        StructField("shipping_cost", DoubleType(), True),
        StructField("order_date", StringType(), True),
        StructField("delivery_date", StringType(), True),
        StructField("status", StringType(), True)
    ])
