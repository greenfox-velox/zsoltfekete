'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function
function summa(list) {
  var sum = 0;
  for (var i = 0; i < list.length; i++) {
    sum += list[i];
  }
  return sum;
}
console.log(summa(numbers));
