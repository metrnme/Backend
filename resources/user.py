from flask import Response, request, jsonify
from database.models import Users
from database.db import connect_db
from flask_restful import Resource
from flask_jwt_extended import JWTManager


class UsersApi(Resource):  # for USERS
    def get(self):
        data = dict()
        counter = 0
        for user in Users.objects:
            data.setdefault(counter, user.to_json())
            counter += 1
        return {'status': 200, 'content': data}


class UserApi(Resource):  # for USER
    def post(self):
        # try:
        # username = request.args.get('username')
        # name = request.args.get('name')
        # gender = request.args.get('gender')
        # age = request.args.get('age')
        #   print(username, name, gender, age)
        # Create a link-based post
        # post = Users(username=username, name=name, gender=gender, age=age)
        # post.save()
        # return {'status': 201, 'message': 'User has been sucessfully created!'}

        try:
            data = request.get_json(force=True)
            post = Users(username=data['username'], name=data['name'],
                         age=data['age'], gender=data['gender'])
            post.save()
            return {'status': 201, 'message': 'user has been sucessfully posted!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Username already exists!, please try coming up with a different username!'}

    def delete(self):
        try:
            data = request.get_json(force=True)
            u = Users.objects.get(username=data['username'])
            u.delete()
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


class NewUserApi(Resource):  # for USER
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Users(username=data['username'])
            post.save()
            return {'status': 201, 'message': 'user has been sucessfully posted!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Username already exists!, please try coming up with a different username!'}


class FollowApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            to_u = Users.objects.get(username=data["to"])
            from_me = Users.objects.get(username=data["from"])
            message = "Failed to follow "+data["to"]+"by"+data["from"]

            if(len(to_u.followers) == 0) and (len(from_me.following) == 0):
                message = self.addFollower(
                    to_u, from_me, data["to"], data["from"])
            elif(len(to_u.followers) > 0 and len(from_me.following) == 0):
                for users in to_u.followers:
                    if users != data["from"]:
                        to_u.followers.append(data["from"])
                from_me.following.append(data["to"])
                from_me.save()
                to_u.save()
                message = "case 2 success"
            elif(len(to_u.followers) == 0 and len(from_me.following) > 0):
                for users in from_me.following:
                    if users != data["to"]:
                        from_me.following.append(data["to"])
                to_u.followers.append(data["from"])
                from_me.save()
                to_u.save()
                message = "case 3 sucess"
            else:
                for users in to_u.followers:
                    if(users != data["from"]):
                        to_u.following.append(data["from"])
                        to_u.save()
                for users in from_me.following:
                    if(users != data["to"]):
                        from_me.followers.append(data["to"])
                        from_me.save()

            return {"status": 200, "message": message}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def addFollower(self, to_u, from_me, a, b):
        to_u.followers.append(b)
        from_me.following.append(a)
        to_u.save()
        from_me.save()
        return "Successfully followed" + b+" by "+a
