module.exports = function(source) {
  this.cacheable();

  console.log(source);

  return source;
}
