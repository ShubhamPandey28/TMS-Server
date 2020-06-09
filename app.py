import os
import json

from flask import Flask, jsonify, request, flash
from flask_restful import reqparse, Api, Resource

from .db import connection, insert, PrimaryKeyAlreadyExistsError


app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()

schema = ['city_id', 'city_name', 'city_state']

for i in schema:
    parser.add_argument(i)


class base(Resource):

    def get(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cities;")
        response = {'result':cursor.fetchall()}
        response = jsonify(response)
        response.status_code = 202
        cursor.close()
        return response
    
    
    def post(self):
        
        args = parser.parse_args()
        
        response = jsonify({'reason':'bad-request'})
        response.status_code = 400

        try:
            insert(args)
            response = jsonify({'reason':'success'})
            response.status_code = 202

        except PrimaryKeyAlreadyExistsError:
            response = jsonify({'reason':'primary-key-already-exists'})
            response.status_code = 409

        return response


api.add_resource(base, '/') 

if __name__ == '__main__':
    app.run(debug=True)