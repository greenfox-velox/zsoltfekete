'use strict';

var file = require('./01');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(file.letterCounter('apple'), {a:1, p:2, l:1, e:1});
  t.end();
});
