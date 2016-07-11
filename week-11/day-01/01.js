'use strict'

var http = require('http');
var time = new Date();

var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Method:' + req.method +'\n'+ 'Url' + req.url + 'Url:' +'\n'+ time);
});


server.listen(3000, '127.0.0.1');
