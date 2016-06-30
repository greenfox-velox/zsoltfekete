
'use strict';

// Create a script that replaces every image
// with this: http://bit.ly/lpgreenfox
// Create a bookmarklet that does that on any website.

var img = document.querySelectorAll('img');
img.forEach(function(e) {
  e.setAttribute('src', 'http://bit.ly/lpgreenfox');
})
