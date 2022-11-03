from pyton.connection import execute_query
import random

def form_groups():
    # check_query
    intial_query = """ALTER TABLE heroes ADD COLUMN IF NOT EXISTS patrol_group "text" """
    execute_query(intial_query)
    patrol_groups = ["Cure", "Dasterdly Do-Gooders", "Tragic Backstories", "Synaptek", "Zuper Zealots"]
    count_query = """ SELECT COUNT(id) FROM heroes"""
    count_heroes = execute_query(count_query).fetchone()[0]
    update_query = """UPDATE heroes SET patrol_group = %s WHERE id = %s;"""
    for index in range(1, (count_heroes + 1)):
        execute_query(update_query,(random.choice(patrol_groups),index,))
    print_heros_with_powers()

def acquire_rights_a_franchise():
    insert_query = """ """

def hire_heroes():
    print('Great, always looking for fresh heroes. Are they from an existing group or new hire?')
    x = input("1 for group, 2 for new hire: ")
    if(x == '1'):
        acquire_rights_a_franchise()
    elif(x == '2'):
        enter_new_recruit()

def enter_new_recruit():
    hero_name = input("Hero name: ")
    abilities = input("What are their abilities: ")
    bio = input("What is their backstory? ")
