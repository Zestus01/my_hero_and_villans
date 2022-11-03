from pyton.connection import execute_query
import random
from read import print_heros_with_powers

def power_ranking():
    create_power_rankings_query = """ALTER TABLE heroes ADD COLUMN IF NOT EXISTS power_ranking INT"""
    execute_query(create_power_rankings_query)
    count_query = """ SELECT MAX(id) FROM heroes"""
    count_heroes = execute_query(count_query).fetchone()[0]
    update_query = """UPDATE heroes SET power_ranking = %s WHERE id = %s;"""
    for index in range(1, count_heroes + 1):
        execute_query(update_query,(random.randint(1, 4),index))

def form_connections():
    hero_query = """
        SELECT id FROM heroes
    """
    id_array = []
    id_tuple = execute_query(hero_query).fetchall()
    for slot in id_tuple:
        id_array.append(slot[0])
    print(id_array)

def form_groups():
    # check_query
    initial_query = """ALTER TABLE heroes ADD COLUMN IF NOT EXISTS patrol_group "text" """
    execute_query(initial_query)
    patrol_groups = ["Cure", "Dasterdly Do-Gooders", "Tragic Backstories", "Zuper Zealots", "Survivors"]
    count_query = """ SELECT MAX(id) FROM heroes"""
    count_heroes = execute_query(count_query).fetchone()[0]
    update_query = """UPDATE heroes SET patrol_group = %s WHERE id = %s;"""
    for index in range(1, (count_heroes + 1)):
        execute_query(update_query,(random.choice(patrol_groups),index,))
    print_heros_with_powers()

form_connections()