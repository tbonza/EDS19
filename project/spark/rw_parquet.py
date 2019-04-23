""" 
Read parquet file and write an output.
"""
from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("parquet")\
        .load("s3://ds6050/author_2019-04-20_0.parquet")

    result = df.groupby('name').count().take(25)

    result.write.format("parquet").mode("overwrite")\
        .save("s3://ds6050-output/author_count_example.parquet")
