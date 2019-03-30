import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    auth_login: false,
    username: '',
    password: '',
    remeber_login: false
  },
  mutations: {
    account_sign_in (state, params) {
      console.log('Store sign in');
      state.auth_login = true;
    },

    account_sign_out (state) {
      console.log('Store sign out');

      state.auth_login = false;
    }
  },
  actions: {

  }
})
