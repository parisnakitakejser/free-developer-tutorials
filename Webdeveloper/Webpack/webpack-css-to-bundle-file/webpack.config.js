var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';

const ExtractTextPlugin = require('extract-text-webpack-plugin');

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

  module:{
    rules:[{
      test: /\.css$/,
      exclude: /node_modules/,
      loader: ExtractTextPlugin.extract({
        use: 'css-loader',
        fallback: 'style-loader'
      })
    }]
  },

  plugins: [
    new ExtractTextPlugin("stylesheets/[name].bundle.css")
  ]
}
