from mongoengine import *
import datetime

Users_type = (('m', 'Male'),
              ('f', 'Female'),
              (' ', 'Undefined'))


class Genre(EmbeddedDocument):
    genres_name = StringField(max_length=30, unique=True, required=True)


class CommentsQuerySet(QuerySet):
    def getAllComments(self, id):
        return self.filter(track_id=id)


class Comments(Document):
    track_id = IntField(required=True)
    username = StringField(max_length=30, required=True)
    content = StringField(max_length=120)
    timestamp = DateTimeField(default=datetime.datetime.now)
    vote = IntField(default=0)

    objects = QuerySetManager()
    meta = {'queryset_class': CommentsQuerySet}


Instrument_type = (('PER', 'Percussions'),
                   ('STR', 'Strings'),
                   ('BRS', 'Brass'),
                   ('KYS', 'Keys'),
                   ('HRN', 'Horns'))


class Instruments(Document):
    name = StringField(required=True, unique=True)
    i_type = StringField(max_length=3, required=True, choices=Instrument_type)
    objects = QuerySetManager()


class Users(Document):
    username = StringField(required=True, unique=True)
    name = StringField(max_length=30, default="")
    age = IntField(default=0)
    gender = StringField(max_length=1, choices=Users_type, default=" ")
    timestamp = DateTimeField(default=datetime.datetime.now)
    followers = ListField(StringField(max_length=30))
    following = ListField(StringField(max_length=30))
    isMusician = BooleanField(default=False)
    inst = ListField(StringField(unique=True))
    #genres = ListField(EmbeddedDocumentField(Genre))
    objects = QuerySetManager()


class Counter(Document):
    collection = StringField(unique=True)
    counter = IntField(default=0)
    objects = QuerySetManager()


class Track(Document):
    track_id = IntField(unique=True)
    name = StringField()
    url = StringField(unique=True)
    username = StringField(required=True)
    #comments = ListField(EmbeddedDocumentField(Comments))
    likes = IntField(default=0)
    objects = QuerySetManager()
    #inst_used = ListField(EmbeddedDocumentField(Instruments))
    #inst_void = ListField(EmbeddedDocumentField(Instruments))


class Playlist(Document):
    p_username = StringField(required=True)
    name = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)
    p_type = StringField(default="User")
    track_list = ListField(StringField(unique=True, max_length=150))
