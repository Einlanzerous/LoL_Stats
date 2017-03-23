/**
 * Created by TheEn on 3/22/2017.
 */
var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://ruler:Katarina7!@ds135700.mlab.com:35700/summonertest';

var pullnames = function(db, callback) {
    var cursor = db.collection('summonerdata').find();
    cursor.each(function(err, doc) {
        assert.equal(err, null);
        if (doc != null) {
            console.dir(doc);
        } else {
            callback();
        }
    });
};

MongoClient.connect(url, function(err, db) {!
    assert.equal(null, err);
    pullnames(db, function() {
        db.close();
    });
});