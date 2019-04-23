"""
Make sure we can do a basic count and write out the results.

Reference:
  https://spark.apache.org/examples.html
"""
import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    outpath = "s3://ds6050-output/counts_by_name_example.parquet"

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("parquet")\
        .load("s3://ds6050/author_2019-04-20_0.parquet")\

    countsByName = df.groupby('name').count()
    countsByName.write.format("parquet").save(outpath)

