#test file for trying to pull summoner names from the server.

#Created by Ashley Dodson

import os
import time
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
import pymongo
from pymongo import MongoClient

#Create database connections
server = MongoClient("mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest")
serverdb = server.summonertest

namerequest = MongoClient("mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest")
requestdb = namerequest.namerequest


#Test getting name
testval = serverdb.summonerdata.find()

for each in testval:
    print (each)

#Test displaying names
showval = requestdb.name_list.find()

for each in showval:
    print each