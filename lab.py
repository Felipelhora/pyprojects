'''string_qualquer = 'ola mundo,'


PROJETOS = ['MVC', 'REST', 'REST_SIMPLE', 'LOCAL_APP']


ola = {


    "felipe": "felipe",
    
}

from src.config import GENERAL_IMPORTS


for c in GENERAL_IMPORTS:
    print (GENERAL_IMPORTS[c])'''

from src.config import CONFIG, KEY_NAME_RIGHT, KEY_NAME_LEFT, GENERAL_IMPORTS, FLASK_IMPORTS, SQLALCHEMIST_IMPORTS, BAR, ESPECIAL_IMPORTS


repository_file = ''
name_table = 'trajetoria'

def create_condicional_if_update(fields):
    repository_file = f'{repository_file}{CONFIG["spacing_3"]}if {name_table}:\n'
    for field in fields:
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}if {field}!= None:\n'
        repository_file = f'{repository_file}{CONFIG["spacing_5"]}if {field}!= None:\n'
        repository_file = f'{repository_file}{CONFIG["spacing_6"]}{name_table}.{field} = {field}\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}db_connection.session.commit()\n'
    print (repository_file)

create_condicional_if_update(fields)
    