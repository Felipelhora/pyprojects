from src.services.Models import Models
from src.services.Repositorys import Repositorys




fields = [
            {
                "name" : "id",
                "type" : "Integer",
                "additional_parameter" : "primary_key=True"
            },
            {
                "name" : "categoria",
                "type" : "String",
                "additional_parameter" : "100"
            },
            {
                "name" : "valor",
                "type" : "Integer",
                "additional_parameter" : None
            },
            {
                "name" : "especie",
                "type" : "String",
                "additional_parameter" : "100"
            },
            {
                "name" : "sub_especie",
                "type" : "String",
                "additional_parameter" : "100"
            },
            {
                "name" : "data_evento",
                "type" : "String",
                "additional_parameter" : "timezone=True"
            },
            {
                "name" : "cadastrante",
                "type" : "String",
                "additional_parameter" : "20"
            }
        ]
            

#Models().create_model(table_name='despesas_gastos_mensais', fields=fields)
#Repositorys().create_repository(table_name='despesas_gastos_mensais', fields=fields)

'''from src.controllers.project_choice_controller import project_choice_controller
import os

PROJETOS = ['MVC', 'REST', 'REST_SIMPLE', 'LOCAL_APP']
local = f"{os.getcwd()}/teste"

project_choice_controller('REST', local)

from src.services.TextFiles import TextFiles

print(TextFiles().config_text_base('REST_SIMPLE'))'''

'''
        self.type_project = instalation_info['type_project']
        self.installation_folder = instalation_info['installation_folder']
        self.licence = instalation_info['licence']
        self.readme = instalation_info['readme']

'''
from src.services.MvcProject import MvcProject
import os




models = [
            {
                "table_name": "gastos_despesas_mensais",
                "fields": fields
            },
            {
                "table_name": "gastos_despesas_mensais2",
                "fields": fields
            }
        ]

MVC =   {
            "type_project":"REST",
            "installation_folder": f"{os.getcwd()}/teste",
            "licence": "MIT",
            "readme": "",
            "type_databases": "postgresql",
            "models": models

        }

MvcProject(MVC).create_mvc_project()