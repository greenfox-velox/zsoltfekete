'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and
//also deletes it from it
// please don`t use the built in methods

function Stack() {
  this.elements = []
  var number_of_elements= 0;

  this.size = function () {
    return number_of_elements};

  this.add_element= function (element) {
    this.elements[number_of_elements] = element;
    number_of_elements += 1;
    return this.elements;
  };

  this.remove= function () {
    this.elements.splice(number_of_elements-1);
    number_of_elements -= 1;
    return this.elements[number_of_elements];
  };

}
var geza = new Stack();
geza.add_element('macska');
geza.add_element('kutya');
geza.add_element('ló');

console.log(geza.size());
console.log(geza.elements);
geza.remove();
console.log(geza.size());
console.log(geza.elements);
