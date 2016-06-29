'use strict'

    // Turn the party on and off by clicking the button.

  var button = document.querySelector('button');

function party () {
  if (document.querySelector('div').classList.contains('party')) {
   document.querySelector('div').classList.remove('party');
 } else {
 document.querySelector('div').classList.add('party');
 }
}
button.addEventListener('click', party);
