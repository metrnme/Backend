from resources.user import UserApi, UsersApi, NewUserApi, FollowApi
from resources.comment import CommentApi
from resources.instrument import InstrumentApi, InstrumentUserApi
from resources.playlist import PlaylistApi
from resources.counter import CounterApi
from resources.track import TrackApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/v1/users')
    api.add_resource(UserApi, '/api/v1/user')
    api.add_resource(NewUserApi, '/api/v1/n_user')
    api.add_resource(FollowApi, '/api/v1/follow')
    api.add_resource(CommentApi, '/api/v1/comment')
    api.add_resource(InstrumentApi, '/api/v1/inst')
    api.add_resource(InstrumentUserApi, '/api/v1/user/inst')
    api.add_resource(TrackApi, '/api/v1/user/trk')
    api.add_resource(CounterApi, '/api/v1/counter')
    api.add_resource(PlaylistApi, '/api/v1/play')
#    api.add_resource(SignupApi, '/api/auth/signup')
#    api.add_resource(LoginApi, '/api/auth/login')
