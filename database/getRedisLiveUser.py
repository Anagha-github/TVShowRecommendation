import  redis
import pymongo
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
conn = redis.Redis('localhost')


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydbMain = myclient["tvShows"]
mycolShowName = mydbMain["showName"]

tconstList = mycolShowName.find({ "primaryTitle":{"$in": ["Fleabag", "The Wire", "Monster", "Doctor Who", "The Thick of It"]}})

seriesList = []

for show in tconstList:
    print(show)
    seriesList.append({"name": show["primaryTitle"], "tconst": show["tconst"]})

print(seriesList)


print(conn.hgetall("pythonDict"))
# print(conn.hmget("pythonDict", "tt0047708"))
print(seriesList)

displayList = []
for series in seriesList:
    count = conn.hmget("pythonDict", series["tconst"])
    series["liveCount"] = str(count[0]).split("'")[1]
    displayList.append(series)

print(displayList)



plt.rcdefaults()
fig, ax = plt.subplots()

people = []
performance =[]
for value in displayList:
    people.append(value["name"])
    performance.append(int(value["liveCount"]))


#people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')

y_pos = np.arange(len(people))
#performance = [2, 3, 4, 5 ,6]

ax.barh(y_pos, performance, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How many people are watching Right now')

plt.show()