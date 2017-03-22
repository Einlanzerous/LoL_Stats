#Code for making requests as users need them to Caitlyn
#Created by Ashley Dodson
#March 2017, for CSCI 344 API Project

import os
import time
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy, StatSummaryType
import pymongo
from pymongo import MongoClient
import server_call

#Create database connections
namerequest = MongoClient("mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest")
requestdb = namerequest.namerequest

while 1:
    print "No current requests, awaiting new request"

    if(requestdb.name_lists.count() > 0):
        print "New request incoming"

        #Test displaying names
        showval = requestdb.name_lists.find()

        # Send name for request
        current_name = showval[0]["name"]

        print "Requesting ", current_name, " be added to Katarina server"

        server_call.request_data(current_name)

        # Remove newly pulled name from Caitlyn server
        if (requestdb.name_lists.find({"name": current_name})):
            requestdb.name_lists.delete_many({"name": current_name})

        print "Removed request from Caitlyn server"