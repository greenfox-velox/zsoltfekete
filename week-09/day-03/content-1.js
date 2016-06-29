'use strict'
  // 1. Alert the content of the header.
  // 2. Write the content of the first paragraph to the console.
  // 3. Alert the content of the second paragraph.
  // 4. Replace the heading's content with 'New content'.
  // 5. Replace the last paragraph's content with the first paragraph's content.

  var h1 = document.querySelector('h1');
  alert(h1.textContent);

  var first_paragh = document.querySelector('p');
  console.log(first_paragh.textContent);

  var sec_paragh = document.querySelector('.other');
  alert(sec_paragh.textContent);

var last_paragh = document.querySelector('.result');

h1.innerHTML = 'New Content';

last_paragh.innerHTML = first_paragh.textContent;
