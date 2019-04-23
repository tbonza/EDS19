""" 
Read parquet file and write an output.
"""
import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    outpath = "s3://ds6050-output/author_count_example.parquet"

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("parquet")\
        .load("s3://ds6050/author_2019-04-20_0.parquet")\

    df.write.format("parquet").save(outpath)

