'use strict';

var imageList = [
  'images/1.jpg',
  'images/2.jpg',
  'images/3.jpg',
  'images/4.jpg',
  'images/5.jpg',
  'images/6.jpg',
  'images/7.jpg'];

var titleList = [
  '0 kép',
  '1 kép',
  '2 kép',
  '3 kép',
  '4 kép',
  '5 kép',
  '6 kép'];

var mainImage = document.querySelector('.picture');
var smallImage = document.querySelectorAll('.small_picture');
var imageIndex = 0;
var smallimageIndex = 0;
var leftBigButton = document.querySelector('.left_big');
var rightBigButton = document.querySelector('.right_big');
var leftSmallButton = document.querySelector('.left_small');
var rightSmallButton = document.querySelector('.right_small');
var h1Title = document.querySelector('h1');

leftBigButton.addEventListener('click', back);
rightBigButton.addEventListener('click', foward);
leftSmallButton.addEventListener('click', smallBack);
rightSmallButton.addEventListener('click', smallFoward);
drawing();


function drawing() {
  mainImage.setAttribute('src', imageList[0]);
  imageList.forEach(
    function (e, i) {
      if (i < 4) {
        smallImage[i].setAttribute('src', e);
        smallImage[i].setAttribute('data-index', i);
        smallImage[i].addEventListener('click', events );
      }
    }
  );
  imgTitle();
}

function events(event) {
  changeImage(event.target.getAttribute('src'));
  imageIndex = parseInt(event.target.getAttribute('data-index'))
  imgTitle();
}

function changeImage(image) {
  mainImage.setAttribute('src', image);
}

function smallChangeImage(image, position) {
  smallImage[position].setAttribute('src', image);
}

function smallBack() {
  if (smallimageIndex > 0) {
    smallimageIndex--;
    for (var i = 0; i < 5; i++) { smallChangeImage(imageList[smallimageIndex + i], i);
    smallImage[i].setAttribute('data-index', smallimageIndex + i); 
    }
  }
}

function smallFoward() {
  if (smallimageIndex < imageList.length - 4 ) {
    smallimageIndex++;
    for (var i = 0; i < 5; i++) { smallChangeImage(imageList[smallimageIndex + i], i);
    smallImage[i].setAttribute('data-index', smallimageIndex + i); }
  }
}

function imgTitle() {
  h1Title.textContent = titleList[imageIndex];
}

function foward() {
  if (imageIndex < imageList.length - 1) {
    imageIndex++;
  }
  else {
    imageIndex = 0;
  }
  changeImage(imageList[imageIndex]);
  imgTitle();
}

function back() {
  if (imageIndex > 0) {
    imageIndex--;
  }
  else {
    imageIndex = imageList.length - 1;
  }
  changeImage(imageList[imageIndex]);
  imgTitle();
}
