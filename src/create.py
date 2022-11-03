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
    x = input("1 for group, 2 for new hire: ")
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
    insert_hero_query = """INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s);"""
    insert_ability_query = """INSERT INTO ability_types (name) VALUES (%s)"""
    execute_query(insert_hero_query, (hero_name, about_them, bio,))
    execute_query(insert_ability_query,(hero_ability,))
    connect_abilities(hero_name, hero_ability)

def connect_abilities(hero_name, hero_ability):
    hero_id_query = """ SELECT id FROM heroes WHERE LOWER(name) = %s;"""
    hero_id = execute_query(hero_id_query,(hero_name.lower(),)).fetchone()[0]
    ability_id_query = """SELECT id from ability_types WHERE LOWER(name) = %s;"""
    ability_id = execute_query(ability_id_query,(hero_ability.lower(),)).fetchone()[0]
    insert_query = """INSERT INTO abilities(hero_id, ability_type_id) VALUES (%s, %s);"""
    execute_query(insert_query,(hero_id, ability_id))

def copy_tables():
    check_query = """SELECT * FROM information_schema.tables 
                WHERE Table_type = 'BASE TABLE'
                and TABLE_NAME = 'heroes_backup';"""
    if(execute_query(check_query).fetchone()[0] != 'postgres'):
        copy_hero_query = """SELECT * INTO heroes_backup FROM heroes"""
        copy_ability_query = """SELECT * INTO abilities_backup FROM abilities"""
        copy_ability_types_query = """SELECT * INTO ability_type_backup FROM ability_types"""
        copy_relationship_query = """SELECT * INTO relationships_backup FROM relationships"""
        copy_relationship_types_query = """SELECT * INTO relationship_type_backup FROM relationship_types"""
        query_array = [copy_hero_query, copy_ability_query, copy_ability_types_query, copy_relationship_query, copy_relationship_types_query]
        for query in query_array:
            execute_query(query)
