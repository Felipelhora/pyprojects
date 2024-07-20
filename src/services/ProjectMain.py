import os
from src.config import CONFIG, BAR
from src.services.TextFiles import TextFiles

class ProjectMain(TextFiles):
    def __init__(self) -> None:
        pass

    def create_path(self, path:str)->None:
        try:
            os.makedirs(path)
        except:
            ...
        return None

    def create_files_project(self, path:str, text:str)->None:
        with open(path, 'w+') as file:
            file.write(text)

    def create_folders(self, path:str, folders:list):
        for folder in folders:
            self.create_path(f'{path}{BAR}{folder}')


    def create_base_project(self, installation_folder:str, type_project:str, licence:str, readme:str):
        # COMMON FOLDERS
        self.create_folders(path=installation_folder, folders=CONFIG['common_folders'])
        # CONFIG 
        self.create_files_project(path=f'{installation_folder}{BAR}src{BAR}config.py', text=self.config_text_base(type_project))
        # env e env_example
        self.create_files_project(path=f'{installation_folder}{BAR}.env', text=self.env_text_base(type_project))
        self.create_files_project(path=f'{installation_folder}{BAR}.env_example', text=self.env_text_base(type_project))
        # requeriments
        self.create_files_project(path=f'{installation_folder}{BAR}requeriments', text=self.requeriments_text_base(type_project))
        # licence
        self.create_files_project(path=f'{installation_folder}{BAR}licence', text=self.licences_text(licence))
        # Readme
        self.create_files_project(path=f'{installation_folder}{BAR}docs{BAR}readme.md', text=self.readme_text(readme))
