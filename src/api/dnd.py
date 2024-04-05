from flask_restful import Resource, reqparse, request
from db import dnd

class HelloWorld(Resource):
    def get(self):
        return list(tuple(dnd.list_users()))

class Users(Resource):
    def get(self):
        return list(tuple(dnd.list_users()))