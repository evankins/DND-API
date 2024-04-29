DROP TABLE IF EXISTS abilities CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS characters CASCADE;
DROP TABLE IF EXISTS skills CASCADE;
DROP TABLE IF EXISTS proficiencies CASCADE;
DROP TABLE IF EXISTS character_abilities CASCADE;

CREATE TABLE IF NOT EXISTS abilities(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(25) NOT NULL UNIQUE
);

INSERT INTO abilities (id, name) VALUES 
    (1, 'Strength'),
    (2, 'Dexterity'),
    (3, 'Constitution'),
    (4, 'Intelligence'),
    (5, 'Wisdom'),
    (6, 'Charisma')
ON CONFLICT (id) DO NOTHING;

CREATE TABLE IF NOT EXISTS skills(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255) NOT NULL UNIQUE,
    ability_id       INT NOT NULL REFERENCES abilities
);

-- saving throws are included, but are initially assigned based on class and can't be changed unless the class changes
INSERT INTO skills (id, name, ability_id) VALUES 
    (1, 'Strength Saving Throw', 1),
    (2, 'Dexterity Saving Throw', 2),
    (3, 'Constitution Saving Throw', 3),
    (4, 'Intelligence Saving Throw', 4),
    (5, 'Wisdom Saving Throw', 5),
    (6, 'Charisma Saving Throw', 6),
    (7, 'Athletics', 1),
    (8, 'Acrobatics', 2),    
    (9, 'Sleight of Hand', 2),    
    (10, 'Stealth', 2),
    (11, 'Arcana', 4),
    (12, 'History', 4),
    (13, 'Investigation', 4),
    (14, 'Nature', 4),
    (15, 'Religion', 4),
    (16, 'Animal Handling', 5), 
    (17, 'Insight', 5),
    (18, 'Medicine', 5),
    (19, 'Perception', 5),
    (20, 'Survival', 5),
    (21, 'Deception', 6),
    (22, 'Intimidation', 6),
    (23, 'Performance', 6),
    (24, 'Persuasion', 6)
ON CONFLICT (id) DO NOTHING;

CREATE TABLE IF NOT EXISTS classes(
    id                          SERIAL PRIMARY KEY,
    name                        VARCHAR(255) NOT NULL UNIQUE,
    saving_throw_ability_1      INT NOT NULL REFERENCES skills, -- Saving throw proficiency
    saving_throw_ability_2      INT NOT NULL REFERENCES skills -- Saving throw proficiency
);

INSERT INTO classes (id, name, saving_throw_ability_1, saving_throw_ability_2) VALUES 
    (1, 'Barbarian', 1, 3),
    (2, 'Bard', 5, 6),
    (3, 'Cleric', 5, 4),
    (4, 'Druid', 5, 3),
    (5, 'Fighter', 1, 2),
    (6, 'Monk', 2, 3),
    (7, 'Paladin', 1, 5),
    (8, 'Ranger', 2, 4),
    (9, 'Rogue', 2, 6),
    (10, 'Sorcerer', 4, 6),
    (11, 'Warlock', 4, 5),
    (12, 'Wizard', 4, 1)
ON CONFLICT (id) DO NOTHING;

CREATE TABLE IF NOT EXISTS characters(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255) NOT NULL,
    level         INT NOT NULL,
    class_id      INT NOT NULL REFERENCES classes
);

CREATE TABLE IF NOT EXISTS character_abilities(
    id              SERIAL PRIMARY KEY,
    character_id    INT NOT NULL REFERENCES characters,
    ability_id      INT NOT NULL REFERENCES abilities,
    score           INT NOT NULL
);

CREATE TABLE IF NOT EXISTS proficiencies(
    id            SERIAL PRIMARY KEY,
    character_id  INT NOT NULL REFERENCES characters,
    skill_id       INT NOT NULL REFERENCES skills
);

