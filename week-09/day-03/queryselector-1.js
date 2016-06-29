// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.

var king = document.querySelector('.asteroid');
console.log(king);

var conceited = document.querySelector('.b326');
alert(conceited);

var businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function(e) {console.log(e)});

var conceitedKing = document.querySelectorAll('.container .asteroid');
conceitedKing.forEach(function(e) {alert(e)});

var noBusiness = document.querySelectorAll('div.asteroid');
noBusiness.forEach(function(e) {console.log(e)});

var allBizniss = document.querySelector('p');
alert(allBizniss);
