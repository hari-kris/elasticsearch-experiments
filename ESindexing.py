from elasticsearch import Elasticsearch
es = Elasticsearch()


index = "mobin"
type = "class1"


data = {
    "name": "Victoria",
    "version": 11,
    "mini-version": 12
}

# Indexing the document
es.index(index=index, doc_type=type, body=data)

# POST /index/type
# {
# "name": Victoria,
# "age": 24
# }
