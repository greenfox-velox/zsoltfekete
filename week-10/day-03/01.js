'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');

function countWords (fileName,callback) {
  fs.readFile(fileName,function(error, content){
    if (error) {
      return callback(err);
    }
    callback(null, String(content).split(/\s/g).length-1);
  });
}

countWords ('apple.txt', function(error,content) {
  console.log(error,content);
});
