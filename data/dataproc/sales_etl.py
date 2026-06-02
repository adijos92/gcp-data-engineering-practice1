from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "sales_etl"
).getOrCreate()

df = spark.read.csv(
    "gs://sales-data-bucket-demo/sales.csv",
    header=True
)

df.show()

filtered_df = df.filter(df.amount > 1500)

filtered_df.show()