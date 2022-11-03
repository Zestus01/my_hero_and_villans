SELECT * FROM heroes;
 SELECT relationship_type_id from relationships WHERE hero1_id = 5 and hero2_id = 3;

 SELECT name from relationship_types where ID = 1;

SELECT relationship_type_id from relationshipstsasd WHERE hero1_id = 2 and hero2_id = 113;

INSERT INTO abilities (hero_id, ability_type_id) VALUES (15, 5);
INSERT INTO heroes(name, about_me, biography) VALUES ('Chill Woman', 'Chill', 'Test');
ALTER TABLE heroes ADD patrol_group "text";

INSERT (hero1_id, hero2_id, relationship_type_id);


SELECT *
FROM information_schema.tables
WHERE Table_type = 'BASE TABLE'
and TABLE_NAME = 'heroes_backup';
WHERE name = 'Artists';
INSERT INTO heroes (name, about_me, biography) VALUES ('Saitama', 'One-punch guy', 'ONE PUNCH MAN');
SELECT ID FROM heroes WHERE id = 5;
DELETE FROM heroes where name = 'Test';
DELETE FROM ability_types WHERE name = 'You will Die';
DELETE FROM abilities where hero_id = 14;

INSERT INTO heroes (name, about_me, biography) VALUES ('Kelsier', 'A man with conviction who fights for the good of the common people. Sacrifices himself to save others', 'Kelsier is the main male character in the first book of the Mistborn trilogy, and he is the leader of the rebel crew and Vins mentor. Most commonly known among the skaa as the Survivor, Kelsier is a wily Mistborn who plans to topple Lord Ruler. Kelsier becomes the new God figure that replaces Lord Ruler starting the Church of the Survivor revered by the Skaa, 
he is now known as a religious figure, the religion is called Survivorism');

SELECT heroes.id, heroes.name, string_agg(ability_types.name, ', '), heroes.power_ranking, heroes.patrol_group FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id 
            GROUP BY heroes.id
            ORDER BY heroes.id;
INSERT INTO ability_types(name) VALUES ('One-punch');
ALTER TABLE heroes DROP COLUMN patrol_group;
CREATE TABLE IF NOT EXISTS heroes_backup();
IF NOT EXISTS heroes_backup SELECT  * INTO heroes_backup FROM heroes;

INSERT INTO relationships (hero1_id, hero2_id, relationship_type_id) VALUES (2, 11, 1);

DROP TABLE IF EXISTS heroes_backup;

SELECT power_ranking from heroes WHERE id = 2;

ALTER TABLE heroes ADD COLUMN IF NOT EXISTS power_ranking INT;

DROP TABLE heroes_backup;

SELECT * INTO heroes_backup FROM heroes;

SELECT heroes.id, heroes.name, string_agg(ability_types.name, ', '), heroes.patrol_group FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id 
            GROUP BY heroes.id;

UPDATE heroes SET patrol_group = 'League of Villans' WHERE id = 1;

select * from hereos_backup;

EXISTS(heroes.patrol_group) IS NOT NULL
BEGIN
    SELECT COUNT(id) FROM heroes
END;

IF EXISTS(SELECT 1 FROM sys.COLUMNS WHERE name = N'patrol_group' AND OBJECT_ID = OBJECT_ID(N'heroes.heroes'))
BEGIN
    SELECT COUNT(id) FROM heroes
END;

SELECT IFNULL(COL_LENGTH(heroes.patrol_group),
BEGIN
    SELECT COUNT(id) FROM heroes
END;

Select id from heroes where LOWER(heroes.name) = 'Chill woman';

SELECT relationship_type_id from relationships WHERE hero1_id = 1 and hero2_id = 3;


SELECT *
    FROM   pg_attribute a
    WHERE  attrelid = 'heroes'::regclass
    and attname = 'heroes_backup';

ALTER TABLE IF 
    SELECT COUNT(*)
    FROM   pg_attribute a
    WHERE  attrelid = 'heroes'::regclass  --  tbl here
    AND attname = 'patrol_group' = 0 heroes ADD patrol_group "text";

SELECT *
    FROM   pg_attribute a
    WHERE  attrelid = 'heroes'::regclass

ALTER TABLE heroes ADD COLUMN IF NOT EXISTS patrol_group "text";

select * from heroes;

DELETE FROM relationships WHERE hero1_id = 11 or hero2_id = 11;

select name, patrol_group from heroes ORDER BY patrol_group;
SELECT heroes.name, ability_types.name, heroes.patrol_group  FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id; 


INSERT INTO ability_types (name) VALUES ('Size manipulation'), ('Power siphoning'), ('Shapeshifting'), ('Edit Source-Code'), ('Allomancy'), ('Billionaire');

DROP 

select id from heroes where name = 'Kelsier';

select Max(id) from heroes;

UPDATE heroes SET patrol_group = 'Test 5' WHERE id = 7;

SELECT id from ability_types WHERE name = 'Allomancy';

INSERT INTO hereos (name, about_me, biography) VALUES ('Vin', 'A street urchin who defeats a god, then becomes one herself', 'Street Urchin');
INSERT INTO abilities(hero_id, ability_type_id) SELECT id.heroes, ability_types.id FROM heroes s1 INNER JOIN ability_types s2 ON s1.id = s2.id;
DELETE FROM heroes WHERE name = 'Kelsier';
DELETE FROM ability_types WHERE name = 'Billionaire';
DELETE FROM ability_types WHERE name = 'Allomancy';
DELETE FROM ability_types WHERE name = 'Edit Source-Code';
DELETE FROM ability_types WHERE name = 'Power siphoning';
DELETE FROM ability_types WHERE name = 'Size manipulation' ;
DELETE FROM ability_types WHERE name = 'Shapeshifting';