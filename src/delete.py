from pyton.connection import execute_query
from read import print_heros_with_powers
from create import copy_tables
import random

def sign_sokovia_accords():
    alter_query = """ALTER TABLE heroes DROP COLUMN patrol_group;"""
    execute_query(alter_query)
    print("Heroes work alone")

def alien_attack():
    copy_tables()
    tokyo_alien_strength = random.randint(1, 20)
    boston_alien_strength = random.randint(1, 20)
    print("Aliens are attacking Tokyo and Boston. THEY NEED URGENT HELP!!")
    if(tokyo_alien_strength > boston_alien_strength):
        print("Our intel says that the force at Tokyo is greater!")
    elif(boston_alien_strength == tokyo_alien_strength):
        print("Our intel suggests equal strength")
    else:
        print("Our intel says that Boston has a greater presence!")
    print_heros_with_powers(False)
    print('Which heroes shall we send to Tokyo?')
    tokyo_heroes = input('Input their id with spaces: ').split(' ')
    print('And to Boston?')
    boston_heroes = input('Input their id with spaces: ').split(' ')
    boston_heroes_strength = 0
    tokyo_heroes_strength = 0
    strength_query = """SELECT power_ranking from heroes WHERE id = %s;""" 
    for index in tokyo_heroes:
        tokyo_heroes_strength += execute_query(strength_query, (index,)).fetchone()[0]
    for index in boston_heroes:
        boston_heroes_strength += execute_query(strength_query, (index,)).fetchone()[0]
    if(boston_alien_strength >= boston_heroes_strength):
        if((boston_alien_strength/2) >= boston_heroes_strength):
            print("DISASTER STRIKES, ALL of the Boston heroes died!")
        else:
            print('Travesty, some of the Boston heros died')
            for index in boston_heroes:
                if(random.randint(0, 1)):
                    boston_heroes.remove(index)
                else:
                    continue
        hero_death(boston_heroes)
    else:
        print("Our brave heros in Boston were able to defeat the aliens!")

    if(tokyo_alien_strength >= tokyo_heroes_strength):
        if((tokyo_alien_strength/2) >= tokyo_heroes_strength):
            print("DISASTER STRIKES, ALL of the Tokyo heroes died!")
        else:
            print('Travesty, some of the Tokyo heros died')
            for index in tokyo_heroes:
                if(random.randint(0, 1)):
                    tokyo_heroes.remove(index)
                else:
                    continue
        hero_death(tokyo_heroes)
    else:
        print("Our brave heros in Tokyo were able to defeat the aliens!")

def hero_death(heroes):
    delete_hero_query = """DELETE FROM heroes where id = %s;"""
    delete_ability_query = """DELETE FROM abilities where id = %s;"""
    delete_ability_types_query = """DELETE FROM ability_types where id = %s;"""
    delete_relationship_query = """DELETE FROM relationships where hero1_id = %s OR hero2_id = %s;"""
    for index in heroes:
        hero_id_query = """SELECT id FROM heroes WHERE id = %s;"""
        hero_id = execute_query(hero_id_query,(index,)).fetchone()[0]
        execute_query(delete_hero_query,(hero_id,))
        execute_query(delete_ability_query,(hero_id,))
        execute_query(delete_ability_types_query,(hero_id,))
        execute_query(delete_relationship_query,(hero_id,hero_id,))


def delete_backups():
    delete_hero_query = """DROP TABLE IF EXISTS heroes_backup"""
    delete_ability_query = """DROP TABLE IF EXISTS abilities_backup"""
    delete_ability_types_query = """DROP TABLE IF EXISTS ability_type_backup"""
    delete_relationship_query = """DROP TABLE IF EXISTS relationships_backup"""
    delete_relationship_types_query = """DROP TABLE IF EXISTS relationship_type_backup"""
    query_array = [delete_hero_query, delete_ability_query, delete_ability_types_query, delete_relationship_query, delete_relationship_types_query]
    for query in query_array:
        execute_query(query)


# alien_attack()