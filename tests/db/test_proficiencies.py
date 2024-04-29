import unittest
from src.db.character import create_character
from src.db.proficiencies import *
from src.db.dnd_math import *

class TestProficiencies(unittest.TestCase):
    def setUp(self):
        exec_sql_file('src/db/schema.sql')
        exec_sql_file('src/db/test_data.sql')
    
    def _test_proficiencies(self):
        test_id = create_character('Test', 7, 20, 18, 16, 14, 12, 10, 1)

        # Test proficiency bonus
        prof_bonus = get_proficiency_bonus(test_id)
        self.assertEqual(prof_bonus, 3)

        # Add skill proficiency
        create_proficiency(test_id, 'Athletics')
        create_proficiency(test_id, 'Persuasion')
        proficiencies = get_proficiencies(test_id)
        self.assertIn('Athletics', proficiencies[0])

        # Test skill proficiency
        athletics_prof = get_skill_modifier(test_id, 'Athletics')
        persuasion_prof = get_skill_modifier(test_id, 'Persuasion')
        # proficiency bonus : 3
        # str modifier : 5
        self.assertEqual(athletics_prof, 8)
        # proficiency bonus : 3
        # cha modifier : 0
        self.assertEqual(persuasion_prof, 3)

        # Test non-proficient skill
        acrobatics_prof = get_skill_modifier(test_id, 'Acrobatics')
        # proficiency bonus : 3 (not applied)
        # dex modifier : 4
        self.assertEqual(acrobatics_prof, 4)

        # Test delete proficiency
        delete_proficiency(test_id, 'Athletics')
        proficiencies = get_proficiencies(test_id)
        self.assertNotIn('Athletics', proficiencies[0])

