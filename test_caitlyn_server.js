/**
 * Created by Einlanzerous on 3/21/2017.
 */

var listname = function (providedName) {

    var mongoose = require('mongoose');

    mongoose.Promise = global.Promise;

    mongoose.connect('mongodb://emperor:Caitlyn7!@ds058739.mlab.com:58739/namerequest');

    var db = mongoose.connection;

    db.on('error', console.error.bind(console, 'connection error:'));

    db.once('open', function callback() {
        var name = mongoose.model('name_list', (
            {
                name: String
            }
        ));

        var insertname = new name({
            name: providedName
        });

        var request = [insertname];
        name.insertMany(request);
    });
};

listname("C9 Gun");