import os
from .db_utils import *
from .dnd_math import *
from .skills import get_skill

def create_character(name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id):
    """
    Creates a character

    Keyword arguments:
    name -- name of the character
    level -- level of the character
    str, dex, con, int, wis, cha -- ability scores
    class_id -- class id

    Returns the id of the created character
    """

    # Check if any of the parameters are None
    if any(arg is None for arg in [name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id]):
        return "Character creation failed: All parameters must be provided"
    
    # Check if any of the ability scores are not between 1 and 20
    if any(not 1 <= score <= 20 for score in [strength, dexterity, constitution, intelligence, wisdom, charisma]):
        return "Character creation failed: All ability scores must be between 1 and 20"
    
    # Check if the class_id exists
    sql = "SELECT id FROM classes WHERE id = %s"
    result = exec_get_one(sql, [class_id])
    if not result:
        return "Character creation failed: Class ID does not exist"

    
    sql = """
    INSERT INTO characters (name, level, class_id) VALUES 
        (%s, %s, %s)
    RETURNING id;
    INSERT INTO character_abilities (character_id, ability_id, score) VALUES 
        (currval('characters_id_seq'), 1, %s), 
        (currval('characters_id_seq'), 2, %s), 
        (currval('characters_id_seq'), 3, %s), 
        (currval('characters_id_seq'), 4, %s), 
        (currval('characters_id_seq'), 5, %s), 
        (currval('characters_id_seq'), 6, %s)
    RETURNING currval('characters_id_seq');
    """

    result = exec_commit_get_one(sql, [name, level, class_id, strength, dexterity, constitution, intelligence, wisdom, charisma])

    if result is not None:
        return result
    return "Character creation failed: Unknown error"

def get_character(character_id = None):
    """
    Gets a character by id

    Keyword arguments:
    user_id -- id key of the character, None if not specified
    
    Returns all information about the character (name, level, class, ability scores) if character_id is given
    Otherwise, returns all characters' surface-level information (name, level, class) 
    """

    sql = """
    SELECT ch.name, ch.level, c.name as class_name,
    ARRAY_AGG(json_build_object('name', a.name, 'score', ca.score)) as ability_scores
    FROM characters ch
    INNER JOIN classes c ON ch.class_id = c.id
    INNER JOIN character_abilities ca ON ch.id = ca.character_id
    INNER JOIN abilities a ON ca.ability_id = a.id
    WHERE (ch.id = %s OR %s IS NULL)
    GROUP BY ch.name, ch.level, c.name;
    """
    
    # if character_id is None, return all surface-level character information
    if character_id is None:
        result = exec_get_all(sql, [character_id, character_id])
        characters = []
        for character in result:
            character = {
                'name': character[0],
                'level': character[1],
                'class': character[2],
            }
            characters.append(character)
        return characters
    
    # if character_id is not None, return all information about the character
    else:
        result = exec_get_one(sql, [character_id, character_id])
        if result is not None:
            character = {
                'name': result[0],
                'level': result[1],
                'class_name': result[2],
                'ability_scores': [],
                'skills': get_skill(character_id) # second SQL query to get skills
            }
            for ability in result[3]:
                ability_score = {
                    'name': ability['name'],
                    'score': ability['score'],
                    'modifier': calculate_ability_modifier(ability['score'])
                }
                character['ability_scores'].append(ability_score)
            return character
        return None
            

def update_character(character_id, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id):
    """
    Updates a character

    Keyword arguments:
    character_id -- id key of the character
    name -- name of the character
    level -- level of the character
    class_id -- class
    """
        
    # Check if any of the ability scores are not between 1 and 20, ignores None values
    if any(not 1 <= score <= 20 for score in [strength, dexterity, constitution, intelligence, wisdom, charisma] if score is not None):
        return "Character update failed: All ability scores must be between 1 and 20"

    # Check if the character with the given ID exists
    sql_check = "SELECT id FROM characters WHERE id = %s"
    result = exec_get_one(sql_check, [character_id])
    if not result:
        return "Character update failed: Character not found"
    
    # Check if the class_id exists
    sql = "SELECT id FROM classes WHERE id = %s OR %s IS NULL"
    result = exec_get_one(sql, [class_id, class_id])
    if not result:
        return "Character update failed: Class ID does not exist"

    # COALESCE is used to update only the fields that are not None
    sql = """
    UPDATE characters
    SET name = COALESCE(%s, name), level = COALESCE(%s, level), class_id = COALESCE(%s, class_id)
    WHERE id = %s;
    UPDATE character_abilities
    SET score = CASE ability_id
        WHEN 1 THEN COALESCE(%s, score)
        WHEN 2 THEN COALESCE(%s, score)
        WHEN 3 THEN COALESCE(%s, score)
        WHEN 4 THEN COALESCE(%s, score)
        WHEN 5 THEN COALESCE(%s, score)
        WHEN 6 THEN COALESCE(%s, score)
        ELSE score
        END
    WHERE character_id = %s AND ability_id IN (1, 2, 3, 4, 5, 6);
    """

    exec_commit(sql, [name, level, class_id, character_id, strength, dexterity, constitution, intelligence, wisdom, charisma, character_id])
    return "Character updated successfully"

def delete_character(character_id):
    """
    Deletes a character

    Keyword arguments:
    character_id -- id key of the character
    """

    # Check if the character with the given ID exists
    sql_check = "SELECT id FROM characters WHERE id = %s"
    result = exec_get_one(sql_check, [character_id])
    if not result:
        return "Character deletion failed: Character not found"

    sql = """
    DELETE FROM character_abilities WHERE character_id = %s;
    DELETE FROM proficiencies WHERE character_id = %s;
    DELETE FROM characters WHERE id = %s
    """

    exec_commit(sql, [character_id, character_id, character_id])
    return "Character deleted successfully"


