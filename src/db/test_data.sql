INSERT INTO stats (name) VALUES 
    ('Strength'),
    ('Dexterity'),
    ('Constitution'),
    ('Intelligence'),
    ('Wisdom'),
    ('Charisma');

INSERT INTO classes (name, stp_id_1, stp_id_2) VALUES 
    ('Barbarian', 1, 3),
    ('Bard', 5, 6),
    ('Cleric', 5, 4),
    ('Druid', 5, 3),
    ('Fighter', 1, 2),
    ('Monk', 2, 3),
    ('Paladin', 1, 5),
    ('Ranger', 2, 4),
    ('Rogue', 2, 6),
    ('Sorcerer', 4, 6),
    ('Warlock', 4, 5),
    ('Wizard', 4, 1);

INSERT INTO characters (name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, class_id) VALUES 
    ('Character 1', 1, 10, 12, 14, 8, 16, 13, 1),
    ('Character 2', 2, 12, 14, 10, 16, 8, 13, 2),
    ('Character 3', 3, 14, 10, 12, 8, 13, 16, 3);


INSERT INTO skills (name) VALUES 
    ('Acrobatics'),
    ('Animal Handling'),
    ('Arcana'),
    ('Athletics'),
    ('Deception'),
    ('History'),
    ('Insight'),
    ('Intimidation'),
    ('Investigation'),
    ('Medicine'),
    ('Nature'),
    ('Perception'),
    ('Performance'),
    ('Persuasion'),
    ('Religion'),
    ('Sleight of Hand'),
    ('Stealth'),
    ('Survival');

INSERT INTO skill_proficiencies (character_id, skill_id) VALUES 
    (1, 1),
    (1, 4),
    (1, 8),
    (1, 9),
    (1, 12),
    (1, 13),
    (1, 15),
    (1, 17),
    (1, 18),
    (2, 2),
    (2, 3),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 10),
    (2, 11),
    (2, 14),
    (2, 16),
    (3, 1),
    (3, 4),
    (3, 8),
    (3, 9),
    (3, 12),
    (3, 13),
    (3, 15),
    (3, 17),
    (3, 18);
