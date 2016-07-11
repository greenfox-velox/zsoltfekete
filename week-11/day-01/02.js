'use strict'

var express = require('express');
var app = express();


app.get('*', function(req, res) {
  var time = new Date();
  res.send('Method:' + req.method +'\n'+ 'Url' + req.url + 'Url:' +'\n'+ time);
})

app.listen(3000);
