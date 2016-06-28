'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function list_checker(list) {
  return list.every(function(i) { return is_prime(i)});
}

function is_prime(number) {
    for(var i = 2; i < number; i++) {
        if(number % i === 0) {
            return false;
        }
    }
    return number > 1;
}

console.log(list_checker(numbers))
