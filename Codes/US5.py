#User story 5: I am the Producer of 'Yes, Prime Minister' and I want to know which episodes have a dip in rating for my TV show.

from neo4j import GraphDatabase, basic_auth
import matplotlib.pyplot as plt

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth(user = "neo4j", password = "123456"))
session = driver.session()

avg= session.run("match (e)-[:episode_of]-> (s)where s.primaryTitle = 'Yes, Prime Minister' return avg(e.averageRating) as row") #The Twilight Zone
for i in avg:
    avgRE = i[0]
print("Average Rating of the TV show is:", avgRE)

compare_1 = []
compare_2 = []

details = session.run("match (e)-[:episode_of]-> (s)where s.primaryTitle = 'Yes, Prime Minister' return e.averageRating,e.seasonNumber,e.episodeNumber") #The Twilight Zone
for record in details:
    if record[0] < (avgRE - 1.5):
        print("AverageRating=",record[0],"SeasonNumber=",record[1],"EpisodeNumber=",record[2])

details = session.run("match (e)-[:episode_of]-> (s)where s.primaryTitle = 'Yes, Prime Minister' return e.averageRating,e.seasonNumber,e.episodeNumber")
for x in details:
    compare_2.append("E" + x[2] + "S" + x[1])
    compare_1.append(x[0])

plt.scatter(compare_2, compare_1)
plt.show()