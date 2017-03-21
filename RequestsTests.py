import random
import os
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
import pymongo
from pymongo import MongoClient
from datetime import datetime

riotapi.set_region("NA")
riotapi.print_calls(False)
dev_key = os.environ["RIOT_DEV"]
riotapi.set_api_key(dev_key)
riotapi.set_load_policy(LoadPolicy.lazy)

summoner = riotapi.get_summoner_by_name("stella videntis")
print("{name} is a level {level} summoner on the NA server.".format(name=summoner.name, level=summoner.level))

match_list = summoner.match_list()

num_matches = 10

kills = 0
deaths = 0
assists = 0
kda = 0.0
avg_time = 0
cs = 0

for i, match_reference in enumerate(match_list[0:num_matches]):
    match = match_reference.match()
    for participant in match.participants:
        if participant.summoner_id == summoner.id:
            cs += participant.stats.cs
            kills += participant.stats.kills
            deaths += participant.stats.deaths
            assists += participant.stats.assists
            avg_time += match.duration.total_seconds()

    kda = (float)(kills + assists) / deaths
    #print ("Rolling KDA is {0}, based on  {1}/{2}/{3}".format(round(kda, 4), kills, deaths, assists))

avg_time = (float)((avg_time) / 60 / num_matches)
avg_cs = (float)(cs / num_matches)

print("Average KDA is {0}/{1}/{2} == {3} over past {4} matches.".format(kills, deaths, assists, round(kda, 4), num_matches))

if(avg_time > 0):
    print("Average game time is {0}, with average CS being {1} per game.".format(round(avg_time, 2), avg_cs))

challenger_league = riotapi.get_challenger()
best_na = challenger_league[0].summoner
print("He's much better at writing Python code than he is at LoL. He'll never be as good as {name}.".format(name=best_na.name))

client = MongoClient("mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest")

db = client.summonertest

if(db.summonerdata.find({"sname": summoner.name})):
    clear = db.summonerdata.delete_many({"sname": summoner.name})

print("This operation resulted in {0} deletions from the database.".format(clear.deleted_count))

testVal = db.summonerdata.insert_one(
    {
        "sname": summoner.name,
        "datafrom": num_matches,
        "kda": round(kda, 3),
        "level": summoner.level,
        "averagecs": avg_cs,
        "averagetime": round(avg_time, 2),
        "inserted": "true"
    }
)

finder = db.summonerdata.find().sort([
    ("sname", pymongo.ASCENDING)
    ])

for items in finder:
    print(items)
