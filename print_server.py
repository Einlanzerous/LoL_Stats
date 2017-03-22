#Prints out all objects on both servers
#Created by Ashley Dodson
#March 2017, for CSCI 344 API Project

import pymongo
from pymongo import MongoClient

#Functionn for printing out stats
def print_stats(summoner, num):
    print "# Summoner: ", summoner[num]["summoner"]
    print "# KDA: ", summoner[num]["kda"], " over ", summoner[num]["matches_polled"], "matches used to compile data"
    print "# Kills: [", summoner[num]["kills"], "] Deaths: [", summoner[num]["deaths"], "] Assists: [", summoner[num]["assists"], "]"
    print "# Average CS per game: ", summoner[num]["average_cs"], " Average CS per minute: ", summoner[num]["average_cs_per_min"]
    print "# Average game time: ", summoner[num]["average_time"], " || This data was last updated on", summoner[num]["date_created"]
    print "########################################################################################"

#Create database connections
namerequest = MongoClient("mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest")
caitdb = namerequest.namerequest

summonertest = MongoClient("mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest")
katdb = summonertest.summonertest

#Print names awaiting push to main database
print "Printing Caitlyn information (Name_lists)"

results = caitdb.name_lists.find()

if (caitdb.name_lists.count() > 0):
    for each in results:
        print each
else:
    print "...Caitlyn server has no names awaiting push"


#Print objects from complete database
print "Printing Katarina information (summonerdata)"

datapoints = katdb.summonerdata.find()

if (katdb.summonerdata.count() > 0):
    for i in range(0, katdb.summonerdata.count()):
        print_stats(datapoints, i)
else:
    print "...Katarina has no data within."
