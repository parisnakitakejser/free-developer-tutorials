import os
import configparser
from pymongo import MongoClient


def init_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    file_config = configparser.ConfigParser()
    file_config.read(f'{dir_path}/config.ini')

    return file_config


config = init_config()


def init_mongodb_conn(database):
    host = config['mongodb']['host']
    port = config['mongodb']['port']

    try:
        client = MongoClient(f'{host}:{port}')
        mongodb_conn = client[database]
    except ValueError as e:
        raise SystemExit('MongoDB connection to {host} is refused')

    return mongodb_conn


class CORSComponent(object):
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')

        if req_succeeded and req.method == 'OPTIONS' and req.get_header('Access-Control-Request-Method'):
            allow = resp.get_header('Allow')
            resp.delete_header('Allow')

            allow_headers = req.get_header('Access-Control-Request-Headers', default='*')

            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'),  # 24 hours
            ))