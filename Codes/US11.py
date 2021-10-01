#User story 11: I am from the Production House. Please give me an analysis on all possible languages to which I can dub the two TV shows : “Fawlty Towers”
# and “Spartacus: Gods of the Arena”, so that I can decide which languages might bring better success.
import numpy as np
from pymongo import MongoClient
import matplotlib.pyplot as plt
from bson.son import SON
#-----------------------------------------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["TVSeries"] #created a db
Languages = db["Languages"] #created a collection
MainCollect = db["MainCollect"]
#-----------------------------------------------------------

compare_1 = []
compare_2 = []
#Language popularity = popularity for a show based on its genre in different countries

query_1 = Languages.aggregate([{'$lookup':{'from':'MainCollect','localField':'tconst','foreignField':'tconst', 'as':'newarray'}},{'$unwind': '$newarray'}, {'$match': {'primaryTitle': 'Fawlty Towers'}},{'$project': {"_id":0,"languagePopularity":1}}])
for x in query_1:
    compare_1.append(x)

query_1 = Languages.aggregate([{'$lookup':{'from':'MainCollect','localField':'tconst','foreignField':'tconst', 'as':'newarray'}},{'$unwind': '$newarray'}, {'$match': {'primaryTitle': 'Spartacus: Gods of the Arena'}},{'$project': {"_id":0,"languagePopularity":1}}])

for x in query_1:
    compare_2.append(x)

compare_list1 = []
compare_list2 = []
for i in compare_1:
    compare_list1.append(i["languagePopularity"])
    print(compare_list1)
for i in compare_2:
    compare_list2.append(i["languagePopularity"])
    print(compare_list2)

barWidth = 0.25
s1=list(compare_list1[0].values())
s2=list(compare_list2[0].values())

r1 = np.arange(len(s1))
r2 = [x + barWidth for x in r1]
langPop = ["Italian", "German", "English", "Hindi", "French", "Spanish", "Korean"]

plt.figure(figsize=(9, 2))
plt.bar(r1,s1,color='#7f6d5f', width=barWidth, edgecolor='white', label='The Twilight Zone')
plt.bar(r2,s2,color='#557f2d', width=barWidth, edgecolor='white', label='Spartacus: Gods of the Arena')
plt.xlabel('Languages', fontweight='bold')
plt.ylabel('Popularity', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(s1))], ["Italian", "German", "English", "Hindi", "French", "Spanish", "Korean"])
plt.suptitle("Popularity on languages")
plt.legend()
plt.show()