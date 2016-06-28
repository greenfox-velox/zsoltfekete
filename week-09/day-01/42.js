'use strict';

// create a function that returns it's input factorial
function factor(number) {
  var total = 1;
  for (var i = 1; i <= number; i++) {
    total *= i;
  }
  return total;
}

console.log(factor(5));
