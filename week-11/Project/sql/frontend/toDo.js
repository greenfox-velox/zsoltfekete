'use strict';

const inputdata = document.querySelector('.button-input');
const AddButton = document.querySelector('.button-text');
const host = 'http://localhost:3002/todos/';
AddButton.addEventListener('click', addNewElement);

function display(method, response) {
  if (method === 'GET' || method === 'POST') {
    response.forEach(function (e) {addli(e)});
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

function checkstatus(li,button){

  if (Boolean(li.classList.length)){
    li.classList.remove('done');
    button.classList.remove('done');
 } else  {
   li.classList.add('done');
   button.classList.add('done');
 }
}

function completeDisplay(response){
  let li=document.querySelector('#i' + response.id);
  let button=document.querySelector('#c' + response.id);
  checkstatus(li,button)
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
  inputdata.value = '';
}}

function completeTask(event) {
  xhrRequest('PUT', host + getServerId(event),
  JSON.stringify({ id: event.target.id, completed: completedStatus(event) }), function(response) {
    display('PUT', JSON.parse(response));
  })
}

function completedStatus(event) {
  if (event.target.classList.length === 1) {
    return true
  }
  return false
}

function deleteTask(event) {
  xhrRequest('DELETE', host + getServerId(event),
  JSON.stringify({ id: event.target.id, destroyed: true }),function(response) {
    display('DELETE', JSON.parse(response));
  })
}

function getServerId(event) {
  return event.target.id.slice(1, 10)
}

function addli(e) {
  if (e.destroyed !== true && e.destroyed !== 1) {
    let ul = document.querySelector('ul');
    let li = document.createElement('li');
    li.textContent = e.text;
    li.setAttribute('id', 'i' + e.id);
    createDeleteButton (li, e);
    createCompleteButton (li, e);
    if (e.completed === true || e.completed === 1 ) {
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
  if (e.completed === true || e.completed === 1 ) {
    completeButton.classList.add('done')
  }
  li.appendChild(completeButton);
}

get();
