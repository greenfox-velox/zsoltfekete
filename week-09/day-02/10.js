'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

function Student() {
  this.grade_list = [];
  this.add_grade = function (grade) {
    this.grade_list.push(grade);
    return this.grade_list;
  };

  this.get_Average =function() {
    var avarage_grade = 0;
    this.grade_list.forEach(function(e) {avarage_grade += e});
    return avarage_grade/this.grade_list.length;
  }
}

var geza = new Student();
geza.add_grade(5);
geza.add_grade(3);
geza.add_grade(1);

console.log(geza.get_Average());
