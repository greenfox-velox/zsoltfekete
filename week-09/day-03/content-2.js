  // fill every paragraph with the last one's content.

  var last = document.querySelector('.dog');
  var evry_paragh = document.querySelectorAll('p');
  evry_paragh.forEach(function(e) {e.innerHTML = last.textContent;});
