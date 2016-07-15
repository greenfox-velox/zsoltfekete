'use strict'

var chai = require('chai');
var assert = chai.assert;
const mongoskin = require('mongoskin');
// const MongoClient = mongodb.MongoClient;
var dbUrl = 'mongodb://localhost:27017/todotest';

process.env.NODE_ENV= 'test';
var db = mongoskin.db(dbUrl,{safe:true});

// var DbProvider = function() {
//   this.dbUrl = 'mongodb://localhost:27017/todotest';
// };

// DbProvider.prototype.connect = function(cb) {
// var self = this;
// MongoClient.connect(this.dbUrl, function(err, db) {
//   self.db = db;
//   cb(db)
// });
// }
// var todosdb = new DbProvider().db;

beforeEach(function(done) {
  db.collection('todo').remove();
  db.collection('todo').insert({'text': 'test','id':1 ,'completed':false}, function(err, result){});
});

  describe('ApiTest', function() {
    it('Get', function(done) {
    var url = 'http://localhost:3001'
    var data = ''
    request(url)
      .get('/todos')
      .send(data)
      .end(function(err, res) {
        res.body.errors.pages.should.have.property('text').eql('test');
        res.body.errors.pages.should.have.property('id').eql('1');
        res.body.errors.pages.should.have.property('completed').eql('false');
        done();
      });
    });
});
