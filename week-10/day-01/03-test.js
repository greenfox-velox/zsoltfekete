'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area// Every rectangle should have a method called getCircumference() that returns its circumference

var file = require('./03');
var tape = require('tape');
var bigger = new file.Rectangles(4,6);
var only_X = new file.Rectangles(4);

tape(function(t) {
  t.deepEqual(bigger.getArea(), 24);
  t.deepEqual(bigger.getCircumference(), 20);
  t.end();
});
