import csv
import sys
import json

test = {}
test["final"] =[]

with open('../DataSets/allRatings.tsv', 'r') as tsvin:
     for line in csv.reader(tsvin, delimiter='\t'):
             with open('../DataSets/episodeInfoNew.json') as g:
                 datajsons = json.load(g)
                 for datajson in datajsons["final"]:
                     if datajson["tconst"] == line[0]:
                        print(datajson["tconst"], line)
                        test["final"].append({
                            'tconst': datajson["tconst"],
                            'titleType': datajson["titleType"],
                            'primaryTitle': datajson["primaryTitle"],
                            'originalTitle': datajson["originalTitle"],
                            'isAdult': datajson["isAdult"],
                            'startYear': datajson["startYear"],
                            'endYear': datajson["endYear"],
                            'runtimeMinutes': datajson["runtimeMinutes"],
                            'genres': datajson["genres"],
                            'parentTconst': datajson["parentTconst"],
                            "seasonNumber": datajson["seasonNumber"],
                            "episodeNumber": datajson["episodeNumber"],
                            "averageRating": line[1],
                            "numVotes": line[2]
                        })

with open('episodeInfoUpdated.json', 'w') as f:
    json.dump(test, f)
