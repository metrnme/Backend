from resources.user import UserApi, UsersApi
from resources.comment import CommentApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/v1/users')
    api.add_resource(UserApi, '/api/v1/user')
    api.add_resource(CommentApi, '/api/v1/comment')
#    api.add_resource(SignupApi, '/api/auth/signup')
#    api.add_resource(LoginApi, '/api/auth/login')
