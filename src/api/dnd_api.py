from flask_restful import Resource, reqparse, request
from db import character
from db import proficiencies
from db import skills


class CharactersAPI(Resource):
    def get(self):
        character_id = request.args.get("id")
        response = character.get_character(character_id)

        if response is None:
            return "Character get failed: Character not found"
        else:
            return response
    
    def post(self):
        data = request.get_json()

        name = data.get('name')
        level = data.get('level')
        strength = data.get('strength')
        dexterity = data.get('dexterity')
        constitution = data.get('constitution')
        intelligence = data.get('intelligence')
        wisdom = data.get('wisdom')
        charisma = data.get('charisma')
        class_id = data.get('class_id')

        response = character.create_character(name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id)

        # if response is not an int (an id), the character was not created successfully
        if type(response) is not int:
            return response
        else:
            return ["Character created successfully", response]
    
    def put(self):
        data = request.get_json()

        character_id = data.get('id')
        name = data.get('name')
        level = data.get('level')
        strength = data.get('strength')
        dexterity = data.get('dexterity')
        constitution = data.get('constitution')
        intelligence = data.get('intelligence')
        wisdom = data.get('wisdom')
        charisma = data.get('charisma')
        class_id = data.get('class_id')

        response = character.update_character(character_id, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id)
        return response
    
    def delete(self):
        character_id = request.args.get("id")
        response = character.delete_character(character_id)

        return response


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