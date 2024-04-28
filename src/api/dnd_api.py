from flask_restful import Resource, reqparse, request
from db import character
from db import proficiencies
from db import skills


class CharactersAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        return character.get_character(character_id)

class ProficienciesAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        return proficiencies.list_proficiencies(character_id)

class SkillsAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        skill_name = request.args.get("skill")
        return skills.get_skill(character_id, skill_name)