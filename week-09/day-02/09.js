'use strict';
// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function letter_counter (string) {
  var word = string.split('');
  var output = {};
  word.forEach(function(e) {
    if (e in output) {
      {output[e] += 1;}}
    else{
      output[e] = 1};
    })
  return output
}
console.log(letter_counter('apple'));
