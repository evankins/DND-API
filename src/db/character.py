import os
from .db_utils import *

def rebuild_tables():
    exec_sql_file('src/db/schema.sql')
    exec_sql_file('src/db/test_data.sql')

def list_characters():
    """
    Compiles a list of all characters' information from the database

    Returns a list of all characters
    """

    sql = """
    SELECT ch.name, ch.level, c.name,
	ARRAY_AGG(a.name || ': ' || ca.score) ability_scores 
	FROM characters ch
    INNER JOIN classes c ON ch.class_id = c.id
    INNER JOIN character_abilities ca ON ch.id = ca.character_id
    INNER JOIN abilities a ON ca.ability_id = a.id
	GROUP BY ch.name, ch.level, c.name
    """

    return exec_get_all(sql)

def get_character(character_id):
    """
    Gets a character by id

    Keyword arguments:
    user_id -- id key of the character
    
    Returns all of the information about a character
    """

    sql = """
    SELECT ch.name, ch.level, c.name,
	ARRAY_AGG(a.name || ': ' || ca.score) ability_scores 
	FROM characters ch
    INNER JOIN classes c ON ch.class_id = c.id
    INNER JOIN character_abilities ca ON ch.id = ca.character_id
    INNER JOIN abilities a ON ca.ability_id = a.id
    WHERE ch.id = %s
	GROUP BY ch.name, ch.level, c.name
    """

    return exec_get_one(sql, [character_id])

def create_character(name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id):
    """
    Creates a character

    Keyword arguments:
    name -- name of the character
    level -- level of the character
    class_id -- class id

    Returns the id of the created character
    """

    sql = """
    INSERT INTO characters (name, level, class_id)
    VALUES (%s, %s, %s)
    RETURNING id;
    INSERT INTO character_abilities (character_id, ability_id, score)
    VALUES (currval('characters_id_seq'), 1, %s), 
    (currval('characters_id_seq'), 2, %s), 
    (currval('characters_id_seq'), 3, %s), 
    (currval('characters_id_seq'), 4, %s), 
    (currval('characters_id_seq'), 5, %s), 
    (currval('characters_id_seq'), 6, %s)
    RETURNING currval('characters_id_seq');
    """

    return exec_commit_get_one(sql, [name, level, class_id, strength, dexterity, constitution, intelligence, wisdom, charisma])

def update_character(character_id, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id):
    """
    Updates a character

    Keyword arguments:
    character_id -- id key of the character
    name -- name of the character
    level -- level of the character
    class_id -- class
    """

    sql = """
    UPDATE characters
    SET name = %s, level = %s, class_id = %s
    WHERE id = %s;
    UPDATE character_abilities
    SET score = CASE ability_id
        WHEN 1 THEN %s
        WHEN 2 THEN %s
        WHEN 3 THEN %s
        WHEN 4 THEN %s
        WHEN 5 THEN %s
        WHEN 6 THEN %s
        ELSE score
        END
    WHERE character_id = %s AND ability_id IN (1, 2, 3, 4, 5, 6);
    """

    exec_commit(sql, [name, level, class_id, character_id, strength, dexterity, constitution, intelligence, wisdom, charisma, character_id])

def delete_character(character_id):
    """
    Deletes a character

    Keyword arguments:
    character_id -- id key of the character
    """

    sql = """
    DELETE FROM character_abilities WHERE character_id = %s;
    DELETE FROM proficiencies WHERE character_id = %s;
    DELETE FROM characters WHERE id = %s
    """

    exec_commit(sql, [character_id, character_id, character_id])


