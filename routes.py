from resources.user import UserApi, UsersApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/v1/users')
    api.add_resource(UserApi, '/api/v1/user')
