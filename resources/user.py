from flask import Response, request, jsonify
from database.models import Users, Comments
from flask_restful import Resource


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
            resp = jsonify(
                {'status': 409, 'error_message': 'Username already exists!, please try another coming up with a different username!'})
            return resp

    def delete(self, id):
        # user_id = get_jwt_identity()
        user = Users.objects.get(id=id)
        user.delete()
        return Response(status=200, mimetype='application/json')

    def get(self):
        try:
            username = request.headers.get('User-Agent')
            result = Users.objects.get(username=username)
            json_data = result.to_json()
            return {'status': 200, 'content': json_data}
        except Exception as e:
            print(e)
            resp = jsonify(
                {'status': 404, 'error_message': 'The User Searched does not exist!'})
            return resp


class CommentApi(Resource):
    def post(self):
        print("Post a Comment")

    def get(self, id):
        print("Get a Comment")

    def delete(self, id):
        print("Delete a Comment")

    def update(self, id):
        print("Update a Comment")
