from elasticsearch import Elasticsearch
es = Elasticsearch()
host = "localhost"
port = 9200
index = "python"
type = "class1"
# get the document id separately
es.update(index=index,id="50FeTG0BsY0arHYik7Pa",body={"doc": {"mini-version": 7.2 }})
