import math

def calculate_proficiency_bonus(level):
    """
    Calculate the proficiency bonus based on the character's level.

    Keyword arguments:
    level -- level of the character

    Returns the proficiency bonus
    """

    # Proficiency Bonus = 1 + Character Level / 4 (round up)
    return 1 + math.ceil((level) / 4)

def calculate_ability_modifier(ability_score):
    """
    Calculate the modifier for an ability score.

    Keyword arguments:
    ability_score -- score of one of the six abilities (str, dex, con, int, wis, cha)

    Returns the modifier for the ability score
    """

    # Ability Modifier = (Ability Score - 10) / 2 (round down)
    return (ability_score - 10) // 2