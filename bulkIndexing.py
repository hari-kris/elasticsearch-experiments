from elasticsearch import Elasticsearch
es = Elasticsearch()
#  Module to Include the Bulk Indexing Api
from elasticsearch import helpers
import csv
import time

host = "localhost"
port = 9200
#index = "testing-elk"
index = "mapping-elk"
type = "ship"
filePath = "/data/ELK/DataSet/train.csv"
actions = []



def readCsv(filePath):
    fileObj = open(filePath)
    reader = csv.DictReader(fileObj, delimiter=',')
    return reader

def printFile(fileObj):
    for line in fileObj:
        print(line)

def sequentialIndexing(fileObj):
    for line in fileObj:
        data = {
                     'Fare': line['Fare'],
                     'Name': line['Name'],
                     'Embarked': line['Embarked'],
                     'Age': line['Age'],
                     'Parch': line['Parch'],
                     'Pclass': line['Pclass'],
                     'Sex': line['Sex'],
                     'Survived': line['Survived'],
                     'SibSp': line['SibSp'],
                     'PassengerId': line['PassengerId'],
                     'Ticket': line['Ticket']
                }
        print("Processing")
        es.index(index=index, body=data)


def composeDocuments(fileObj):
    #counter
    for line in fileObj:
        action = {
            "_index": index,
            # "_type": type,
            "_source":
                {'Fare': line['Fare'],
                 'Name': line['Name'],
                 'Embarked': line['Embarked'],
                 'Age': line['Age'],
                 'Parch': line['Parch'],
                 'Pclass': line['Pclass'],
                 'Sex': line['Sex'],
                 'Survived': line['Survived'],
                 'SibSp': line['SibSp'],
                 'PassengerId': line['PassengerId'],
                 'Ticket': line['Ticket']
                 }

        }
        actions.append(action)

def bulkIndex(actions):
    helpers.bulk(es, actions)


fileObj = readCsv(filePath)
# printFile(fileObj)
#composeDocuments(fileObj)
#start = time.time()
#bulkIndex(actions)
#end = time.time()
#print(end - start)

fileObj = readCsv(filePath)
start = time.time()
sequentialIndexing(fileObj)
end = time.time()
print(end - start)
