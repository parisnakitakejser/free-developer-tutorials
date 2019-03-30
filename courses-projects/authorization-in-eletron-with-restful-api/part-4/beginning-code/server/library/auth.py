import falcon
import time
from bson.json_util import dumps

from library import init_config, init_mongodb_conn

class Login(object):
    def on_post(self, req, resp):
        start_time = time.time()

        config = init_config()
        resp.status = falcon.HTTP_200

        conn = init_mongodb_conn(config['mongodb']['database'])
        data = req.media

        account = conn['users'].find_one({
            'email': data['username']
        })

        if account:
            if account['password'] == data['password']:
                resualt = {
                    'token': account['token'],
                    'name': account['name']
                }
            else:
                resp.status = falcon.HTTP_UNAUTHORIZED
                resualt = None
        else:
            resualt = None
            resp.status = falcon.HTTP_UNAUTHORIZED

        data_output = {
            'ip': req.access_route,
            'exec_time': str((time.time() - start_time)),
            'resualt': resualt
        }

        resp.body = dumps(data_output)
