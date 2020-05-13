from flask import Response, request, jsonify
from database.models import Counter
from flask_restful import Resource


class CounterApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Counter(collection=data['collection'])
            post.save()
            return {'status': 201, 'message': 'Counter for '+data['collection']+' has been created'}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def get(self):
        try:
            data = request.get_json(force=True)
            post = Counter.objects.get(collection=data['collection'])
            post.counter += 1
            post.save()
            return {'status': 201, post.collection: post.counter}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}
