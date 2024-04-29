import unittest
import json
from tests.test_utils import *


class TestExample(unittest.TestCase):

    def setUp(self):  
        """Initialize DB using API call"""
        post_rest_call(self, 'http://127.0.0.1:5000/manage/init')
        print("DB Should be reset now")
    
    def test_character(self):
        """Test characters API"""
        print("Testing characters API")

        # used whenever header contains nothing else
        hdr = {'Content-Type': 'application/json'}

        # ================================
        print("\nTesting GET /characters")

        characters = get_rest_call(self, 'http://127.0.0.1:5000/characters')

        self.assertEqual(characters[2]['class'], 'Cleric', "Expected third character to be a Cleric")

        print(json.dumps(characters, indent=4))

        # ================================
        print("\nTesting POST /characters 'Grognak'")

        data = {
            "name": "Grognak",
            "level": 20,
            "class_id": 1,
            "strength": 20,
            "dexterity": 16,
            "constitution": 20,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 8
        }
        print("Data:\n", data)

        response = post_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)
        id = response[1]

        self.assertEqual(response[0], "Character created successfully", "Expected success message")
        
        print(response[0])

        # ================================
        print("\nTesting POST /characters with incomplete data")

        data = {
            "name": "Grognak",
            "level": 20
        }
        print("Data:\n", data)


        response = post_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character creation failed: All parameters must be provided", "Expected error message")

        print(response)

        # ================================
        print("\nTesting POST /characters with invalid ability scores")

        data = {
            "name": "Grognak",
            "level": 20,
            "class_id": 1,
            "strength": -20,
            "dexterity": 16,
            "constitution": 20,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 8
        } 
        print("Data:\n", data)

        response = post_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character creation failed: All ability scores must be between 1 and 20", "Expected error message")

        print(response)

        # ================================
        print("\nTesting POST /characters with invalid class_id")

        data = {
            "name": "Grognak",
            "level": 20,
            "class_id": 999999,
            "strength": 20,
            "dexterity": 16,
            "constitution": 20,
            "intelligence": 1,
            "wisdom": 10,
            "charisma": 8
        }
        print("Data:\n", data)

        response = post_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character creation failed: Class ID does not exist", "Expected error message")

        print(response)

        # ================================
        print(f"\nTesting GET /characters?id={id} 'Grognak'")

        character = get_rest_call(self, f'http://127.0.0.1:5000/characters?id={id}')

        self.assertEqual(character['name'], 'Grognak', "Expected character to be Grognak")

        print(json.dumps(character, indent=4))

        # ================================
        print("\nTesting GET /characters?id=999999 (non-existent character)")

        response = get_rest_call(self, 'http://127.0.0.1:5000/characters?id=999999')

        self.assertEqual(response, "Character get failed: Character not found", "Expected character not found message")

        print(response)

        # ================================
        print("\nTesting PUT /characters on 'Grognak' to 'Grognak the Destroyer'")

        data = {
            "id": id,
            "name": "Grognak the Destroyer"
        }
        print("Data:\n", data)

        response = put_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)
        character = get_rest_call(self, f'http://127.0.0.1:5000/characters?id={id}')

        self.assertEqual(response, "Character updated successfully", "Expected success message")
        self.assertEqual(character['name'], 'Grognak the Destroyer', "Expected character name to be Grognak the Destroyer")

        print(response)
        print('Get updated character')
        print('New name:', character['name'])

        # ================================
        print("\nTesting PUT /characters?id=999999 (non-existent character)")

        data = {
            "id": 999999,
            "name": "Spike Spiegel"
        }

        response = put_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character update failed: Character not found", "Expected character not found message")

        print(response)

        # ================================
        print("\nTesting PUT /characters with invalid ability scores")

        data = {
            "id": id,
            "strength": 21
        }
        print("Data:\n", data)

        response = put_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character update failed: All ability scores must be between 1 and 20", "Expected error message")

        print(response)

        # ================================
        print("\nTesting PUT /characters with invalid class_id")

        data = {
            "id": id,
            "class_id": 999999
        }
        print("Data:\n", data)

        response = put_rest_call(self, 'http://127.0.0.1:5000/characters', json.dumps(data), hdr)

        self.assertEqual(response, "Character update failed: Class ID does not exist", "Expected error message")

        print(response)

        # ================================  
        print("\nTesting DELETE /characters on 'Grognak the Destroyer'")

        response = delete_rest_call(self, f'http://127.0.0.1:5000/characters?id={id}')

        self.assertEqual(response, "Character deleted successfully", "Expected success message")

        print(response)

        # ================================
        print("\nTesting DELETE /characters?id=999999 (non-existent character)")

        response = delete_rest_call(self, f'http://127.0.0.1:5000/characters?id=999999')

        self.assertEqual(response, "Character deletion failed: Character not found", "Expected character not found message")

        print(response)

        # ================================
        print("\nTesting GET /characters on 'Grognak the Destroyer' after deletion")

        response = get_rest_call(self, f'http://127.0.0.1:5000/characters?id={id}')

        self.assertEqual(response, "Character get failed: Character not found", "Expected character not found message")

        print(response)


