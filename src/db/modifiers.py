from .db_utils import *
from .dnd_math import *

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

    proficiency_bonus = calculate_proficiency_bonus(level)
    ability_modifier = calculate_ability_modifier(ability_score)

    if is_proficient:
        return proficiency_bonus + ability_modifier
    else:
        return ability_modifier

def get_ability_modifier(character_id, stat_name):
    """
    Calculate the modifier for an ability score.

    Keyword arguments:
    character_id -- id of the character
    stat_name -- name of the ability score

    Returns the modifier for the ability score
    """
    
    sql = """
    SELECT ca.score FROM character_abilities ca
    INNER JOIN abilities a ON a.id = ca.ability_id
    WHERE ca.character_id = %s AND a.name = %s
    """

    value = exec_get_one(sql, [character_id, stat_name])[0]

    return calculate_ability_modifier(value)
