'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function convert_number_to_string(number) {
  switch (number) {
    case 0:
      console.log('zero');
      break;
    case 1:
      console.log('one');
      break;
    case 2:
      console.log('two');
      break;
    default:
      console.log('many');
      break;
  }
}
(convert_number_to_string(2));
