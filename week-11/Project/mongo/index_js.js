'use strict';


const express = require('express');
const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;
const app = express();
const bodyParser = require('body-parser');
var id = 1

const url = 'mongodb://localhost:27017/todo';

app.use(bodyParser.json());
app.use(express.static('./frontend'));

MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

  let collection = db.collection('todo')

  app.get('/todos', function(req, res) {
    collection.find({} ,{'id': 1, 'text': 1, '_id': 0 ,'completed':1,'destroyed': true}).toArray(function (err, result){
      if (err) {
        console.log(err);
      }
      res.json(result)
      return (id = result.length)
    })}
  );

  app.get('/todos/:id', function(req, res) {
    collection.find({'id': parseInt(req.params.id)}, {'id': 1, 'text': 1, '_id': 0}).toArray( function (err, result) {
      if (err) {
        console.log(err);
      }
      res.json(result)
    })});

  app.post('/todos', function(req, res){
    collection.insert({'text': req.body.text,'id':id ,'completed':false}, function(err, result){
    if (err) {
      console.log(err);
    }
    res.json({'id': parseInt(id) ,'text': req.body.text,'completed':false})
    return (id++)
      })
    });

  app.put('/todos/:id', function(req, res){
    collection.update({'id': parseInt(req.params.id)}, {$set:{'completed':req.body.completed}}, function(err, result){
    if (err) {
      console.log(err);
    }
    res.json({'id': parseInt(req.params.id), 'completed':req.body.completed})
      })
    });

  app.delete('/todos/:id', function(req, res){
    collection.update({'id': parseInt(req.params.id)}, {$set:{'destroyed':true}}, function(err, result){
    if (err) {
      console.log(err);
    }
    res.json({'id': parseInt(req.params.id),'destroyed': true})
      })
    });

app.listen(3001);}
});
