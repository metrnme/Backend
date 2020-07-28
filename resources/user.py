from flask import Response, request, jsonify
from database.models import Users
from database.db import connect_db
from flask_restful import Resource


class AllUsersApi(Resource):  # for USERS
    def get(self):
        data = dict()
        counter = 0
        for user in Users.objects:
            data.setdefault(counter, user.to_json())
            counter += 1
        return {'status': 200, 'content': data}


class UserDataApi(Resource):  # for USER
    def put(self):
        try:
            data = request.get_json(force=True)
            u=Users.objects.get(username=data['username'])
            u.name=data['name']
            u.age=data['age']
            u.gender=data['gender']
            u.save()
            return {'status': 201, 'message': 'User Information has been sucessfully updated!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': e}

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


class CreateUserApi(Resource):  # for USER
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Users(username=data['username'])
            post.save()
            return {'status': 201, 'message': 'user has been sucessfully posted!'}

        except Exception as e:
            print(e)
            return {'status': 300, 'message': 'Username already exists!, please try coming up with a different username!'}



class FollowApi(Resource):
    def put(self):
        try:
            data = request.get_json(force=True)
            to_u = Users.objects.get(username=data["to"])
            from_me = Users.objects.get(username=data["from"])
            message = data["from"]+" is already following "+data["to"]

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
                message = data["from"]+" started following "+data["to"]
            elif(len(to_u.followers) == 0 and len(from_me.following) > 0):
                for users in from_me.following:
                    if users != data["to"]:
                        from_me.following.append(data["to"])
                to_u.followers.append(data["from"])
                from_me.save()
                to_u.save()
                message = data["from"]+" started following "+data["to"]
            else:
                for users in to_u.followers:
                    if(users != data["from"]):
                        to_u.followers.append(data["from"])
                        to_u.save()
                for users in from_me.following:
                    if(users != data["to"]):
                        from_me.following.append(data["to"])
                        from_me.save()
                message = data["from"]+" started following "+data["to"]
                
            return {"status": 200, "message": message}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def addFollower(self, to_u, from_me, a, b):
        to_u.followers.append(b)
        from_me.following.append(a)
        to_u.save()
        from_me.save()
        return "Successfully followed " + b+" by "+a
