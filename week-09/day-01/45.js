'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array
function short_string (list) {
  var shortest = list[0];
  for (var i = 0; i < list.length; i++) {
    if (shortest.length > list[i].length) {
      shortest = list[i];
    }
  }
  return shortest;
}

console.log(short_string(names));
