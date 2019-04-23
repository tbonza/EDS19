"""
Data preprocessing -- create a working table.

Need to join Commits, Meta, and Author to create a working
table for the PredictingRepoHealth analysis. Game plan is
to only validate the join in this script.

Turns out that Spark isn't the best for joins. Plan B.
"""
import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    outpath = "s3://ds6050-output/working_table.parquet"
    
    spark = SparkSession.builder.getOrCreate()
    spark.conf.set("spark.sql.cbo.enabled", "true")

    ## Load data
    
    authors = spark.read.format("parquet").load("s3://ds6050/author_2019-04-20_0.parquet")
    #commits = spark.read.format("parquet").load("s3://ds6050/commit_file_2019-04-20_0.parquet")
    meta = spark.read.format("parquet").load("s3://ds6050/meta_2019-04-20_0.parquet")

    ## Join dataframes

    # Meta to Authors (one to one); inner join is default

    joinExpression = meta['commit_hash'] == authors['commit_hash']
    metaAuthors = meta.join(authors, joinExpression)
    #metaAuthors = metaAuthors.repartition(1)

    # MetaAuthors to Commits (one to many)
    
    #joinType = "outer"
    #joinExpression = metaAuthors['commit_hash'] == commits['commit_hash']
    #metadf = metaAuthors.join(commits, joinExpression, joinType)

    ## Write out working_table

    #metadf.write.format("parquet").save(outpath)
    metaAuthors.repartition(5)\
        .write.format("parquet").save(outpath)








