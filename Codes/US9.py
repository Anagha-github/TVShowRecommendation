#User story 9: My production house wants to invest in the TV show “Breaking Bad” or "Friday Night Lights" inorder to be released on my streaming service.
# I would like to know whether this TV show is the right choice and also I would appreciate some help in choosing the country where I can release it?

import pandas as pd
from pymongo import MongoClient
#-----------------------------------------------------------

client = MongoClient("mongodb://localhost:27017/")
db = client["TVSeries"]
IllegalCollect = db["IllegalCollect"]
MainCollect= db["MainCollect"]
#-----------------------------------------------------------
query1 = pd.DataFrame(db.MainCollect.aggregate([{ "$group":{"_id": 0, "avg_Votes": {"$avg": {"$toInt": "$numVotes"}}}}]))
avg_Votes = query1.iloc[0]['avg_Votes']
print("Average Votes:", avg_Votes)

query = db.MainCollect.find({"primaryTitle":"Friday Night Lights"},{"_id": 0, "numVotes":1 }) #Friday Night Lights
for x in query:
    num_Votes = x["numVotes"]

if int(num_Votes) > int(avg_Votes):
    print("This is a highly popular TV show with a popularity of :")
    query_1 = db.MainCollect.find({"primaryTitle": "Friday Night Lights"},{"_id": 0, "numVotes": 1,}) #Friday Night Lights
    for x in query_1:
        print(x)

    print("The following are the countries where this TV show was downloaded illegally. "
          "You may choose the country based on the number of illegal downloads in those countries")
    result = IllegalCollect.aggregate([{'$lookup':{'from':'MainCollect','localField':'tconst','foreignField':'tconst','as':'newarray'}},
                                       {'$unwind': '$newarray'}, {'$match': {'primaryTitle': 'Friday Night Lights'}},
                                       {'$project': {'_id':0,'illegalDownloadCountries':1 }}]) #Friday Night Lights
    for x in result:
        print(x)
else:
    print("This show does not have a high popularity")
