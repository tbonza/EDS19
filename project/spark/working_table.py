"""
Data preprocessing -- create a working table.

Need to join Commits, Meta, and Author to create a working
table for the PredictingRepoHealth analysis. Game plan is
to only validate the join in this script.
"""
import sys

from pyspark.sql import SparkSession


if __name__ == "__main__":

    outpath = "s3://ds6050-output/working_table.parquet"
    inpaths = {
        "author": "s3://ds6050/author_2019-04-20_0.parquet",
        "commit_file": "s3://ds6050/commit_file_2019-04-20_0.parquet",
        "meta": "s3://ds6050/meta_2019-04-20_0.parquet",
    }
    
    spark = SparkSession.builder.getOrCreate()

    ## Load data
    
    authors = spark.read.format("parquet").load(inpaths['author'])
    commits = spark.read.format("parquet").load(inpaths['commit_file'])
    meta = spark.read.format("parquet").load(inpaths['meta'])

    ## Join dataframes

    # Meta to Authors (one to one)

    joinType = "left_outer"
    joinExpression = meta['commit_hash'] == authors['commit_hash']
    metaAuthors = meta.join(author, joinExpression, joinType)

    # MetaAuthors to Commits (one to many)
    
    joinType = "outer"
    joinExpression = metaAuthors['commit_hash'] == commits['commit_hash']
    metadf = metaAuthors.join(commits, joinExpression, joinType)

    ## Write out working_table

    metadf.write.format("parquet").save(outpath)







