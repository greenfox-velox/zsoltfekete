'use strict'

  // Remove the king from the list.
  // Fill the list based on the following list of objects:
  // only add the asteroids to the list.
  // each list item should have its category as a class
  // and its content as text content.

  var list = document.querySelector('ul.asteroids');
  var king = document.querySelector('li');
  list.removeChild(king);

    // Remove the king from the list.
    // Fill the list based on the following list of objects:
    var planetData = [
      {
        category: 'inhabited',
        content: 'Foxes',
        asteroid: true
      },
      {
        category: 'inhabited',
        content: 'Whales and Rabbits',
        asteroid: true
      },
      {
        category: 'uninhabited',
        content: 'Baobabs and Roses',
        asteroid: true
      },
      {
        category: 'inhabited',
        content: 'Giant monsters',
        asteroid: false
      },
      {
        category: 'inhabited',
        content: 'Sheep',
        asteroid: true
      }
    ]
    // only add the asteroids to the list.
    // each list item should have its category as a class
    // and its content as text content.

planetData.forEach(function(e) {
var add_elements = document.createElement('li');
  if (e.asteroid) {
    add_elements.textContent = e.content;
    add_elements.classList.add(e.category);
    list.appendChild(add_elements);
    }
})
