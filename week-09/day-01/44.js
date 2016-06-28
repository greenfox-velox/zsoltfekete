'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)
function minimal(numbers) {
  var minimal = numbers[0];
  for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] < minimal) {
      minimal = numbers[i];
  }
  }
  return minimal;
}

console.log(minimal(numbers));
