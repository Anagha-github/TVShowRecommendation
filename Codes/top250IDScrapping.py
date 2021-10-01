from lxml import html
import requests


page = requests.get('https://www.imdb.com/chart/toptv?ref_=tt_awd')
tree = html.fromstring(page.content)

hrefs = tree.xpath('//td[@class="titleColumn"]/a')

# f = open("top250TvIDss.csv", "x") #x means create files and return error if already exist
for href in hrefs:
#    f = open("top250TvIDs.csv", "a")
#    f.write(href.attrib['href'].split("/")[2] + ", ")
#    f.close()

   print(href.attrib['href'].split("/")[2] + ", ")