import pymongo
from textblob import TextBlob
from lxml import html
import json
import requests
import pymongo
import nltk
import ssl
import pandas as pd
import matplotlib.pyplot as plt

from neo4j import GraphDatabase, basic_auth

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=basic_auth("neo4j", "Kubrick"))
session = driver.session()

result = session.run("match (e { primaryTitle: 'Mad Men'})return e.tconst as tconst")#change tconst/primary title to get rating
averageRatings= session.run("match (e)-[:episode_of]-> (m)where m.primaryTitle = 'Mad Men' set e.averageRating = toInt(e.averageRating)return e.averageRating, e.seasonNumber, e.episodeNumber, e.tconst")

print(averageRatings)
data = {}
data["rating"] = []
data["index"] = []
count = 0
sum = 0
for i in averageRatings:
    count = count +1;
    sum = sum + i[0]
    print(i[0], i[1], i[2], i[3], count)
    data["rating"].append(i[0])
    data["index"].append(i[3])


average = sum/count
s = pd.DataFrame(data["rating"])
s.plot.line()
plt.show()

for record in result:
    page = requests.get('https://www.imdb.com/title/' + record['tconst'] + '/reviews?ref_=tt_urv')
    tree = html.fromstring(page.content)
    result = tree.xpath('//div[@class="content"]/div[@class="text show-more__control"]')
    reviews = tree.xpath('//span[@class="display-name-link"]/a')
    #rating = tree.xpath('//svg[@class="ipl-icon ipl-star-icon"]/span')
    for index, review in enumerate(result):
        print(review.text_content())
        blob = TextBlob(review.text_content())
        analysis: {}
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity, "here")
            analysis = {"sentence": sentence, "polarity": sentence.sentiment.polarity}
        mydict = {
            "tconst": record['tconst'],
            "reviews":
                {
                    "id": reviews[index].text_content(),
                    "analysis": analysis
                }
        }

        print(mydict)

