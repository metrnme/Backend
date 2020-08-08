from flask import Response, request, jsonify
from database.models import Track, Users, Counter
from flask_restful import Resource
from database.db import connect_db
import json


class TrackLikeApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            dataToupdate = Track.objects.get(track_id=data['track_id'])
            message = 'Track has been sucessfully liked by '+data['username']
            if data['username'] not in dataToupdate.user_likes:
                dataToupdate.user_likes.append(data['username'])
                dataToupdate.likes += 1
                dataToupdate.save()
            else:
                message = 'Track is already liked by '+data['username']
            return {'status': 201, 'message': message}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': "not working"}


class TrackUnLikeApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            dataToupdate = Track.objects.get(track_id=data['track_id'])
            message = 'Track has been sucessfully unliked by '+data['username']
            if data['username'] in dataToupdate.user_likes:
                dataToupdate.user_likes.remove(data['username'])
                dataToupdate.likes -= 1
                dataToupdate.save()
            else:
                message = 'Track is already unliked by '+data['username']
            return {'status': 201, 'message': message}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': "not working"}


class TrackUserApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            usertracks = Track.objects.getAllUserTracks(data['username'])
            resp = Response(usertracks.to_json(), status=200,
                            mimetype='application/json')
            return resp

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


class TrackApi(Resource):
    def get(self):
        try:
            data = []
            for track in Track.objects:
                t = {"track_id": track.track_id,  "name": track.name,
                     "username": track.username, "url": track.url, "image_url": track.image_url, "genre": track.genre, "inst_used": track.inst_used, "likes": track.likes}
                data.append(t)
                json_data = json.dumps(data, indent=2)

            resp = Response(json_data, status=200,
                            mimetype='application/json')
            return resp

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def post(self):
        try:
            data = request.get_json(force=True)
            cnt = Counter.objects.get(collection="track")
            cnt.counter += 1
            cnt.save()
            empty_list = ['default']
            post = Track(track_id=cnt.counter, name=data['name'],
                         url=data['url'], username=data['username'], image_url=data['image_url'], inst_used=data['inst_used'], genre=data['genre'], user_likes=empty_list)
            post.save()
            return {'status': 201, 'message': 'Track has been sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}
