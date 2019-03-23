export default function auth({next, router}) {
    console.log('middleware auth test');
    const account_auth = true;
    if(!account_auth) {
        return router.push({name: 'Home'});
    }

    return next();
}