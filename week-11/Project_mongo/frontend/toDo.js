'use strict';

const inputdata = document.querySelector('.button-input');
const AddButton = document.querySelector('.button-text');
const host = 'http://localhost:3000/todos/';
AddButton.addEventListener('click', addNewElement);


function display(method, response) {
  if (method === 'GET' || method === 'POST') {
    response.forEach(function (e) { addli(e)});
  } else if (method === 'DELETE') {
    deleteDisplay(response)
  } else if (method === 'PUT') {
    completeDisplay(response);
  }
}

function deleteDisplay(response){
  let li = document.querySelector('#i' + response.id);
  let ul = document.querySelector('ul');
  ul.removeChild(li);
}

function completeDisplay(response){
  let li=document.querySelector('#i' + response.id);
  let button=document.querySelector('#c' + response.id);
  if (response.completed){
    li.classList.add('done');
    button.classList.add('done');
  } else {
    li.classList.remove('done');
    button.classList.remove('done');
  }
}

function xhrRequest(method, url, data, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url, true);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(data);
  xhr.onload = function () {
    if (xhr.readyState === xhr.DONE) {
      callback(xhr.response);
    }
  }
}

function get() {
  xhrRequest('GET', host, '', function(response) {
    display('GET', JSON.parse(response));
  })
}

function addNewElement() {
  if (inputdata.value !== ''){
  xhrRequest('POST', host, JSON.stringify({ text: inputdata.value }),
    function(response) { addli(JSON.parse(response));
    }
  )
}}

function completeTask(event) {
  xhrRequest('PUT', host + getServerId(event),
  JSON.stringify({ id: event.target.id, completed: true }), function(response) {
    display('PUT', JSON.parse(response));
  })
}

function deleteTask(event) {
  xhrRequest('DELETE', host + getServerId(event), JSON.stringify({ id: event.target.id, destroyed: true }), function(response) {
    display('DELETE', JSON.parse(response));
  })
}

function getServerId(event) {
  return event.target.id.slice(1, 10)
}

function addli(e) {
  console.log(e.destroyed);
  if (e.destroyed !== true) {
    const ul = document.querySelector('ul');
    const li = document.createElement('li');
    li.textContent = e.text;
    li.setAttribute('id', 'i' + e.id);
    createDeleteButton (li, e);
    createCompleteButton (li, e);
    if (e.completed === true) {
      li.classList.add('done')
    }
    ul.appendChild(li);
}}

function createDeleteButton (li,e) {
  let deleteButton = document.createElement('BUTTON');
  deleteButton.setAttribute('id', 'd' + e.id);
  deleteButton.addEventListener('click', function(event){deleteTask(event)});
  deleteButton.classList.add('deletebutton');
  li.appendChild(deleteButton);
}

function createCompleteButton (li,e) {
  let completeButton = document.createElement('BUTTON');
  completeButton.setAttribute('id', 'c' + e.id);
  completeButton.addEventListener('click', function(event){completeTask(event)});
  completeButton.classList.add('completebutton');
  if (e.completed === true) {
    completeButton.classList.add('done')
  }
  li.appendChild(completeButton);
}

get();
