from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "orders_etl"
).getOrCreate()

df = spark.read.csv(
    "gs://orders-landing-bucket-demo/orders.csv",
    header=True
)

df.show()