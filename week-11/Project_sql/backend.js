'use strict';

const mysql = require('mysql');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

const con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'sql',
  database: 'toDoDatabes',
});

con.connect(function (err) {
  if (err) {
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

app.use(bodyParser.json())
app.use(express.static('./frontend'));

app.get('/todos/', function(req, res) {
  con.query('SELECT * FROM Todo;', function(err,todos){
    if (err) {
      console.log(err.toString());
      return;
    }
    res.json(todos);
  });
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM Todo WHERE id ='+req.params.id,function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.json(todo[0]);
  });
});

app.post('/todos/',function(req, res) {
  con.query("INSERT INTO todo (text) VALUES ('"+req.body.text+"')",
   function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.json({id:todo.insertId  , text:req.body.text  });
  });
});

app.put('/todos/:id',function(req, res) {
  console.log(req);
  con.query('UPDATE todo SET completed = !completed WHERE id ='+req.params.id,
   function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    con.query('SELECT completed FROM Todo WHERE id ='+req.params.id, function(err,status){
      res.json({ id : req.params.id, completed: Boolean(status[0].completed) })
    })
  });
});

app.delete('/todos/:id',function(req, res) {
  con.query('DELETE FROM todo WHERE id='+req.params.id,
   function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.json({ id : req.params.id});
  });
});

app.listen(3000);
