var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';
var path_obj = require('path');

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
      test: /\.json$/,
      exclude: /node_modules/,
      loader: path_obj.resolve('resources/loaders/custom-loader.js')
    }]
  }
}
