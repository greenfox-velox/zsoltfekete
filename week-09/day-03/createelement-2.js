'use strict'

  // Remove the king from the list.
  // Add 3 list items saying 'The Fox' to the list.

var list = document.querySelector('ul.asteroids');
var king = document.querySelector('li');
list.removeChild(king);

var fox_1 = document.createElement('li');
fox1.textContent = 'The Fox';
list.appendChild(fox_1);

var fox_2 = document.createElement('li');
fox2.textContent = 'The Fox';
list.appendChild(fox_2);

var fox_3 = document.createElement('li');
fox3.textContent = 'The Fox';
list.appendChild(fox_3);
