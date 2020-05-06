from mongoengine import *
import datetime


class Users(Document):
    username = StringField(required=True, unique=True)
    name = StringField(max_length=30)
    age = IntField()
    gender = StringField(max_length=1)
    timestamp = DateTimeField(default=datetime.datetime.now)
    followers = ListField(StringField(max_length=30))
    objects = QuerySetManager()


class Comments(EmbeddedDocument):
    content = StringField(max_length=120)
    timestamp = DateTimeField(default=datetime.datetime.now)
    objects = QuerySetManager()


class Likes(Document):
    count = IntField()
    objects = QuerySetManager()


class Track(Document):
    name = StringField()
    url = URLField(url_regex=None)
    comments = ListField(EmbeddedDocumentField(Comments))
    likes = ReferenceField(Likes)
    objects = QuerySetManager()
