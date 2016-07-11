'use strict'

var todos = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
]

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var id = todos.length
app.use(bodyParser.json())

app.get('/todos/', function(req, res) {
  res.json(todos)
});

app.get('/todos/:id', function(req, res) {
  res.json(getOne(req.params.id));
});

app.post('/todos/',function(req, res) {
  res.json(addOne(req.body.text));
});

app.put('/todos/:id',function(req, res) {
  res.json(putOne(req.params.id, req.body.text));
});

app.delete('/todos/:id', function(req, res) {
  res.json(deleteOne(req.params.id));
  }
);

function addOne(inputText) {
  id++;
  var newToDo ={"completed":false, "id": id, "text":inputText}
  todos.push(newToDo);
  return newToDo;
}

function getOne(inputId) {
  return todos.filter(function(todo,index) {
    return idChecker(inputId,todo);
  });
}

function putOne(inputId, inputText) {
  return todos.filter(function(todo,index) {
    if (idChecker(inputId, todos[index])){
      todo.completed = true;
      todo.text = inputText;
      return todo;
    }
  });
}

function deleteOne(inputId) {
  return todos.filter(function(todo,index) {
    if (idChecker(inputId, todos[index])){
      todo.destroyed = true;
      return todos.splice(todo, 1)[0];
    }
  });
}

function idChecker(inputId,todo) {
  if(parseInt(inputId) === todo.id) {
    return todo;
  }
}

app.listen(3000);
