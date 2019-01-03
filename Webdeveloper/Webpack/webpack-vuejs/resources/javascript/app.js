import Vue from 'vue';
import HelloWorld from '../vue/hello-world.vue';

console.log('App laoder');

new Vue({
  el: '#app-hello-world',
  render: h => h(HelloWorld)
});
