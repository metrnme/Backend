from mongoengine import connect


def connect_db():
    client = connect(
        host='mongodb+srv://test:test1@mtrnme-yr9b5.mongodb.net/mtrnme?retryWrites=true&w=majority')
    return client.db


'''
Multi Line Comment
'''
