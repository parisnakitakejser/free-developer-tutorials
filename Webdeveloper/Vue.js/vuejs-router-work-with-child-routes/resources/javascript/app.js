import Vue from 'vue';
import App from '../vue/app.vue';
import VueRouter from 'vue-router';

import HomeComponent from '../vue/HomeComponent.vue';
import AboutComponent from '../vue/AboutComponent.vue';
import ContactComponent from '../vue/ContactComponent.vue';
import AboutMeComponent from '../vue/AboutMeComponent.vue';
import AboutDogComponent from '../vue/AboutDogComponent.vue';

Vue.use(VueRouter);

const routers = [{
    name: 'Home',
    path: '/',
    component: HomeComponent
},{
    name: 'About',
    path: '/about',
    component: AboutComponent,
    children: [{
      name: 'AboutMe',
      path: 'me',
      component: AboutMeComponent
    },{
      name: 'AboutDog',
      path: 'dog',
      component: AboutDogComponent
    }]
},{
    name: 'Contact',
    path: '/contact',
    component: ContactComponent
}]

const router = new VueRouter({mode: 'history', routes: routers})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
