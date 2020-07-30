from flask import Response, request, jsonify
from database.models import Playlist, Counter
from flask_restful import Resource
import json

class PlaylistPostApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            result=Playlist.objects.getAllPlaylist(data['username'])
            resp = Response(result.to_json(), status=200,
                            mimetype='application/json')
            return resp
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


class PlaylistApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            cnt = Counter.objects.get(collection="playlist")
            cnt.counter += 2
            cnt.save()
            post = Playlist(pl_id=cnt.counter, name=data['name'], username=data['username'])
            post.save()
            return {'status': 201, 'message': 'playlist sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def get(self):
        try:
            username = request.args.get('username')
            result=Playlist.objects.getAllPlaylist(username)
            resp = Response(result.to_json(), status=200,
                            mimetype='application/json')
            return resp
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}
    
    def put(self):
        data = request.get_json(force=True)
        u = Playlist.objects.get(pl_id=data['playlist_id'])
        u.track_list.append(data['track_id'])
        u.save()
        json_data = {'status': 201, 'message': 'Track has been sucessfully added to Playlist'}
        return json_data
    
    def delete(self):
        data = request.get_json(force=True)
        u = Playlist.objects.get(pl_id=data['playlist_id'])
        u.delete()
        json_data = {'status': 201, 'message': 'Track has been sucessfully deleted from Playlist'}
        return json_data
