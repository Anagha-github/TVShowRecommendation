#User Story 8 : I am a copyright lawyer. I would like to list 10 shows that have a maximum illegal downloads.
import json
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["TVSeries"] #created a db
IllegalCollect = db["IllegalCollect"] #created a collection
MainCollect= db["MainCollect"]
#-----------------------------------------------------------

result = IllegalCollect.aggregate([{ '$limit': 10 }, {'$sort':{'illegalTotalDownloads': -1}},
                                   {'$lookup':{'from':'MainCollect','localField':'tconst','foreignField':'tconst','as':'newarray'}},
                                   {'$unwind': '$newarray'}, {'$project': {'_id':0,'illegalDownloadCountries':1,'illegalTotalDownloads':1, 'newarray.primaryTitle':1}}])
for doc in result:
    print(doc)



