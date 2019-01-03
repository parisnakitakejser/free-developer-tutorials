var path = './resources/javascript/';
var output_path = __dirname +'/public/assets/';

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
      test: /\.css$/,
      exclude: /node_modules/,
      loader: 'style-loader!css-loader'
    },{
      test: /\.(woff|woff2|eot|ttf|svg)$/,
      exclude: /node_modules/,
      loader: 'url-loader',
      options: {
        publicPath: './fonts/',
        name: '../fonts/[name].[ext]',
        limit: 1000
      }
    }]
  }
}
