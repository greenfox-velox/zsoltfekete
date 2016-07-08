'use strict';

var inputdata = document.querySelector('.button-input');
var AddButton = document.querySelector('.button-text');
var linkGet = 'https://mysterious-dusk-8248.herokuapp.com/todos';
AddButton.addEventListener('click',addNewElement);

get();

function display(get,del,com){
  if (get !== null) {
    get.forEach(function(e) { addli(e)})
    var allli=document.querySelectorAll('li')
  } else if (del !== null) {
    var li=document.querySelector('#i'+del.id)
    var ul=document.querySelector('ul')
    ul.removeChild(li);
  } else if (com!== null) {
    var li=document.querySelector('#i'+com.id);
    var button=document.querySelector('#c'+com.id);
    li.classList.add('done')
    button.classList.add('done')
  }
}

function get(){
  var xhr = new XMLHttpRequest();
  xhr.open('GET', linkGet);
  xhr.send();
  xhr.onload = function() {
    if (xhr.readyState === xhr.DONE) {
      display(JSON.parse(xhr.response),null,null);
    }
  }
}

function addNewElement(){
  var xhradd = new XMLHttpRequest();
  xhradd.open('POST', linkGet);
  xhradd.setRequestHeader("content-type","application/json");
  xhradd.send(JSON.stringify({"text" : inputdata.value }));
  xhradd.onload = function() {
    if (xhradd.readyState === xhradd.DONE) {
      addli(JSON.parse(xhradd.response));
    }
  }
}

function completeTask(event){
  var targetid = event.target.id;
  var serveridcom= targetid.slice(1,10)
  var text = event.target;
  var xhrmod = new XMLHttpRequest();
  xhrmod.open('PUT', linkGet + '/' + serveridcom);
  xhrmod.setRequestHeader("content-type",'application/json');
  xhrmod.onload = function() {
    if (xhrmod.readyState === xhrmod.DONE) {
      display(null,null,JSON.parse(xhrmod.response))
    }
  }
  xhrmod.send(JSON.stringify({"text" : text, "completed": true }));
}

function deleteTask(event){
  var targetid = event.target.id;
  var xhrdel = new XMLHttpRequest();
  var serveriddel= targetid.slice(1,10)
  xhrdel.open('DELETE', linkGet + '/' + serveriddel);
  xhrdel.setRequestHeader("content-type",'application/json');
  xhrdel.onload = function() {
    if (xhrdel.readyState === xhrdel.DONE) {
      display(null,JSON.parse(xhrdel.response),null)
    }
  }
  xhrdel.send();
}

function addli (e) {
  var ul = document.querySelector("ul");
  var li = document.createElement("li");
  li.textContent = e.text;
  li.setAttribute('id','i' + e.id);
  createDeleteButton (li,e);
  createCompleteButton (li,e);
  if (e.completed){li.classList.add('done')}
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
    if (e.completed){completeButton.classList.add('done')}
  li.appendChild(completeButton);
}
