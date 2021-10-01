
import csv
import sys
import json

# allTconst = '.'

# with open('../DataSets/relevantEpisodes.json') as f:
#     datajson = json.load(f)
#
# print(datajson["relevantTvEpisodes"])

test = {}
test["final"] =[]

with open('episodeInfo.json') as f:#try a better way than this
    datas = json.load(f)

    for data in datas["data"]:
        with open('../DataSets/relevantEpisodes.json') as g:
            datajsons = json.load(g)
            for datajson in datajsons["relevantTvEpisodes"]:
                if data['tconst'] == datajson["tconst"]:
                    test["final"].append({
                        'tconst': data["tconst"],
                        'titleType': data["titleType"],
                        'primaryTitle': data["primaryTitle"],
                        'originalTitle': data["originalTitle"],
                        'isAdult': data["isAdult"],
                        'startYear': data["startYear"],
                        'endYear': data["endYear"],
                        'runtimeMinutes': data["runtimeMinutes"],
                        'genres': data["genres"],
                        'parentTconst': datajson["parentTconst"],
                        "seasonNumber": datajson["seasonNumber"],
                        "episodeNumber": datajson["episodeNumber"]
                    })

with open('episodeInfoNew.json', 'w') as f:
    json.dump(test, f)


# list = []
# listInfo=[]
#
# for data in datas['data']:
#     list.append(data['tconst'])
#     listInfo.append({
#         'tconst': data[0],
#         'titleType': data[1],
#         'primaryTitle': data[2],
#         'originalTitle': data[3],
#         'isAdult': data[4],
#         'startYear': data[5],
#         'endYear': data[6],
#         'runtimeMinutes': data[7],
#         'genres': data[8]
#     })
# #print(list)
# episodeTconst = {}
# episodeTconst["data"] = []
# with open('../DataSets/relevantEpisodes.json') as f:
#     datajson = json.load(f)
#     for i in datajson["relevantTvEpisodes"]:
#         if i['tconst'] in list:
#             episodeTconst["data"].append({
#                 "parentTconst": i["parentTconst"],
#             })
#
# print(episodeTconst)

# episodeInfo = {}
# episodeInfo["data"] = []
# with open('../DataSets/allTconstInfo.tsv', 'r') as tsvin:
#     for line in csv.reader(tsvin, delimiter='\t'):
#         if line[0] in episodeTconst['data']:
#             episodeInfo["data"].append({
#                 'tconst': line[0],
#                 'titleType': line[1],
#                 'primaryTitle': line[2],
#                 'originalTitle': line[3],
#                 'isAdult': line[4],
#                 'startYear': line[5],
#                 'endYear': line[6],
#                 'runtimeMinutes': line[7],
#                 'genres': line[8],
#             })
#
# with open('episodeInfo.json', 'w') as f:
#     json.dump(episodeInfo, f)
