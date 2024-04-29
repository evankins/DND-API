from .db_utils import *
from .dnd_math import *


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

def get_proficiencies(character_id):
    """
    Gets all proficiencies for a character.

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


def delete_proficiency(character_id, proficiency_name):
    """
    Delete a proficiency for a character.

    Keyword arguments:
    character_id -- id of the character
    proficiency_name -- name of the proficiency
    """

    sql = """
    DELETE FROM proficiencies
    USING skills
    WHERE skills.id = proficiencies.skill_id
    AND proficiencies.character_id = %s
    AND skills.name = %s
    """

    exec_commit(sql, [character_id, proficiency_name])
