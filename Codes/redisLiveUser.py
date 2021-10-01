import  redis
import pymongo
import random
conn = redis.Redis('localhost')


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydbMain = myclient["tvShows"]
mycolShowName = mydbMain["showName"]

hashmap = {}

for show in mycolShowName.find():
    hashmap[show["tconst"]] = random.randint(1000,5000)

print(hashmap)

conn.hmset("pythonDict", hashmap)

print(conn.hgetall("pythonDict"))





# user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}
#
# conn.hmset("pythonDict", user)
#
# conn.hgetall("pythonDict")