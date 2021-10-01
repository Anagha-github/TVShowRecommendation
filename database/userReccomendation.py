#Comment and rating on same scale

from neo4j import GraphDatabase, basic_auth
import requests
import pymongo
from textblob import TextBlob
from lxml import html

# uri = "bolt://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=basic_auth("neo4j", "Kubrick"))
# session = driver.session()
#
# result = session.run("match (s: Series) return s")


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydbWithUser = myclient["tvAnalysis"]
mycolWithUser = mydbWithUser["seriesReview_New"]
mydbMain = myclient["tvShows"]
mycolShowName = mydbMain["showName"]

getTconstFromPrimary = {"primaryTitle": "The Wire"} #get tconst from primary
tconst = ''

mytconst = mycolShowName.find(getTconstFromPrimary)

for x in mytconst:
  print(x["tconst"])
  tconst = x["tconst"]

print(tconst)

getReviewsFromTconst = {"tconst": tconst}
getTconstFromUserId = {""}

myReviews = mycolWithUser.find(getReviewsFromTconst)

likedUser = []
for x in myReviews:
  #print(x["reviews"])
  for review in x["reviews"]:
      if review["rating"] is not None and (float(review["rating"])) > 9:
          likedUser.append(review["userPageId"])


relevantTcoonst = {}
data = []
dataAll = []

for user in likedUser:

                page = requests.get('https://www.imdb.com/user/' + user + '/ratings?sort=date_added,desc&ratingFilter=10&mode=detail&lastPosition=0')
                tree = html.fromstring(page.content)
                list = tree.xpath('//div[@class="lister-list"]')
                for review in list:
                    print(review.find_class("lister-item-header")[0].cssselect('a')[0].text_content())
                    # dataAll.append(user["userId"])
                    # if user["userId"] not in data:
                    #     data.append(user["userId"])
                    # result = session.run("CREATE (a:user)"
                    #                      "SET a.userId = $user[userId]")
                    # print(result)
# print(len(data), len(dataAll))