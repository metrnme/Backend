from flask import Response, request, jsonify
from database.models import Comments
from flask_restful import Resource


class CommentApi(Resource):
    def post(self):
        print("Post a Comment")

    def get(self, id):
        print("Get a Comment")

    def delete(self, id):
        print("Delete a Comment")

    def update(self, id):
        print("Update a Comment")
