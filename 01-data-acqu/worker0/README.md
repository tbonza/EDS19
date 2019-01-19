# Worker0

Airflow will communicate with `Worker0` via rest api. This is similar
to how [Apache Livy](https://livy.incubator.apache.org/) communicates
with [Apache Spark](https://spark.apache.org/). Airflow acts as a 
scheduler which tracks the progress of jobs and schedules new jobs. 


This approach is preferable to the default approach in Airflow which
requires setting up a message broker. It's preferable because it's
cheaper. Basically, it's a non-fancy http API with a message broker
behind the scenes to reduce the likelihood of mayhem. 
