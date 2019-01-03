var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';
var path_obj = require('path');

const {VueLoaderPlugin} = require('vue-loader');

module.exports = {
  mode: 'development',
  watch: true,
  entry: {
    'app' : path + 'app.js',
  },
  output: {
    path: output_path,
    filename: '[name].bundle.js'
  },

  module: {
    rules: [{
      test: /\.vue$/,
      loader: 'vue-loader',
      exclude: /node_modules/
    }, {
      test: /\.js$/,
      loader: 'babel-loader',
      exclude: /node_modules/
    }]
  },

  plugins: [
    new VueLoaderPlugin(),
  ]
}
