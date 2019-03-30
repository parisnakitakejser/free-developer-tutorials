import falcon
from wsgiref import simple_server
from bson.json_util import dumps

from library import CORSComponent
from library.auth import Login as UserLogin, VerifyToken as UserVerifyToken

application = falcon.API(middleware=[
    CORSComponent()
])
application.add_route('/login', UserLogin())
application.add_route('/verify-token', UserVerifyToken())

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8001, application)
    httpd.serve_forever()