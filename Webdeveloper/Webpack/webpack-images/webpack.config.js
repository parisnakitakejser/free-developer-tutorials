var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';

module.exports = {
  mode: 'development',
  watch: true,
  entry: {
    'app' : path + 'app.js'
  },
  output: {
    path: output_path,
    filename: '[name].bundle.js'
  },

  module: {
    rules: [{
      test: /\.(png|jpg)$/,
      exclude: /node_modules/,
      loader: 'url-loader',
      options: {
        limit: 10000,
        name: '../images/[name].[ext]',
        publicPath: './iamges/'
      }
    }]
  }
}
