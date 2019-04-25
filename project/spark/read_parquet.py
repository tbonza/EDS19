""" 
Read some parquet files from an S3 bucket
"""
from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("parquet")\
        .load("s3://ds6050/author_2019-04-20_0.parquet")

    print(df.count())

