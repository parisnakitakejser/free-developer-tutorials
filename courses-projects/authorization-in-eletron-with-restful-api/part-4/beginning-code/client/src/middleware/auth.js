import store from '@/store';

export default function auth({next, router}) {
    console.log('hit middleware here');
    store.commit('account_sign_out');
    return next();
}