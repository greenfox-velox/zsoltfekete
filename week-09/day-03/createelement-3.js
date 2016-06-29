'use strict'

    // Remove the king from the list.
    // Add list items that have the following text contents:

  var new_list=['apple', 'bubble', 'cat', 'green fox']


  var list = document.querySelector('ul.asteroids');
  var king = document.querySelector('li');
  list.removeChild(king);

  new_list.forEach(function(e) {
    var add_elements = document.createElement('li');
    add_elements.textContent = e;
    list.appendChild(add_elements);
  });
