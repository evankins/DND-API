from flask_restful import Resource, reqparse, request
from db import character

class HelloWorld(Resource):
    def get(self):
        return list(tuple(character.list_characters()))

class Users(Resource):
    def get(self):
        return list(tuple(character.list_characters()))