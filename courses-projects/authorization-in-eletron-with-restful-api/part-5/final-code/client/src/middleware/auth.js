import store from '@/store';
import cookies from 'vue-cookies';

export default function auth({next, router}) {
    console.log('hit middleware here');

    const verify_token = (cookies.get('auth') !== 'null' ? cookies.get('auth') : null);

    if (verify_token) {
        store.commit('account_sign_in', {
            'verify_token': true
        });
    } else {
        store.commit('account_sign_out');
    }

    return next();
}