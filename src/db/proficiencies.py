import os
import math
from .db_utils import *


# ===== Private functions =====
def __calculate_proficiency_bonus(level):
    """
    Calculate the proficiency bonus based on the character's level.

    Keyword arguments:
    level -- level of the character

    Returns the proficiency bonus
    """

    # Proficiency Bonus = 1 + Character Level / 4 (round up)
    return 1 + math.ceil((level) / 4)

def __calculate_ability_modifier(ability_score):
    return (ability_score - 10) // 2


# ===== Public functions =====

def create_proficiency(character_id, proficiency_name):
    """
    Create a proficiency for a character.

    Keyword arguments:
    character_id -- id of the character
    proficiency_name -- name of the proficiency
    """

    sql = """
    INSERT INTO proficiencies(character_id, skill_id)
    SELECT %s, 
    s.id FROM skills s WHERE s.name = %s
    """

    exec_commit(sql, [character_id, proficiency_name])

def delete_proficiency(character_id, proficiency_name):
    """
    Delete a proficiency for a character.

    Keyword arguments:
    character_id -- id of the character
    proficiency_name -- name of the proficiency
    """

    sql = """DELETE FROM proficiencies WHERE character_id = %s AND name = %s"""

    exec_commit(sql, [character_id, proficiency_name])

def list_proficiencies(character_id):
    """
    List all proficiencies for a character.

    Keyword arguments:
    character_id -- id of the character

    Returns a list of proficiencies
    """

    sql = """
    SELECT s.name FROM skills s
    INNER JOIN proficiencies p ON p.skill_id = s.id
    WHERE p.character_id = %s
    """

    return exec_get_all(sql, [character_id])


def get_proficiency_bonus(character_id):
    """
    Calculate the proficiency bonus based on the character's level.

    Keyword arguments:
    character_id -- id of the character

    Returns the proficiency bonus
    """

    sql = """SELECT level FROM characters WHERE id = %s"""

    level = exec_get_one(sql, [character_id])[0]

    return __calculate_proficiency_bonus(level)


def get_skill_modifier(character_id, skill_name):
    """
    Calculate the modifier for a skill.

    Keyword arguments:
    character_id -- id of the character
    skill_name -- name of the skill

    Returns the modifier for the skill
    """

    # left join on the proficiencies table to avoid issues with non-proficient skills 
    sql = """ 
    SELECT ch.level, ca.score, p.character_id as is_proficient FROM abilities a
	INNER JOIN characters ch ON ch.id = %s
    INNER JOIN skills s ON s.ability_id = a.id
	INNER JOIN character_abilities ca ON ca.character_id = ch.id
    LEFT JOIN proficiencies p ON p.skill_id = s.id AND p.character_id = ch.id
    WHERE s.name = %s
	AND ca.ability_id = a.id;
    """

    result = exec_get_one(sql, [character_id, skill_name])
    level = result[0]
    ability_score = result[1]
    is_proficient = result[2] is not None

    proficiency_bonus = __calculate_proficiency_bonus(level)
    ability_modifier = __calculate_ability_modifier(ability_score)

    if is_proficient:
        return proficiency_bonus + ability_modifier
    else:
        return ability_modifier

def get_ability_value(character_id, stat_name):
    sql = """SELECT {} FROM characters WHERE id = %s""".format(stat_name)

    return exec_get_one(sql, [character_id])[0]

def get_ability_modifier(character_id, stat_name):
    value = get_ability_value(character_id, stat_name)

    return (value - 10) // 2

