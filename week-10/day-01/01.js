'use strict';

function letterCounter(string) {
  return string.split('').reduce(function(output,next){
    output[next] = output[next]+1 || +1;
    return output;
  },{});
}

// function letterCounter(string) {
//   var word = string.split('');
//   var output = {};
//   word.forEach(function (e) { output[e] = output[e] +1 || 1})
//   return output
// }
//
module.exports.letterCounter = letterCounter;
