import unittest
from src.db.character import *

class TestCharacter(unittest.TestCase):
    
    def setUp(self):
        exec_sql_file('src/db/schema.sql')
        exec_sql_file('src/db/test_data.sql')
    
    def test_character(self):
        # List before
        characters_len = len(list_characters())

        # Create
        test_id = create_character('Test', 1, 1, 1, 1, 1, 1, 1, 1)
        self.assertIsNotNone(test_id)

        # List after
        new_characters_len = len(list_characters())
        self.assertEquals(new_characters_len, characters_len + 1)

        # Get
        test_character = get_character(test_id)
        self.assertEquals(test_character[0], 'Test')

        # Update
        test_id = update_character(test_id, 'Test2', 2, 2, 2, 2, 2, 2, 2, 1)
        test_character = get_character(test_id)
        self.assertEquals(test_character[0], 'Test2')

        # Delete
        delete_character(test_id)
        deleted_character = get_character(test_id)
        self.assertIsNone(deleted_character)




