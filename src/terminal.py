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
    print("3] Throw a party?")
    print("4] EMERGENCY ALIEN ATTACK, ACTION REQUIRED!!!")
    print("5] Query hero relationship")
    print('6] Create Patrol groups')
    print('7] Disband Patrol groups')
    print('8] Reassess power rankings of heroes')
    print('9] Bring the heroes back from the dead')
    print("10] Close the console....")
    x = input("Awaiting your command: ")
    if(x == "1"):
        print_heros_with_powers()
    elif(x == '2'):
        hire_heroes()
    elif(x == '3'):
        form_connections()
    elif(x == '4'):
        alien_attack()
    elif(x == '5'):
        get_hero_relationship()
    elif(x == '6'):
        form_groups()
    elif(x == '7'):
        sign_sokovia_accords()
    elif(x == '8'):
        power_ranking()
    elif(x == '9'):
        lazarus_project()
        delete_backups()
    elif(x == '10'):
        print('Goodbye commander')
        return
    else:
        print("Commander please type in a number of the action you want to complete")    
    terminal_load()    

terminal_load()