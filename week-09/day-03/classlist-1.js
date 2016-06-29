'use strict'
  // Does cat have a cat class?
  // If so, alert 'YEAH CAT!'
  // If dolphin has a 'dolphin' class, replace apple's content with 'pear'
  // If apple has an 'apple' class, replace cat's content with 'dog'
  // Make apple red
  // Make balloon less balloon-like

  var all_p = document.querySelectorAll('p');

  all_p.forEach(function(e) {
    if (e.textContent === 'cat' && e.classList.contains('cat'))
      {alert('YEAH CAT!')}
    })

  var apple = document.querySelector('.apple');

  all_p.forEach(function(e) {
    if (e.textContent === 'dolphin' && e.classList.contains('dolphin'))
      {apple.textContent ='pear'}
    })

var cat = document.querySelector('.cat');

  all_p.forEach(function(e) {
    if (e.textContent === 'apple' && e.classList.contains('apple'))
      {cat.textContent ='dog'}
    })

var balloon = document.querySelector('.balloon');

apple.classList.add('red')
balloon.classList.remove('balloon')
