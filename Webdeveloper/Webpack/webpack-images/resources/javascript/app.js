console.log('App loader');

var img = document.createElement('img');
img.style.height = '100px';
img.style.width = '100px';
img.src = require('../images/webpack.png');

var element = document.getElementById('img_container');
element.appendChild(img);
