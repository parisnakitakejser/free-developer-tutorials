from pymongo import MongoClient

mongodb_host = 'localhost'
mongodb_port = '27017'

client = MongoClient(mongodb_host +':'+ mongodb_port)
db = client['mongo-test']

print db
