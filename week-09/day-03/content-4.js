  // replace the list items' content with items from this list:
var list = ['apple', 'banana', 'cat', 'dog']
var li = document.querySelectorAll('li');
li.forEach(function(e,i) {e.innerHTML = list[i]});
