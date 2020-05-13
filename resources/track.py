from flask import Response, request, jsonify
from database.models import Track, Users, Counter
from flask_restful import Resource


class TrackApi(Resource):
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
