from flask import Response, request, jsonify
from database.models import Track, Users, Counter
from flask_restful import Resource
from database.db import connect_db
import json


class TrackApi(Resource):
    def get(self):
        try:
            data = []
            for track in Track.objects:
                t = {"track_id": track.track_id,  "name": track.name,
                     "username": track.username, "url": track.url, "likes": track.likes}
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
            post = Track(track_id=cnt.counter, name=data['name'],
                         url=data['url'], username=data['username'])
            post.save()
            return {'status': 201, 'message': 'Track has been sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


'''
            db = connect_db()
            x = db.collection_names
            print(x)
            result = Track.objects
            data = []
            if(len(result) > 1):

            else:
                t = [{"track_id": result.track_id,  "name": result.name,
                      "username": result.username, "url": result.url, "likes": result.likes}]
                json_data = json.dumps(t)

'''
