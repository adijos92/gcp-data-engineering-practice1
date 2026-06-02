from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("orders_etl").getOrCreate()

df = spark.read.csv(
    "gs://orders-landing-bucket-demo/orders.csv",
    header=True,
    inferSchema=True
)

print("Original Orders:")
df.show()

filtered_df = df.filter(col("amount") > 5000)

print("Orders above 5000:")
filtered_df.show()