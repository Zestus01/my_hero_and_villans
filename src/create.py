from pyton.connection import execute_query
from read import *
import random

def form_groups():
    intial_query = """ALTER TABLE heroes ADD COLUMN IF NOT EXISTS patrol_group "text" """
    execute_query(intial_query)
    patrol_groups = ["Cure", "Dasterdly Do-Gooders", "Tragic Backstories", "Zuper Zealots", "Survivors"]
    count_query = """ SELECT MAX(id) FROM heroes"""
    count_heroes = execute_query(count_query).fetchone()[0]
    update_query = """UPDATE heroes SET patrol_group = %s WHERE id = %s;"""
    for index in range(1, (count_heroes + 1)):
        execute_query(update_query,(random.choice(patrol_groups),index,))
    print_heros_with_powers()

def acquire_rights_a_franchise():
    print("Which franchise did you purchase?")
    franchise = input('1] The Boys, or 2] Marvel')
    if(franchise == '1'):
        franchise_insert_query = """ """

def hire_heroes():
    print('Great, always looking for fresh heroes. Are they from an existing group or new hire?')
    x = input("Only have new hire paperwork, 2 for new hire: ")
    if(x == '1'):
        acquire_rights_a_franchise()
    elif(x == '2'):
        enter_new_recruit()

def enter_new_recruit():
    hero_name = input("Hero name: ")
    hero_ability = input("What are their abilities: ")
    bio = input("What is their backstory? ")
    about_them = input('What is their personality? ')
    recruit_hero(hero_name, about_them, bio, hero_ability)
    

def recruit_hero(hero_name, about_them, bio, hero_ability):    
    insert_hero_query = """INSERT INTO heroes (name, about_me, biography, power_ranking, patrol_group) VALUES (%s, %s, %s, 1, 'Newbies');"""
    insert_ability_query = """INSERT INTO ability_types (name) VALUES (%s)"""
    execute_query(insert_hero_query, (hero_name, about_them, bio,))
    execute_query(insert_ability_query,(hero_ability,))
    connect_abilities(hero_name, hero_ability)

def connect_abilities(hero_name, hero_ability):
    hero_id_query = """ SELECT id FROM heroes WHERE LOWER(name) = %s;"""
    hero_id = execute_query(hero_id_query,(hero_name.lower(),)).fetchone()[0]
    if(type(hero_ability) == int):
        ability_id_query ="""SELECT id from ability_types WHERE id = %s;"""
    else:    
        ability_id_query = """SELECT id from ability_types WHERE LOWER(name) = %s;"""
        hero_ability = hero_ability.lower()
    ability_id = execute_query(ability_id_query,(hero_ability,)).fetchone()[0]
    insert_query = """INSERT INTO abilities(hero_id, ability_type_id) VALUES (%s, %s);"""
    execute_query(insert_query,(hero_id, ability_id))

def copy_tables():
    check_query = """SELECT * FROM information_schema.tables 
                WHERE Table_type = 'BASE TABLE'
                and TABLE_NAME = 'heroes_backup';"""
    if(execute_query(check_query).fetchone()[0] != 'postgres'):
        copy_hero_query = """SELECT * INTO heroes_backup FROM heroes"""
        copy_ability_query = """SELECT * INTO abilities_backup FROM abilities"""
        copy_relationship_query = """SELECT * INTO relationships_backup FROM relationships"""
        query_array = [copy_hero_query, copy_ability_query, copy_relationship_query]
        for query in query_array:
            execute_query(query)

def lazarus_project():
    zombie_check_query = """SELECT COUNT(*) FROM ability_types WHERE name = 'Zombie';"""
    zombie_check = execute_query(zombie_check_query).fetchone()[0]
    if(zombie_check == 0):
        zombie_insert_query = """INSERT INTO ability_types(name) VALUES ('Zombie');"""
        execute_query(zombie_insert_query)
    count_query = """SELECT MAX(id) FROM heroes_backup"""
    count_heroes = execute_query(count_query).fetchone()[0]
    insert_heroes_conflict_query = """INSERT INTO heroes (name, about_me, biography, patrol_group, power_ranking) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;"""
    ability_count_query = """SELECT COUNT(*) from abilities_backup WHERE hero_id = %s"""
    relationship_count_query = """SELECT COUNT(*) from relationships_backup WHERE hero1_id = %s OR hero2_id = %s"""
    hero_data_query = """SELECT * from heroes_backup WHERE id = %s;"""
    hero_check_query = """Select COUNT(*) from heroes where LOWER(name) = %s"""
    for index in range(1, (count_heroes + 1)):
        hero_data = execute_query(hero_data_query, (index,)).fetchall()
        if(hero_data):
            hero_check = execute_query(hero_check_query,(hero_data[0][1].lower(),)).fetchone()[0]
            if(hero_check == 0):
                execute_query(insert_heroes_conflict_query,(hero_data[0][1], hero_data[0][2], hero_data[0][3], hero_data[0][5], hero_data[0][6]))
                hero_id_query = """SELECT id FROM heroes WHERE LOWER(name) = %s;"""
                hero_id = execute_query(hero_id_query,(hero_data[0][1].lower(),)).fetchone()[0]
                ability_count = execute_query(ability_count_query, (hero_id,)).fetchone()[0]
                ability_query = """SELECT * from abilities_backup WHERE hero_id = %s;"""
                ability = execute_query(ability_query, (hero_id,)).fetchall()
                for index2 in range(0, ability_count):
                    connect_abilities(hero_data[0][1], ability[index2][2])
                connect_abilities(hero_data[0][1], 'Zombie')    
    

def test_function():
    query = hero_check_query = """Select COUNT(*) from heroes where LOWER(name) = %s"""
    placeholder = execute_query(query, ('test man'.lower(),)).fetchone()[0]
    if(placeholder == 0):
        print('True')
    else:
        print('False')
test_function()    