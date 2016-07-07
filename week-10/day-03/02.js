'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

var fs = require('fs');

function letterCount(fileName, letter, callback) {
  fs.readFile(fileName,function(error, content){
    if (error) {
      return callback(error);
    }
    var counter = 0;
    String(content).split('').forEach(function(e) {
      if (e === letter) {
        counter++;
      }
    });
    callback(null, counter);
  });
}

letterCount('apple.txt', 'a', function(error, c) {
  console.log(error, c);
})
