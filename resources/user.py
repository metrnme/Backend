from flask import Response, request, jsonify
from database.models import Users
from flask_restful import Resource
from flask_jwt_extended import JWTManager


class UsersApi(Resource):
    def get(self):
        try:
            sabkuch = Users.objects.all()
            counter = 1
            data = dict()
            for users in sabkuch:
                data.setdefault(counter, users.to_json())
                counter += 1
            print(data)

            return {'status': 200, 'content': data}
        except Exception as e:
            print(e)
            resp = jsonify(
                {'status': 404, 'error_message': e})
            return resp


class UserApi(Resource):
    def post(self):
        try:
            username = request.args.get('username')
            name = request.args.get('name')
            gender = request.args.get('gender')
            age = request.args.get('age')
            print(username, name, gender, age)
            # Create a link-based post
            post = Users(username=username, name=name, gender=gender, age=age)
            post.save()
            return {'status': 201, 'message': 'User has been sucessfully created!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Username already exists!, please try coming up with a different username!'}

    def delete(self):
        try:
            username = request.args.get('username')
            Users.objects.get(username=username).delete()
            return {'status': 201, 'message': 'User has been sucessfully deleted!'}
        except Exception as e:
            print(e)
            resp = jsonify(
                {'status': 404, 'error_message': 'Users matching query does not exist!'})
            return resp

    def get(self):
        try:
            data = request.get_json(force=True)
            result = Users.objects.get(username=data['username'])
            json_data = result.to_json()
            return {'status': 200, 'content': json_data}
        except Exception as e:
            print(e)
            resp = jsonify(
                {'status': 404, 'error_message': 'The User Searched does not exist!'})
            return resp
