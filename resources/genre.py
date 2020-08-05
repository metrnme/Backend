from flask import Response, request, jsonify
from database.models import Genre
from flask_restful import Resource
import json
from bson import json_util


class GenreApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Genre(name=data['name'])
            post.save()
            return {'status': 201, 'message': 'Genre has been sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def get(self):
        data = []
        for g in Genre.objects:
            data.append({"name": g.name})
        json_data = json.dumps(data, default=json_util.default)
        resp = Response(json_data, status=200, mimetype='application/json')
        return resp
