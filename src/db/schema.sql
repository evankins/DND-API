DROP TABLE IF EXISTS abilities CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS characters CASCADE;
DROP TABLE IF EXISTS skills CASCADE;
DROP TABLE IF EXISTS proficiencies CASCADE;
DROP TABLE IF EXISTS character_abilities CASCADE;

CREATE TABLE abilities(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(25) NOT NULL
);

CREATE TABLE classes(
    id                          SERIAL PRIMARY KEY,
    name                        VARCHAR(255) NOT NULL,
    saving_throw_ability_1      INT NOT NULL REFERENCES abilities, -- Saving throw proficiency
    saving_throw_ability_2      INT NOT NULL REFERENCES abilities -- Saving throw proficiency
);

CREATE TABLE characters(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255) NOT NULL,
    level         INT NOT NULL,
    class_id      INT NOT NULL REFERENCES classes
);

CREATE TABLE character_abilities(
    id              SERIAL PRIMARY KEY,
    character_id    INT NOT NULL REFERENCES characters,
    ability_id      INT NOT NULL REFERENCES abilities,
    score           INT NOT NULL
);

CREATE TABLE skills(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(255) NOT NULL,
    ability_id       INT NOT NULL REFERENCES abilities
);

CREATE TABLE proficiencies(
    id            SERIAL PRIMARY KEY,
    character_id  INT NOT NULL REFERENCES characters,
    skill_id       INT NOT NULL REFERENCES skills
);

