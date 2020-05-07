from mongoengine import *
import datetime

Users_type = (('m', 'Male'),
              ('f', 'Female'))


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


class Instrument(EmbeddedDocument):
    name = StringField(required=True, unique=True)
    i_type = StringField(max_length=3, choices=Instrument_type)


class Users(Document):
    username = StringField(required=True, unique=True)
    name = StringField(max_length=30)
    age = IntField()
    gender = StringField(max_length=1, choices=Users_type)
    timestamp = DateTimeField(default=datetime.datetime.now)
    followers = ListField(StringField(max_length=30, unique=True))
    following = ListField(StringField(max_length=30, unique=True))
    objects = QuerySetManager()
    isMusician = BooleanField(default=False)
    inst = ListField(EmbeddedDocumentField(Instrument))
    genres = ListField(EmbeddedDocumentField(Genre))


class Track(Document):
    name = StringField()
    url = URLField(url_regex=None)
    author = StringField(required=True)
    #comments = ListField(EmbeddedDocumentField(Comments))
    likes = IntField(default=0)
    objects = QuerySetManager()
    inst_used = ListField(EmbeddedDocumentField(Instrument))
    inst_void = ListField(EmbeddedDocumentField(Instrument))


class Playlist(Document):

    name = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)
    p_type = StringField(default="User")
    track_list = ListField(Track.author)
