from src.config import CONFIG, BAR, SQLALCHEMIST_IMPORTS, ESPECIAL_IMPORTS
from src.services.ProjectMain import ProjectMain



class Models(ProjectMain):
    
    def create_models_files(self, installation_folder:str, type_databases:str, models:list):
        # DBconnectionHandler
        self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}models{BAR}DBConnectionHandler.py", text=self.db_connection_handler_text(type_database=type_databases))
        # db_base
        self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}models{BAR}db_base.py", text=self.db_base_text())
        # models
        for model in models:
            self.create_single_model(model=model, installation_folder=installation_folder)
        # create databaseslHandler
        self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}models{BAR}DataBasesHandler.py", text=self.db_handler_text(models))
        self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}models{BAR}__init__.py", text=self.init_models_text(models))
    
    def create_single_model(self, model:dict, installation_folder:str=None):
        if  installation_folder == None:
            installation_folder = f"{CONFIG['local_path']}{BAR}src{BAR}models{BAR}{self.convert_snakecase_to_camelcase(model['table_name'])}.py"
        else:
            installation_folder = f"{installation_folder}{BAR}src{BAR}models{BAR}{self.convert_snakecase_to_camelcase(model['table_name'])}.py"
        self.create_files_project(path=installation_folder, text=self.model_text(fields=model['fields'], table_name=model['table_name']))



