from pyton.connection import execute_query
import random

def select_all():
    query = """
        SELECT * FROM heroes
    """
    list_of_heros = execute_query(query).fetchall()
    for record in list_of_heros:
        print(record[1] + ': ' + record[5])   

def get_hero_relationship():
    hero1ID = input('Type in the name of the first hero or ID: ')
    hero2ID = input('Type in the name of the second hero or ID: ')
    
    if(len(hero1ID) != 1):
        hero1ID = hero1ID.lower()
        name_query = """SELECT id from heroes where LOWER(heroes.name) = %s""".fetchone()[0]
        hero1ID = execute_query(name_query,(hero1ID,))
    if(len(hero2ID) != 1):
        hero2ID = hero2ID.lower()
        name_query = """SELECT id from heroes where LOWER(heroes.name) = %s""".fetchone()[0]
        hero2ID = execute_query(name_query,(hero2ID,))    

    initial_query = """
        SELECT relationship_type_id from relationships WHERE hero1_id = %s and hero2_id = %s
    """
    type_id = execute_query(initial_query,(hero1ID, hero2ID),).fetchone()
    if(type_id == None):
        print("They do not know each other")
        return
    type_id = str(type_id)
    type_id = type_id[1]
    second_query = """
        SELECT name from relationship_types where ID = %s"""
    print('They are ' + execute_query(second_query,(type_id,)).fetchone()[0])    

def print_heros_with_powers(with_space = True):
    query = """ SELECT heroes.id, heroes.name, string_agg(ability_types.name, ', '), heroes.power_ranking, heroes.patrol_group FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id 
            GROUP BY heroes.id
            ORDER BY heroes.id;
            """
    heros_with_powers = execute_query(query).fetchall()
    for record in heros_with_powers:
        if(with_space):
            print('')
        print('ID:' + str(record[0]) +' ' + record[1] + ' with the abilities ' + record[2] + ' Their strength level is :' + str(record[3]) + '. Patrolling with the ' + record[4])  
    print(' ')
