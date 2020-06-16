import os
import json

from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource

from .db import connection, insert, PrimaryKeyAlreadyExistsError, show


app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("data", action="append")

def insert_arg_parse():
    args = parser.parse_args()

    table_datas = []

    for string_data in args["data"]:
        table_data = json.loads(string_data)
        table_datas.append(table_data)

    return table_datas


class base(Resource):
    # to_disp : dict of table columns with val: true for 
    # cols to be displayed
    # eg to_disp = {'col1' = True, 'col2' = False, col3 = 'True'}
    def get(self, table_name):
        to_disp = insert_arg_parse()[0]

        response = {'result':show(table_name, to_disp)}
        response = jsonify(response)
        response.status_code = 202
        return response

    def post(self, table_name):

        table_datas = insert_arg_parse()

        response = jsonify({"reason": "bad-request"})
        response.status_code = 400

        try:
            insert(table_name, table_datas)
            response = jsonify({"reason": "success"})
            response.status_code = 202

        except PrimaryKeyAlreadyExistsError:
            response = jsonify({"reason": "primary-key-already-exists"})
            response.status_code = 409

        return response


api.add_resource(base, "/<string:table_name>")

__all__ = [app, api]
