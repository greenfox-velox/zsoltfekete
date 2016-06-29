'use strict'

    // On the click of the button,
    // Count the items in the list
    // And display the result in the result element.


var button = document.querySelector('button');
  function counter () {
    var list = document.querySelectorAll('li');
    var elements = 0
    list.forEach(function(e) {elements +=1 });
    var result = document.querySelector('.result');
    result.innerHTML = elements
   }

  button.addEventListener('click', counter);
