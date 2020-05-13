from flask import Response, request, jsonify
from database.models import Instruments, Users
from flask_restful import Resource


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
            return {"status": 200, "message": "sucess"}
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
        data = dict()
        counter = 0
        for inst in Instruments.objects:
            data.setdefault(counter, inst.to_json())
            counter += 1
        return {'status': 200, 'content': data}
