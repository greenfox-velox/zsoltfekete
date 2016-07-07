


var h1Title = document.querySelector('h1');
var h2Title = document.querySelector('h2');
var Button = document.querySelector('button');
Button.addEventListener('click', link);

function link(){
var xhr = new XMLHttpRequest();
     xhr.onload = function() {
       h1Title.textContent=(JSON.parse(xhr.response).date);
       h2Title.textContent=(JSON.parse(xhr.response).celebrations.length);
     };
     xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/06');
     xhr.send();
}
