#Code for filling Server with needed information from  Riot API
#Created by Ashley Dodson
#March 2017, for CSCI 344 API Project
#Uses Pymongo and Cassiopeia to quickly access resources

import os
import time
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
from pymongo import MongoClient
import pymongo

#Set Riot API information
riotapi.set_region("NA")
riotapi.print_calls(False)
riotapi.set_api_key(os.environ["RIOT_DEV"])
riotapi.set_load_policy(LoadPolicy.lazy)

#Establish database connection
client = MongoClient("mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest")
db = client.summonertest

#Declare variables
kills = 0
deaths = 0
assists = 0
kda = 0
avg_time = 0
avg_cs = 0
avg_game_cs = 0
avg_time = 0
cs = 0
name_request = "Stella Videntis" #CHANGE TO DESIRED LOOKUP NAME
summoner = riotapi.get_summoner_by_name(name_request)
match_list = summoner.match_list()

#Number of matches to pull from Riot Servers
num_matches = 5 #CHANGE THIS TO NUMBER INTERESTED IN


#Basic stats collection
for i, match_reference in enumerate(match_list[0:num_matches]):
    match = match_reference.match()
    for participant in match.participants:
        if participant.summoner_id == summoner.id:
            cs += participant.stats.cs
            kills += participant.stats.kills
            deaths += participant.stats.deaths
            assists += participant.stats.assists
            avg_time += match.duration.total_seconds()
            if(avg_time > 0):
                avg_cs += (float)(participant.stats.cs / (match.duration.total_seconds() / 60))

#Matchwide averages
if(deaths >0):
    kda = (float)(kills + assists) / deaths
else:
    kda = kills + assists
if(num_matches > 0):
    avg_time = (float)((avg_time / 60) / num_matches)
    avg_game_cs = (float)(avg_cs / num_matches)
    if(avg_time > 0):
        avg_cs = (float)(cs / num_matches)
#TODO Create scores for various items

#Verify user not already on server, delete if pre-existing
if(db.summonerdata.find({"sname": summoner.name})):
    clear = db.summonerdata.delete_many({"sname": summoner.name})
if(db.summonerdata.find({"summoner": summoner.name})):
    clear = db.summonerdata.delete_many({"summoner": summoner.name})

#Push to server
pushVal = db.summonerdata.insert_one(
    {
        "summoner": summoner.name,
        "level": summoner.level,
        "matches_polled": num_matches,
        "kda": round(kda, 3),
        "kills": kills,
        "deaths": deaths,
        "assists": assists,
        "avgerage_cs_per_min": round(avg_game_cs, 1),
        "average_cs": (int)(avg_cs),
        "average_time": round(avg_time, 2),
        "date_created": time.asctime(time.localtime(time.time()))
    }
)
#TODO Adjust so that data sometimes updates instead of always deleting


#Report data on server to console
display = db.summonerdata.find().sort([
    ("summoner", pymongo.ASCENDING)
    ])

for summoners in display:
    print(summoners)