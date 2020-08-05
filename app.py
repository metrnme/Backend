from flask import Flask, request, Response, render_template, jsonify
from flask_restful import Api
from database.db import connect_db
from routes import initialize_routes
import json


db = connect_db()
app = Flask(__name__)
api = Api(app)
initialize_routes(api)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
