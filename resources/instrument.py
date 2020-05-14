from flask import Response, request, jsonify
from database.models import Instruments, Users
from flask_restful import Resource
import json
from bson import json_util


class InstrumentUserApi(Resource):
    def put(self):
        try:
            data = request.get_json(force=True)
            user = data["username"]
            inst = data["instruments"]
            dataToupdate = Users.objects.get(username=user)
            for instrumento in inst:
                dataToupdate.inst.append(instrumento)
            dataToupdate.save()
            return {"status": 200, "message": "Instrument has been added to the User!"}
        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}


class InstrumentApi(Resource):
    def post(self):
        try:
            data = request.get_json(force=True)
            post = Instruments(name=data['name'], i_type=data['i_type'])
            post.save()
            return {'status': 201, 'message': 'Instrument has been sucessfully added!'}

        except Exception as e:
            print(e)
            return {'status': 409, 'error_message': 'Failed!'}

    def get(self):
        data = []
        for inst in Instruments.objects:
            data.append({"name": inst.name, "i_type": inst.i_type})
        json_data = json.dumps(data, default=json_util.default)
        resp = Response(json_data, status=200, mimetype='application/json')
        return resp
