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
    SELECT ch.name, ch.level, ch.strength, ch.dexterity, ch.constitution, ch.intelligence, ch.wisdom, ch.charisma, c.name FROM characters ch
    INNER JOIN classes c ON ch.class_id = c.id
    """

    return exec_get_all(sql)

def get_character(character_id):
    """
    Gets a character by id

    Keyword arguments:
    user_id -- id key of the character
    
    Returns the character
    """

    sql = """
    SELECT ch.name, ch.level, ch.strength, ch.dexterity, ch.constitution, ch.intelligence, ch.wisdom, ch.charisma, c.name FROM characters ch
    INNER JOIN classes c ON ch.class_id = c.id
    WHERE ch.id = %s
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
    INSERT INTO characters (name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id
    """

    return exec_commit_get_one(sql, [name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id])

def update_character(character_id, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id):
    """
    Updates a character

    Keyword arguments:
    character_id -- id key of the character
    name -- name of the character
    level -- level of the character
    class_id -- class

    Returns the id of the updated character
    """

    sql = """
    UPDATE characters
    SET name = %s, level = %s, strength = %s, dexterity = %s, constitution = %s, intelligence = %s, wisdom = %s, charisma = %s, class_id = %s
    WHERE id = %s
    RETURNING id
    """

    return exec_commit_get_one(sql, [name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id, character_id])

def delete_character(character_id):
    """
    Deletes a character

    Keyword arguments:
    character_id -- id key of the character
    """

    sql = """
    DELETE FROM characters
    WHERE id = %s
    """

    exec_commit(sql, [character_id])


