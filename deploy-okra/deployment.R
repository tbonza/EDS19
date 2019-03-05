# Working through the deployment details

# n1-standard-32
#
# 60 pods per a node,
# 167 nodes
# about $55 per hour

total_repos <- 37338982


pods <- 10000
max_pods_per_node  <- 100
max_nodes <- 5000


1.5 * ((total_repos / pods) / 1000)
