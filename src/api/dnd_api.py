from flask_restful import Resource, reqparse, request
from db import character
from db import proficiencies
from db import skills


class CharactersAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        return character.get_character(character_id)
    
    def post(self):
        data = request.get_json()

        name = data['name']
        level = data['level']
        strength = data['strength']
        dexterity = data['dexterity']
        constitution = data['constitution']
        intelligence = data['intelligence']
        wisdom = data['wisdom']
        charisma = data['charisma']
        class_id = data['class_id']

        character.create_character(name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id)
    
    def put(self):
        data = request.get_json()

        character_id = data['id']
        name = data['name']
        level = data['level']
        strength = data['strength']
        dexterity = data['dexterity']
        constitution = data['constitution']
        intelligence = data['intelligence']
        wisdom = data['wisdom']
        charisma = data['charisma']
        class_id = data['class_id']

        character.update_character(character_id, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id)
    
    def delete(self):
        character_id = request.args.get("id")
        character.delete_character(character_id)

class ProficienciesAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        return proficiencies.get_proficiencies(character_id)
    
    def post(self):
        data = request.get_json()

        character_id = data['id']
        proficiency_name = data['proficiency_name']

        proficiencies.create_proficiency(character_id, proficiency_name)
    
    def delete(self):
        data = request.get_json()

        character_id = data['id']
        proficiency_name = data['proficiency_name']

        proficiencies.delete_proficiency(character_id, proficiency_name)

class SkillsAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        skill_name = request.args.get("skill")
        return skills.get_skill(character_id, skill_name)