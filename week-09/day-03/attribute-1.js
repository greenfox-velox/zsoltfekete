'use strict'
    // Write the image's url to the console.
    // Replace the image with a picture of yourself.
    // Make the link point to the Green Fox Academy website.
    // Disable the second button.
    // Replace its text with 'Don't click me!'

var image = document.querySelector('img');
console.log(image.getAttribute('src'));

image.setAttribute('src','cat.jpg')

var link = document.querySelector('a');
link.setAttribute('href','http://www.greenfoxacademy.com/')

var button = document.querySelector('.this-one');
button.disabled = true;

button.innerHTML='Do not click me!'
