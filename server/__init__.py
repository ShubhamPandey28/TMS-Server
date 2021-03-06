import os
import json

from flask import Flask, jsonify
from flask_restful import reqparse, Api, Resource

from .db import (
    connection,
    insert,
    PrimaryKeyAlreadyExistsError,
    return_table,
    get_client_consignments,
)


app = Flask(__name__)

api = Api(app)

parser = reqparse.RequestParser()

parser.add_argument("data", action="append")
parser.add_argument("table_name")
parser.add_argument("client_name")


def insert_arg_parse():
    args = parser.parse_args()

    table_datas = []

    for string_data in args["data"]:
        table_data = json.loads(string_data)
        table_datas.append(table_data)

    return table_datas


class base(Resource):
    def get(self, table_name):
        response = {"result": return_table(table_name)}
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


class basex(Resource):
    def get(self):
        client_name = parser.parse_args()["client_name"]
        print(client_name)
        response = jsonify({"result": get_client_consignments(client_name)})
        response.status_code = 202
        return response


api.add_resource(base, "/<string:table_name>")
api.add_resource(basex, "/xyz")

__all__ = [app, api]
