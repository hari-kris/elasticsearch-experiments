# dependency taken here
from elasticsearch import Elasticsearch
# machine details are provided here
host = "localhost"
port = 9200

es = Elasticsearch("localhost:9200")


# List the Indices
print(es.cat.indices())
