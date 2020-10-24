from elasticsearch import Elasticsearch
es = Elasticsearch()

index = "session10"
type = "class1"
result = es.search(index=index)
print(result)
print(result['hits']['hits'][0])
print(result['hits']['hits'][0]["_source"])
print(result['hits']['hits'][0]["_source"]['name'])


{'took': 1, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 7, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'python', '_type': 'class1', '_id': 'U1b7P20B5eDWWFX9OPrI', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 3.7}}, {'_index': 'python', '_type': 'class1', '_id': 'VFb7P20B5eDWWFX97PoB', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 10}}, {'_index': 'python', '_type': 'class1', '_id': 'VVYCQG0B5eDWWFX9mfqp', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 10}}, {'_index': 'python', '_type': 'class1', '_id': '5UFcTG0BsY0arHYi5rOx', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 10}}, {'_index': 'python', '_type': 'class1', '_id': '5kFeTG0BsY0arHYiELNE', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 11}}, {'_index': 'python', '_type': 'class1', '_id': '50FeTG0BsY0arHYik7Pa', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 11, 'mini-version': 7.2}}, {'_index': 'python', '_type': 'class1', '_id': 'KqBCYW0BE7H0flf5RLEE', '_score': 1.0, '_source': {'name': 'Introduction to ES by python', 'version': 11, 'mini-version': 12}}]}}
