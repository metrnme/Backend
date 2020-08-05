from flask import Response, request, jsonify
from database.models import Comments, Track
from flask_restful import Resource
from datetime import datetime as dt
import json

class CommentFetchApi(Resource):
     def post(self):
        try:
            data = request.get_json(force=True)
            result = Comments.objects.getAllComments(data['track_id'])
            resp = Response(result.to_json(), status=200,
                            mimetype='application/json')
            return resp
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


class CommentApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Comments(
                track_id=data['track_id'], username=data['username'], content=data["comment"])
            post.save()
            return {'status': 201, 'message': 'Comment has been sucessfully posted!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed to post a comment!'}

        # data = request.get_json(force=True)
        # result = Comments.objects.getAllComments(data['track_id'])
        # data = dict()
        # counter = 0
        # for comments in result:
        #    data.setdefault(counter, comments.to_json())
     #   counter += 1
        # return {'status': 200, 'content': data}

    def delete(self):
        data = request.get_json(force=True)
        result = Comments.objects.get(id=data['id'])
        result.delete()
        return {"result": "success"}

    def put(self, id):
        data = request.get_json(force=True)
        result = Comments.objects.get(id=data['track_id'])
        result.content=data['message']
        print(data)
