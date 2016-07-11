'use strict';

var inputdata = document.querySelector('.button-input');
var AddButton = document.querySelector('.button-text');
var linkGet = 'https://mysterious-dusk-8248.herokuapp.com/todos';
AddButton.addEventListener('click', addNewElement);

function display(method, response){
  if (method === 'GET' || method === 'POST') {
    response.forEach(function (e) { addli(e)})
    var allli = document.querySelectorAll('li');
  } else if (method === 'DELETE') {
    var li = document.querySelector('#i' + response.id)
    var ul = document.querySelector('ul')
    ul.removeChild(li);
  } else if (method === 'PUT') {
    var li=document.querySelector('#i' + response.id);
    var button=document.querySelector('#c' + response.id);
    li.classList.add('done')
    button.classList.add('done')
  }
}

function xhrRequest(method, url, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url, true);
  xhr.setRequestHeader("content-type", 'application/json');
  xhr.send(data);
  xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
      callback(xhr.response);
    }
  }
}

function get() {
  xhrRequest('GET', linkGet, '', function(response) {
    display('GET',JSON.parse(response));
    }
  )
}

function addNewElement(){
  xhrRequest('POST', linkGet, JSON.stringify({"text" : inputdata.value }),
    function(response) {addli(JSON.parse(response));
    }
  )
}

function completeTask(event){
  xhrRequest('PUT', linkGet + '/' + getServerId(event),
  JSON.stringify({"text" : event.target, "completed": true }), function(response) {
    display('PUT',JSON.parse(response));
    }
  )
}

function deleteTask(event){
  xhrRequest('DELETE', linkGet + '/' + getServerId(event),'',function(response) {
    display('DELETE',JSON.parse(response));
    }
  )
}

function getServerId (event){
  return event.target.id.slice(1,10)
}

function addli (e) {
  var ul = document.querySelector("ul");
  var li = document.createElement("li");
  li.textContent = e.text;
  li.setAttribute('id','i' + e.id);
  createDeleteButton (li,e);
  createCompleteButton (li,e);
  if (e.completed){
    li.classList.add('done')
  }
  ul.appendChild(li);
}

function createDeleteButton (li,e) {
  var deleteButton = document.createElement("BUTTON");
  deleteButton.setAttribute('id','d' + e.id);
  deleteButton.addEventListener('click', function(event){deleteTask(event)});
  deleteButton.classList.add('deletebutton');
  li.appendChild(deleteButton);
}

function createCompleteButton (li,e) {
  var completeButton = document.createElement("BUTTON");
  completeButton.setAttribute('id','c'+e.id);
  completeButton.addEventListener('click', function(event){completeTask(event)});
  completeButton.classList.add('completebutton');
    if (e.completed){
      completeButton.classList.add('done')
    }
  li.appendChild(completeButton);
}

get();
