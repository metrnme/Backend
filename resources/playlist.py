from flask import Response, request, jsonify
from database.models import Playlist
from flask_restful import Resource


class PlaylistApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Playlist(name=data['name'], p_username=data['p_username'])
            post.save()
            return {'status': 201, 'message': 'playlist sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}
