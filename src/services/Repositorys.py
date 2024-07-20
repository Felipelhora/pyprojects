from src.config import CONFIG, BAR
from src.services.ProjectMain import ProjectMain

class Repositorys(ProjectMain) :


    def create_repository_files(self, installation_folder:str, models:list) ->None:
        self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}repositories{BAR}ResultHandlerRepository.py", text=self.result_handle_repositories_text())
        for model in models:
            print (model)
            self.create_files_project(path=f"{installation_folder}{BAR}src{BAR}repositories{BAR}{self.convert_snakecase_to_camelcase(model['table_name'])}Repository.py", text=self.repositories_text(model))


    ''' def __init__(self) -> None:
        self.fields = []
        self.name_camecase = ''

    def __get_abbreviation_type(self, type_name:str)-> str:
        if type_name == 'Integer':
            return 'int'
        if type_name == 'Boolean':
            return 'bool'
        else:
            return 'str'

    def __manipule_entry_parameters(self, fields:list)-> str:    
        fields_temp = []
        start_str = '(self,'
        for field in fields:
            fields_temp.append(field['name'])
            start_str = f"{start_str} {field['name']}:{self.__get_abbreviation_type(field['type'])}=None,"
        start_str = f"{start_str}fields=None, limit=None, order_by:list=None) -> dict:"
        return start_str
            
            



    def create_repository(self, table_name:str, fields:list) ->None:
        self.name_camecase = self.manipule_name_file(table_name=table_name)
        output_path = f"{CONFIG['local_path']}{BAR}{self.name_camecase}"
        with open(f"{output_path}Repository.py", 'w+') as repository_file:
             repository_file.write(f'class {self.manipule_name_file(table_name=table_name)}(Result_handler_repository):')
             repository_file.write('\n')
             repository_file.write('\n')
             # function __filter_by_field
             repository_file.write(f'{CONFIG["spacing_1"]}def __filter_by_field(self, fields:list, record:dict):\n')
             repository_file.write(CONFIG['spacing_2'] + 'new_dictionary = {key: value for key, value in record.items() if key in fields}\n')
             repository_file.write(CONFIG['spacing_2'] + 'return new_dictionary\n')
             repository_file.write('\n')
             repository_file.write(CONFIG['spacing_1'] + 'def select_'+ table_name + self.__manipule_entry_parameters(fields=fields))
             repository_file.write('\n')
             repository_file.write(f"{CONFIG['spacing_2']} with DBConnectionHandler() as db_connection:\n{CONFIG['spacing_3']}query = db_connection.session.query({self.manipule_name_file(table_name=table_name)})")
             repository_file.write('\n')
             repository_file.write(self.__create_filter_by_select(fields=fields))
'''