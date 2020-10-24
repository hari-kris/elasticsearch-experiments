
from elasticsearch import Elasticsearch
es = Elasticsearch()
#  Module to Include the Bulk Indexing Api
from elasticsearch import helpers
import csv
import time

host = "localhost"
port = 9200
index = "medical"
type = "hcpc"
filePath = "/home/matrix/ELK/data/hcpc.csv"
bulk_size = 500
actions = []



def readCsv(filePath):
    fileObj = open(filePath)
    reader = csv.DictReader(fileObj, delimiter=',')
    return reader

def printFile(fileObj):
    for line in fileObj:
        print line




def composeDocuments(fileObj):
    global actions
    for line in fileObj:
        action = {
            "_index": index,
            "_type": type,
            "_source":
                {'HCPC': line['HCPC'],
                 'SEQNUM': line['SEQNUM'],
                 'RECID': line['RECID'],
                 'LONG_DESCRIPTION': line['LONG_DESCRIPTION'],
                 'SHORT_DESCRIPTION': line['SHORT_DESCRIPTION']
                 }

        }
        actions.append(action)
        if(len(actions) ==bulk_size):
            bulkIndex(actions)
            actions = []
    bulkIndex(actions)
    actions = []

def bulkIndex(action):
    print "Processing"
    print len(action)
    helpers.bulk(es, action)


fileObj = readCsv(filePath)
# printFile(fileObj)
composeDocuments(fileObj)
start = time.time()
end = time.time()
print(end - start)












