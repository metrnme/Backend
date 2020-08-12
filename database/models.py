from mongoengine import *
import datetime

Users_type = (('m', 'Male'),
              ('f', 'Female'),
              (' ', 'Undefined'))


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
    bio = StringField(max_length=128)
    imgUrl = StringField()
    gender = StringField(max_length=1, choices=Users_type, default=" ")
    timestamp = DateTimeField(default=datetime.datetime.now)
    followers = ListField(StringField(max_length=30), unique=True)
    following = ListField(StringField(max_length=30), unique=True)
    isMusician = BooleanField(default=False)
    inst = ListField(StringField(unique=True))
    objects = QuerySetManager()


class Counter(Document):
    collection = StringField(unique=True)
    counter = IntField(default=0)
    objects = QuerySetManager()


class TrackUserQuerySet(QuerySet):
    def getAllUserTracks(self, id):
        return self.filter(username=id)

    def getOneTrack(self, id):
        return self.filter(track_id=id)


class Track(Document):
    track_id = IntField(unique=True)
    name = StringField()
    url = StringField(unique=True, required=True)
    image_url = StringField()
    username = StringField(required=True)
    likes = IntField(default=0)
    user_likes = ListField(StringField())
    inst_used = ListField(StringField(max_length=30))
    genre = ListField(StringField(max_length=30))
    objects = QuerySetManager()
    meta = {'queryset_class': TrackUserQuerySet}


class PlaylistQuerySet(QuerySet):
    def getAllPlaylist(self, id):
        return self.filter(username=id)


class Playlist(Document):
    pl_id = IntField(unique=True)
    username = StringField(required=True)
    name = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)
    p_type = StringField(default="User")
    track_list = ListField(IntField())
    objects = QuerySetManager()
    meta = {'queryset_class': PlaylistQuerySet}


class Genre(Document):
    name = StringField(required=True, unique=True)
    objects = QuerySetManager()
