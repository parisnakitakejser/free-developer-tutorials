import store from '@/store';
import cookies from 'vue-cookies';
import axios from 'axios';

export default function auth({next, router}) {
    console.log('hit middleware here');

    const verify_token = (cookies.get('auth') !== 'null' ? cookies.get('auth') : null);

    if (verify_token) {
        axios.post(process.env.VUE_APP_API_URL +'/verify-token', {
            'auth': verify_token
        })
        .then((result) => {
            console.log('token success')

            store.commit('account_sign_in', {
                'verify_token': true
            });
        })
        .catch((error) => {
            console.log('token failure')

            store.commit('account_sign_out');
        })
    } else {
        store.commit('account_sign_out');
    }

    return next();
}