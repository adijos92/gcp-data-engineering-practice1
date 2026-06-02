filtered_df.write \
    .format("bigquery") \
    .option(
        "table",
        "sales_dataset.sales"
    ) \
    .save()