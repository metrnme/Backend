from flask import Response, request, jsonify
from database.models import Users
from database.db import connect_db
from flask_restful import Resource
import json


class AllUsersApi(Resource):  # for USERS
    def get(self):
        try:
            data = []
            for user in Users.objects:
                # Add all of this like this below i'll brb
                u = {"_id": {"$oid": "0"}, "username": user.username,  "name": user.name,
                     "age": user.age, "imgUrl": user.imgUrl, "gender": user.gender,  "followers": user.followers,
                     "following": user.following, "isMusician": user.isMusician, "bio": user.bio, "inst": user.inst}
                data.append(u)
                json_data = json.dumps(data, indent=2)

            resp = Response(json_data, status=200,
                            mimetype='application/json')
            return resp

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

        data = dict()
        counter = 0
        Users.objects
        for user in Users.objects:
            data.setdefault(counter, user.to_json())
            counter += 1
        return {'status': 200, 'content': data}


class UserDataApi(Resource):  # for USER
    def put(self):
        try:
            data = request.get_json(force=True)
            u = Users.objects.get(username=data['username'])
            u.name = data['name']
            u.age = data['age']
            u.gender = data['gender']
            u.bio = data['bio']
            u.imgUrl = data['imgUrl']
            u.save()
            json_data = {
                'status': 201, 'message': 'User Information has been sucessfully updated!'}
            return json_data

        except Exception as e:
            print(e)
            json_data = {'status': 409, 'message': str(e)}
            resp = Response(json_data, status=200, mimetype='application/json')
            return resp

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

    def post(self):
        try:
            data = request.get_json(force=True)
            result = Users.objects.get(username=data['username'])
            json_data = result.to_json()
            resp = Response(json_data, status=200, mimetype='application/json')
            return resp
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
            return {'status': 201, 'message': 'User has been sucessfully created!'}

        except Exception as e:
            print(e)
            return {'status': 300, 'message': 'Username already exists!, please try coming up with a different username!'}


class UsertypeApi(Resource):
    def post(self):
        data = request.get_json(force=True)
        u = Users.objects.get(username=data['username'])
        u.isMusician = data['usertype']
        u.save()
        return {'status': 201, 'message': 'User type has been updated!'}


class UnfollowApi(Resource):
    def put(self):
        try:
            data = request.get_json(force=True)
            username = data['from']
            user_to_unfollow = data['to']
            u = Users.objects.get(username=username)
            u2 = Users.objects.get(username=user_to_unfollow)
            message = username+" does not have "+user_to_unfollow+" in its following"
            if(user_to_unfollow in u.following):
                if(len(u.following) == 1):
                    u.following.append("default")
                if(len(u2.followers) == 1):
                    u2.followers.append("default")
                u.following.remove(user_to_unfollow)
                message = username+" has unfollowed "+user_to_unfollow
                u2.followers.remove(username)
            u.save()
            u2.save()
            return {"status": 200, "message": message}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


class FollowApi(Resource):
    def put(self):
        try:
            data = request.get_json(force=True)
            u = data["to"]
            me = data["from"]
            to_u = Users.objects.get(username=u)
            from_me = Users.objects.get(username=me)
            message = ""
            if (me in to_u.followers):
                message = me+" is already following "+u
            else:
                to_u.followers.append(me)
                from_me.following.append(u)
                message = me+" is now following "+u
                to_u.save()
                from_me.save()
            return {"status": 200, "message": message}

            #
            # to_u = Users.objects.get(username=data["to"])
            # from_me = Users.objects.get(username=data["from"])
            # message = data["from"]+" is already following "+data["to"]

            # if(len(to_u.followers) == 0) and (len(from_me.following) == 0):
            #     message = self.addFollower(
            #         to_u, from_me, data["to"], data["from"])
            # elif(len(to_u.followers) > 0 and len(from_me.following) == 0):
            #     for users in to_u.followers:
            #         if users != data["from"]:
            #             to_u.followers.append(data["from"])
            #     from_me.following.append(data["to"])
            #     from_me.save()
            #     to_u.save()
            #     message = data["from"]+" started following "+data["to"]
            # elif(len(to_u.followers) == 0 and len(from_me.following) > 0):
            #     for users in from_me.following:
            #         if users != data["to"]:
            #             from_me.following.append(data["to"])
            #     to_u.followers.append(data["from"])
            #     from_me.save()
            #     to_u.save()
            #     message = data["from"]+" started following "+data["to"]
            # else:
            #     for users in to_u.followers:
            #         if(users != data["from"]):
            #             to_u.followers.append(data["from"])
            #             to_u.save()
            #     for users in from_me.following:
            #         if(users != data["to"]):
            #             from_me.following.append(data["to"])
            #             from_me.save()
            #     message = data["from"]+" started following "+data["to"]

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
