'use strict'
    // fill output1 with the first paragraph's content, text only.
    // fill output2 with the first paragraph's content keeping the cat strong.

    var first = document.querySelector('p');
    var out_1 = document.querySelector('.output1');
    var out_2 = document.querySelector('.output2');
    out_1.innerHTML = first.textContent;
    out_2.innerHTML = first.innerHTML;
