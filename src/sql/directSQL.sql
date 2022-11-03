SELECT * FROM heroes;
 SELECT relationship_type_id from relationships WHERE hero1_id = 5 and hero2_id = 3;

 SELECT name from relationship_types where ID = 1;

ALTER TABLE heroes ADD patrol_group "text";

ALTER TABLE heroes DROP COLUMN patrol_group;

UPDATE heroes SET patrol_group = 'League of Villans' WHERE id = 1;

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


ALTER TABLE IF 
    SELECT COUNT(*)
    FROM   pg_attribute a
    WHERE  attrelid = 'heroes'::regclass  --  tbl here
    AND attname = 'patrol_group' = 0 heroes ADD patrol_group "text";

ALTER TABLE heroes ADD COLUMN IF NOT EXISTS patrol_group "text";

select name, patrol_group from heroes ORDER BY patrol_group;

SELECT heroes.name, ability_types.name, heroes.patrol_group  FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id; 


INSERT INTO ability_types 
