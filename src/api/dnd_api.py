from flask_restful import Resource, reqparse, request
from db import character


class CharactersAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        return character.get_character(character_id)