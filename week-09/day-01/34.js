'use strict';

var ag = [3, 4, 5, 6, 7];
var i = 0
// double all the element's values in ag

while (i < ag.length) {
   ag[i] *= 2;
   i++;
}
console.log(ag)

for (var i = 0; i < ag.length; i++) {
  ag[i] *= 2;
}
console.log(ag);
