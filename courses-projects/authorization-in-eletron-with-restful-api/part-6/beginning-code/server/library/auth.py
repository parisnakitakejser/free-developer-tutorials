import falcon
import time
from bson.json_util import dumps
from passlib.hash import pbkdf2_sha512
import jwt
from uuid import uuid4

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
            if pbkdf2_sha512.verify(data['password'], account['password']):
                token_uuid = uuid4()

                conn['users'].update({
                    '_id': account['_id']
                }, {
                    '$set': {
                        'token': str(token_uuid)
                    }
                })

                token_encode = jwt.encode({
                    'id': str(account['_id']),
                    'token': str(token_uuid)
                }, config['setting']['jwt_token'], algorithm='HS256')

                resualt = {
                    'jwt': token_encode,
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
