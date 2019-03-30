import falcon
from wsgiref import simple_server
from bson.json_util import dumps

from library import CORSComponent

class sample(object):
    def on_get(self, req, resp):
        data_output = {
            'hello': 'world'
        }

        resp.status = falcon.HTTP_200
        resp.body = dumps(data_output)

application = falcon.API(middleware=[
    CORSComponent()
])
application.add_route('/sample', sample())

if __name__ == '__main__':
    httpd = simple_server.make_server('', 8001, application)
    httpd.serve_forever()