'use strict';

// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area// Every rectangle should have a method called getCircumference() that returns its circumference


function Rectangles(x,y) {
  this.x = x;
  this.y = y;
}

Rectangles.prototype.getArea = function() {
   return this.x * this.y;
}

Rectangles.prototype.getCircumference = function() {
  return  2 * (this.x + this.y);
}

var big = new Rectangles(4,6);

console.log(big.getArea());
console.log(big.getCircumference());


module.exports.Rectangles= Rectangles;
