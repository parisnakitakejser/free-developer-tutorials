import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import auth from './middleware/auth.js';

Vue.config.productionTip = false;

const HomeComponent = () => import('./components/HomeComponent.vue');
const AccountComponent = () => import('./components/AccountComponent.vue');

// import HomeComponent from './components/HomeComponent.vue';
// import AccountComponent from './components/AccountComponent.vue';

Vue.use(VueRouter);

const routers = [{
  name: 'Home',
  path: '/',
  component: HomeComponent
},{
  name: 'Account',
  path: '/account',
  component: AccountComponent,
  meta: {
    middleware: [auth]
  }
}];

const router = new VueRouter({mode: 'history', routes: routers});

function nextFactory(context, middleware, index) {
  const subsequentMiddleware = middleware[index];

  if(!subsequentMiddleware) {
    return context.next;
  }

  return (...parameters) => {
    context.next(...parameters);
    const nextMiddleware = nextFactory(context, middleware, index + 1);
    subsequentMiddleware({...context, next: nextMiddleware});
  }
}

router.beforeEach((to, from, next) => {
  if (to.meta.middleware) {
    const middleware = Array.isArray(to.meta.middleware) ? to.meta.middleware : [to.meta.middleware];
    const context = {from, next, router, to};
    const nextMiddleware = nextFactory(context, middleware, 1);

    return middleware[0]({...context, next: nextMiddleware});
  }

  return next();
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
