'use strict'
    // Add an item that says 'The Green Fox' to the asteroid list.
    // Add an item that says 'The Lamplighter' to the asteroid list.
    // Add a heading saying 'I can add elements to the DOM!' to the .container.
    // Add an image, any image, to the container.


var list = document.querySelector('ul');
var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
list.appendChild(newAsteroid);

var newAsteroid_2 = document.createElement('li');
newAsteroid_2.textContent = 'The Lamplighter';
list.appendChild(newAsteroid_2);

var container = document.querySelector('.container');
var h1 = document.createElement('h1')
h1.textContent = 'I can add elements to the DOM!';
container.appendChild(h1);

var image = document.createElement('img')
image.setAttribute('src','cat.jpg')
container.appendChild(image);
