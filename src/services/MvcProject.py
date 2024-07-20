from src.services.Models import Models
from src.services.Repositorys import Repositorys
from src.config import CONFIG, BAR  



    


class MvcProject(Models, Repositorys):
    def __init__(self, instalation_info:dict) -> None:
        self.type_project = instalation_info['type_project']
        self.type_databases = instalation_info['type_databases']
        self.installation_folder = instalation_info['installation_folder']
        self.licence = instalation_info['licence']
        self.readme = instalation_info['readme']
        self.models = instalation_info['models']
        pass

    def create_mvc_project(self):
        # COMMON FOLDERS
        self.create_base_project(installation_folder=self.installation_folder, type_project=self.type_project, licence=self.licence, readme=self.readme)
        # MVC FOLDERS
        self.create_folders(path=self.installation_folder, folders=CONFIG['mvc_paths'])
        self.create_models_files(installation_folder=self.installation_folder, type_databases=self.type_databases, models=self.models)
        # REPOSITORIES FILES
        self.create_repository_files(installation_folder=self.installation_folder, models=self.models)

        
        
        

