# Spark Jobs

Need to scale up the prototype using Apache Spark. This 
folder contains all spark jobs used when replicating
`tbonza/EDS19/project/PredictingRepoHealth.ipynb`. Goal is
to show a forecasting model at scale. 

I already have individual examples for specific repos that
can be graphed in put in a report. We just want to make sure
the relationships generalize.

Getting some basic descriptive statistics would also be helpful.
Priorities:

1. Generate the forecasting model to make sure there's time
1. Follow up with some more general descriptives which may
   be of interest.
   
   * Apache foundation appears to have `x` number of projects
	 with at least `v(t)` velocity in the last year. We can 
	 say the same thing for Google, Facebook, edX, etc. I'm
	 forecasting that velocity `v(t)` will be `y` in the next
	 year for each organization.
