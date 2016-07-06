// Create a function that takes 3 parameters
// //  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

var fs = require('fs');


function ConcatTwoFile (FileName1, FileName2, callback) {
  fs.readFile(FileName1, function(error, content1){
    if (error) {
      return callback(error);
    }
    var newContent = String(content1);
    fs.readFile(FileName2, function(error, content2){
      if (error) {
        return callback(error);
      }
      newContent += String(content2);
      callback(null,newContent)
    });
  })
}

ConcatTwoFile( 'apple.txt', 'pearl.txt', function(error,newContent) {
  console.log(error,newContent);
});
