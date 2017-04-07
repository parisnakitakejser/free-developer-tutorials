from pymongo import MongoClient

mongodb_host = 'localhost'
mongodb_port = '27017'

client = MongoClient(mongodb_host +':'+ mongodb_port)
db = client['python-mongo-test']

try:
    document = []

    document.append({
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    })

    document.append({
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    })

    document.append({
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    })

    document.append({
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    })

    document.append({
        'name' : 'paris',
        'age' : 31,
        'hobby' : 'computer'
    })



    print document
    print ''
    db['test-entry'].insert(document)
    print 'insert {len}'.format(len=len(document))
    print document

except:
    print 'this connection or insert are wrong.'
