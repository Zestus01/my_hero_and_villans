SELECT * FROM heroes;
 SELECT relationship_type_id from relationships WHERE hero1_id = 5 and hero2_id = 3;

 SELECT name from relationship_types where ID = 1;

ALTER TABLE heroes ADD Organization "text";

ALTER TABLE heroes DROP COLUMN Organization;

UPDATE heroes SET Organization = 'League of Villans' WHERE id = 1;

SELECT COUNT(id) FROM heroes 