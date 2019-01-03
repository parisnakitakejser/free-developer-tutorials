var devConfig = require('./webpack.config.js');

devConfig['mode'] = 'production';
devConfig['watch'] = false;

module.exports = devConfig
