'use strict';

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9 , books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

// create a function that counts all the books of an array of students
// not every student has a property called books

// function  bookCounter(lista) {
//   return lista.reduce(function(book,next){
//     book[next] = (book && book.length) || 0
//     return book;
//   },(0));
// }


function bookCounter(lista) {
  var book = 0;
  lista.forEach(function (e) {book +=(e.books && e.books.length) || 0})
    return book
}

console.log(bookCounter(students));

module.exports.bookCounter = bookCounter;
