var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';

module.exports = {
  mode: 'development',
  watch: true,
  entry: {
    'app' : path + 'app.js',
    'login': path + 'login.js'
  },
  output: {
    path: output_path,
    filename: '[name].bundle.js'
  },

  module: {
    rules: [{
      test: /\.css$/,
      exclude: /node_modules/,
      loader: 'style-loader!css-loader'
    }]
  }
}
