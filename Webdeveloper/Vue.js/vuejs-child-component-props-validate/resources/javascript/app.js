import Vue from 'vue';
import HelloVue from '../vue/hello-vue.vue';

console.log('App laoder');

new Vue({
  el: '#app',
  render: h => h(HelloVue)
});
