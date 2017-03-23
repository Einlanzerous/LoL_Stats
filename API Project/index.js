(function () {
    "use strict";
    
    console.log("Starting...");

    var MongoClient = require('mongodb').MongoClient;
    var express = require('express'),
        bodyParser = require('body-parser'),
        mongoose = require('mongoose'),
        app = express();
    var assert = require('assert');
    var ObjectId = require('mongodb').ObjectID;
    var url = 'mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest';

    /*var pullnames = function(db, callback) {
        var found = false;
        var cursor = db.collection('summonerdata').find();
        cursor.each(function(err, doc) {
            assert.equal(err, null);
            if ((doc != null) && !found) {
                var test = doc;
                if(test.summoner == "Einlanzerous"){
                    //console.log(doc);
                    var obj = {
                        "kills": test.kills,
                        "summoner": test.summoner
                    }
                    return obj;
                    found = true;
                }
                //console.dir(doc);
            } else {
                callback();
            }
        });
    };*/
    
    mongoose.Promise = global.Promise;
    
    app.use(express.static(__dirname));
    app.use(bodyParser.urlencoded({extended: true}));
    
    var caitlynDB = mongoose.createConnection('mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest');
    
    var katarinaDB = mongoose.createConnection('mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest');
    
    var name = caitlynDB.model('name_list', (
        {
            "name": String
        }));
    
    app.post("/putName", function(req, res) {
        var newSummonerName = new name(req.body);
        newSummonerName.save(function(error, data) {
            if (error) console.log(error);
        });
    });
    
    var Stat = katarinaDB.model('summoner', new mongoose.Schema(
        {
            "kills": Number,
            "deaths": Number,
            "kda": Number,
            "average_cs_per_min": Number,
            "assists": Number,
            "summoner": String,
            "level": Number,
            "average_time": Number,
            "average_cs": Number,
            "date_created": String,
            "matches_polled": Number
        }));
    
    /*app.get("/getStat", function(req, res) {
        MongoClient.connect(url, function(err, db) {
            assert.equal(null, err);
            console.log(pullnames(db, function() {
                db.close();
            }));
            //console.log(stat);
            //res.json(stat);
        });
    });*/
    
    app.get("/getStat", function(req, res) {
        Stat.find(req.query, function(err, stat) {
            if (err) {
                console.log(err);
            } else {
                var oneStat = stat[stat.length-1];
                console.log(oneStat);
                res.json(oneStat);
            }
        }); 
    });
    
    app.listen(3000);
    console.log("Server listening on port 3000");
})();