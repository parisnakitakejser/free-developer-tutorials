import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import cookies from 'vue-cookies';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    auth_login: true,
    username: '',
    password: '',
    remeber_login: false
  },
  mutations: {
    account_sign_in (state, params) {
      console.log('Store sign in');

      console.log(params);

      if (params.verify_token) {
        cookies.set('auth', cookies.get('auth'));
        state.auth_login = true;
      } else {
        axios.post(process.env.VUE_APP_API_URL + '/login', {
          username: params.username,
          password: params.password
        }).then((result) => {
          console.log(result.data)

          cookies.set('auth', {
            'name': result.data.resualt.name,
            'token': result.data.resualt.jwt
          });

          state.auth_login = true;
        })
        .catch((error) => {

        });
      }
    },

    account_sign_out (state) {
      console.log('Store sign out');

      cookies.remove('auth');
      state.auth_login = false;
    }
  },
  actions: {

  }
})
