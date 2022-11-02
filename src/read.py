from pyton.connection import execute_query

def select_all():
    query = """
        SELECT * FROM heroes
    """
    list_of_heros = execute_query(query).fetchall()
    for record in list_of_heros:
        print(record[1])   

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

select_all()

get_hero_relationship(5, 3)
