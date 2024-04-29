import os
from .db_utils import *
from .dnd_math import *

def get_skill(character_id, skill_name = None):
    """
    Gets the skill of a character, or all skills if skill_name is None

    Keyword arguments:
    character_id -- id of the character
    skill_name -- name of the skill, None if not specified

    Returns the skill(s) and proficiency bonuses of the character
    """

    # left join on the proficiencies table to avoid issues with non-proficient skills
    sql = """
    SELECT ch.level, ca.score, p.character_id as is_proficient, s.name FROM abilities a
	INNER JOIN characters ch ON ch.id = %s
    INNER JOIN skills s ON s.ability_id = a.id
	INNER JOIN character_abilities ca ON ca.character_id = ch.id
    LEFT JOIN proficiencies p ON p.skill_id = s.id AND p.character_id = ch.id
    WHERE (s.name = %s OR %s IS NULL)
	AND ca.ability_id = a.id
    ORDER BY s.ability_id, s.id;
    """

    skills = exec_get_all(sql, [character_id, skill_name, skill_name])
    result = []
    for skill in skills:
        ability_modifier = calculate_ability_modifier(skill[1]) # character's ability score
        
        # if is_proficient is not None, then the character is proficient in the skill
        if skill[2] is not None:
            proficiency_bonus = calculate_proficiency_bonus(skill[0]) # character's level
            skill = {
                'name': skill[3],
                'is_proficient': True,
                'modifier': proficiency_bonus + ability_modifier
            }
        else:
            skill = {
                'name': skill[3],
                'is_proficient': False,
                'modifier': ability_modifier
            }
        result.append(skill)
    
    return result
    

    