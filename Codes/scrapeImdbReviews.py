from lxml import html
# import requests
import json
# import csv
import requests
import pymongo


#     print(href.text_content())
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["tvAnalysis"]
mycol = mydb["reviewsWithRating"]


with open('../DataSets/relevantTconst2.json') as f:
   datajsons = json.load(f)
   for datajson in datajsons:
      page = requests.get('https://www.imdb.com/title/' + datajson + '/reviews?ref_=tt_urv')
      tree = html.fromstring(page.content)
      result = tree.xpath('//div[@class="content"]/div[@class="text show-more__control"]')
      reviews = tree.xpath('//span[@class="display-name-link"]/a')
      rating = tree.xpath('//span[@class="display-name-link"]/a')
      # print(len(reviews), len(result))
      for index, review in enumerate(result):
         mydict = {"tconst": datajson, "reviews":{"id": reviews[index].text_content(), "text":review.text_content()} }
         print(mydict)
         #x = mycol.insert_one(mydict)