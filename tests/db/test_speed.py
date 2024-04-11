import unittest
import timeit
from src.db.character import create_character
from src.db.proficiencies import *

class TestSpeed(unittest.TestCase):

    def test_speed_difference(self):
        test_id = create_character('Test', 7, 20, 18, 16, 14, 12, 10, 1)

        print('\nTesting proficiency bonus calculation speed...')

        # Measure the execution time of calculate_skill_modifier
        calculate_time = timeit.timeit(lambda: old_get_skill_modifier(test_id, 'Athletics'), number=10)

        # Measure the execution time of new_calculate_skill_modifier
        new_calculate_time = timeit.timeit(lambda: get_skill_modifier(test_id, 'Athletics'), number=10)

        # Compare the execution times
        print('calculate_skill_modifier:', round(calculate_time, 4))
        print('new_calculate_skill_modifier:', round(new_calculate_time, 4))


def old_get_skill_modifier(character_id, skill_name):
    """
    Calculate the modifier for a skill.

    Keyword arguments:
    character_id -- id of the character
    skill_name -- name of the skill

    Returns the modifier for the skill
    """


    sql = """ 
    SELECT a.name FROM abilities a
    INNER JOIN skills s ON s.ability_id = a.id
    INNER JOIN proficiencies p ON p.skill_id = s.id
    INNER JOIN characters ch ON ch.id = p.character_id
    WHERE ch.id = %s AND s.name = %s
    """


    proficiency_bonus = get_proficiency_bonus(character_id)
    stat_name = exec_get_one(sql, [character_id, skill_name])

    # if not proficient, return the ability modifier
    if stat_name is None:
        sql = """
        SELECT a.name FROM abilities a
        INNER JOIN skills s ON s.ability_id = a.id
        WHERE s.name = %s
        """
        stat_name = exec_get_one(sql, [skill_name])
        return get_ability_modifier(character_id, stat_name[0])
    
    ability_modifier = get_ability_modifier(character_id, stat_name[0])

    return proficiency_bonus + ability_modifier