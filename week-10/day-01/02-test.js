'use strict';

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9 , books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var file = require('./02');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(file.bookCounter(students), (4));
  t.end();
});
