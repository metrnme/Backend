from flask import Flask, request, Response, render_template, jsonify
from database.models import Users, Comments
from mongoengine import connect
from flask_restful import Api
from routes import initialize_routes
import json
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


client = connect(
    host='mongodb+srv://test:test1@mtrnme-yr9b5.mongodb.net/mtrnme?retryWrites=true&w=majority')

db = client.db
app = Flask(__name__)
api = Api(app)
initialize_routes(api)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

'''
# Old Working Code
--------------------

# Post a User's Data
@app.route("/api/v1/user", methods=["POST"])
def add_user():
    try:
        username = request.args.get('username')
        name = request.args.get('name')
        gender = request.args.get('gender')
        age = request.args.get('age')
        print(username, name, gender, age)
        # Create a link-based post
        post = Users(username=username, name=name, gender=gender, age=age)
        post.save()
        return {'status': 201, 'message': 'User has been sucessfully created! ='}
    except Exception as e:
        print(e)
        resp = jsonify(
            {'status': 409, 'error_message': 'Username already exists!, please try another coming up with a different username!'})
        return resp

# Get a User's information
@app.route("/api/v1/user", methods=["GET"])
def get_user():
    try:
        username = request.args.get('username')
        result = Users.objects.get(username=username)
        json_data = result.to_json()
        return {'status': 200, 'content': json_data}
    except Exception as e:
        print(e)
        resp = jsonify(
            {'status': 404, 'error_message': 'The User Searched does not exist!'})
        return resp


# Get's all Users in our Application
@app.route("/api/v1/users", methods=["GET"])
def get_users():
    try:
        sabkuch = Users.objects.all()
        counter = 1
        data = dict()
        for users in sabkuch:
            data.setdefault(counter, users.to_json())
            counter += 1
        print(data)

        return {'status': 200, 'content': data}
    except Exception as e:
        print(e)
        resp = jsonify(
            {'status': 404, 'error_message': e})
        return resp




'''
