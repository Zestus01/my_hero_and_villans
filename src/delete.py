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
    print("Aliens are attacking Tokyo, and Boston. THEY NEED URGENT HELP")
    print_heros_with_powers(False)
    print('Which heroes shall we send to Tokyo?')
    tokyo_heroes = input('Input their id: ').replace(' ', '')
    print('And to Boston?')
    boston_heroes = input('Input their id: ').replace(' ', '')
    boston_heroes_strength = 0
    tokyo_heroes_strength = 0
    strength_query = """SELECT power_ranking from heroes WHERE id = %s;""" 
    for index in tokyo_heroes:
        tokyo_heroes_strength += execute_query(strength_query, (index,)).fetchone()[0]
    for index in boston_heroes:
        boston_heroes_strength += execute_query(strength_query, (index,)).fetchone()[0]           
    tokyo_alien_strength = random.randint(1, 10)
    boston_alien_strength = random.randint(1, 10)

def delete_backups():
    delete_hero_query = """DROP TABLE IF EXISTS heroes_backup"""
    delete_ability_query = """DROP TABLE IF EXISTS abilities_backup"""
    delete_ability_types_query = """DROP TABLE IF EXISTS ability_type_backup"""
    delete_relationship_query = """DROP TABLE IF EXISTS relationships_backup"""
    delete_relationship_types_query = """DROP TABLE IF EXISTS relationship_type_backup"""
    query_array = [delete_hero_query, delete_ability_query, delete_ability_types_query, delete_relationship_query, delete_relationship_types_query]
    for query in query_array:
        execute_query(query)

delete_backups()
# alien_attack()