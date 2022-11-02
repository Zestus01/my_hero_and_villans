from pyton.connection import execute_query
import random

def select_all():
    query = """
        SELECT * FROM heroes
    """
    list_of_heros = execute_query(query).fetchall()
    for record in list_of_heros:
        print(record[1] + ': ' + record[5])   

def get_hero_relationship(hero1ID, hero2ID):
    intial_query = """
        SELECT relationship_type_id from relationships WHERE hero1_id = %s and hero2_id = %s
    """
    
    type_id = execute_query(intial_query,(hero1ID, hero2ID),).fetchone()
    type_id = str(type_id)
    type_id = type_id[1]
    second_query = """
        SELECT name from relationship_types where ID = %s"""

    print(execute_query(second_query,(type_id,)).fetchone()[0])    

def print_heros_with_powers():
    query = """ SELECT heroes.name, ability_types.name FROM heroes
            JOIN abilities ON heroes.id = abilities.hero_id
            JOIN ability_types on ability_types.id = abilities.ability_type_id
            """
    heros_with_powers = execute_query(query).fetchall()
    for record in heros_with_powers:
        print('')
        print(record[0] + ': ' + record[1])
    print('')    

def form_groups():
    intial_query = """ALTER TABLE heroes ADD Organization "text";"""
    execute_query(intial_query)
    organizations = ["The Cure", "Goody-two-shoes", "Tragic Backstories", "Synaptek"]
    count_query = """ SELECT COUNT(id) FROM heroes"""
    count_heroes = execute_query(count_query).fetchone()[0]
    update_query = """UPDATE heroes SET Organization = %s WHERE id = %s;"""
    for index in range(1, (count_heroes + 1)):
        execute_query(update_query,(random.choice(organizations),index,))
    select_all()

form_groups()

print_heros_with_powers()

get_hero_relationship(5, 3)
