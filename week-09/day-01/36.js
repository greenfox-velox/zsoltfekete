'use strict';

var ah = [3, 4, 5, 6, 7];
var summa_1 = 0
var summa_2 = 0

// print the sum of all numbers in ah

for (var i = 0; i < ah.length; i++) {
  summa_1 += ah[i];
}
console.log(summa_1);

var i = 0

while (i < ah.length) {
   summa_2 += ah[i];
   i++;
}
console.log(summa_2)
