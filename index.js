(function () {
    "use strict";
    
    console.log("Starting...");
    
    var express = require('express'),
        bodyParser = require('body-parser'),
        mongoose = require('mongoose'),
        app = express();
    
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
    
    var Stat = katarinaDB.model('summonerdata', new mongoose.Schema(
        {
            "kills": Number,
            "deaths": Number,
            "kda": Number,
            "average_cs_per_min": Number,
            "assists": Number,
            "summoner": String,
            "level": Number,
            "averager_time": Number,
            "average_cs": Number,
            "date_created": String,
            "matches_polled": Number
        }));
    
    app.get("/getStat", function(req, res) {
        Stat.find(req.query, function(err, stat) {
            if (err) {
                console.log(err);
            } else {
                console.log(stat);
                res.json(stat);
            }
        });
    });
    
    app.listen(3000);
    console.log("Server listening on port 3000");
})();

/*"use strict";
                console.log("Hello World.");
                var app = angular.module('myApp', []);
                
                console.log("Test");
                var mongoose = require('mongoose');
                mongoose.Promise = global.Promise;  mongoose.connect('mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest');
                var db = mongoose.connection;
                db.on('error', console.error.bind(console, 'connnection error'));
            
                
                
                app.controller('myCtrl', ['$scope', function($scope) {
                    $scope.summonerName = '';
                    
                    $scope.sendName = function() {
                        db.once('open', function callback () {
                            var name = mongoose.model('name_list', (
                                {
                                    name: String
                                }
                            ));
                            var insertname = new name ({
                                name: "C9 Ray"
                            });
                            var request = $scope.summonerName;
                            name.insertMany(request);
                        });
                    };
                }]); */