from pymongo import MongoClient

mongodb_host = 'localhost'
mongodb_port = '27017'

client = MongoClient(mongodb_host +':'+ mongodb_port)
db = client['python-mongo-test']

try:
    document = {
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    }

    db['test-entry'].insert(document)

    print str(document['_id'])

except:
    print 'this connection or insert are wrong.'
