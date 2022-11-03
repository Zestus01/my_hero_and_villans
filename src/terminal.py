from pyton.connection import execute_query
from create import *
from read import * 
from delete import *
from update import *
import random

def terminal_load():
    print("Hello commander, What is on today's docket?")
    print("1] Display current data of heros")
    print("2] Enter a new recruit")
    # print("3] Input new data on an existing hero")
    print("3] EMERGENCY ALIEN ATTACK, ACTION REQUIRED!!!")
    print("4] Query hero relationship")
    print('5] Create Patrol groups')
    print('6] Disband Patrol groups')
    print('7] Reassess power rankings of heroes')
    print("8] Close the console....")
    x = input("Awaiting your command: ")
    if(x == "1"):
        print_heros_with_powers()
    elif(x == '2'):
        hire_heroes()
    # elif(x == '3'):
    #     update_existing_hero()
    elif(x == '3'):
        alien_attack()
    elif(x == '4'):
        get_hero_relationship()
    elif(x == '5'):
        form_groups()
    elif(x == '6'):
        sign_sokovia_accords()
    elif(x == '7'):
        power_ranking()
    elif(x == '8'):
        print('Goodbye commander')
        return
    else:
        print("Commander please type in a number of the action you want to complete")    
    terminal_load()    

terminal_load()