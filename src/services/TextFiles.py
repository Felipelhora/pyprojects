from src.config import CONFIG, KEY_NAME_RIGHT, KEY_NAME_LEFT, GENERAL_IMPORTS, FLASK_IMPORTS, SQLALCHEMIST_IMPORTS, BAR, ESPECIAL_IMPORTS



class TextFiles:
    def __init__(self) -> None:
        self.config = ''


    def convert_snakecase_to_camelcase(self, text:str) -> str:
        file_name = text.split('_')
        answer = ''
        for words in file_name:
            words = words.capitalize()
            answer = f'{answer}{words}'
        return answer

    def decode_dict_values_from_text(self,dict_infos:dict, base_text:str) ->str:
        for import_ in dict_infos:
            base_text = f"{base_text}{dict_infos[import_]}\n"
        return base_text

    def insert_repositories_text(self, fields:list, uuid:str=None) ->str:
        start_str = ''
        for field in fields:
            if {field['name']} == 'uuid' and uuid == None:
                start_str = f"{start_str} {field['name']}= uuid4(),"    
            else:
                start_str = f"{start_str} {field['name']}={field['name']},"
        start_str = f"({start_str[:-1]})"
        return start_str


    def config_text_base(self, project:str)->str:
        config_text = ''
        # IMPORTS
        config_text = self.decode_dict_values_from_text(GENERAL_IMPORTS, config_text)
        if project == 'REST' or project == 'REST_SIMPLE':
           config_text = self.decode_dict_values_from_text(FLASK_IMPORTS, config_text)
        # function bar
        config_text = f"{config_text}\ndef bar_system()->str:\n"
        config_text = f"{config_text}{CONFIG['spacing_1']}if platform.system() == 'Windows':\n"
        config_text = f"{config_text}{CONFIG['spacing_2']}return '/'\n"
        config_text = f"{config_text}{CONFIG['spacing_1']}if platform.system() == 'Linux':\n"
        config_text = f"{config_text}{CONFIG['spacing_2']}return '/'\n\n"
        config_text = f"{config_text}BAR = bar_system()\n\n"
        # CONFIG
        config_text = f"{config_text}CONFIG = {KEY_NAME_LEFT}\n{CONFIG['spacing_3']}'local_path':os.getcwd(),\n{CONFIG['spacing_3']}'resources_path':os.getcwd() + BAR + 'resources',\n{CONFIG['spacing_3']}'temp_path':os.getcwd() + BAR + 'temp',\n"
        if project == 'REST' or project == 'REST_SIMPLE':
            config_text = f"{config_text}\n{CONFIG['spacing_3']}'port': config('system_port'),"
            config_text = f"{config_text}\n{CONFIG['spacing_3']}'host': config('host')\n"
        config_text = f"{config_text}{CONFIG['spacing_3']}{KEY_NAME_RIGHT}\n\n"
        if project == 'REST' or project == 'MVC':
           # CONFIG_DATABASE
            config_text = f"{config_text}CONFIG_DATABASE = {KEY_NAME_LEFT}\n{CONFIG['spacing_3']}'user_db':config('user_db'),\n{CONFIG['spacing_3']}'passw_db':config('passw_db'),\n{CONFIG['spacing_3']}'host_db':config('host_db'),\n{CONFIG['spacing_3']}'port_db':config('port_db'),\n{CONFIG['spacing_3']}'database':config('database'),\n{CONFIG['spacing_3']}'database_service':config('database_service')\n"
            config_text = f"{config_text}{KEY_NAME_RIGHT}\n\n"
        if project == 'REST' or project == 'REST_SIMPLE':
            config_text = f"{config_text}server = Flask(__name__)\nphotos = UploadSet('photos', IMAGES)\nserver.config['UPLOADED_PHOTOS_DEST'] = CONFIG['temp_path']\nconfigure_uploads(server, photos)"
        return config_text


    def env_text_base(self, project:str)->str:
        text_env = ''
        if project == 'REST' or project == 'REST_SIMPLE':
           text_env = f'{text_env}rost=\nport=\n'
        if project == 'REST' or project == 'MVC':
           text_env = f'{text_env}user_db=\npassw_db=\ndatabase=\nhost_db=\nport_db=\ndatabase_service='
        return text_env

    def requeriments_text_base(self, project:str, types:list=None)->str:
        text_requeriments = 'python-decouple\n'
        if project == 'REST' or project == 'REST_SIMPLE':
           text_requeriments = f'{text_requeriments}flask\nFlask-JSON\nFlask-Reuploaded\nflask_cors\nitsdangerous\nPyJWT\nrequests'
        if project == 'REST' or project == 'MVC':
           text_requeriments = f'{text_requeriments}pymysql\nSQLAlchemy\n'
        return text_requeriments
    

    def licences_text(self, licence:str)->str:
        text_licence = ''
        return text_licence
    
    def readme_text(self, readme:str)->str:
        text_readme = ''
        return text_readme
    
    #### MODELS

    def db_connection_handler_text(self, type_database:str) ->str:
        db_handler_text = ''
        # IMPORTS
        db_handler_text = self.decode_dict_values_from_text(SQLALCHEMIST_IMPORTS, db_handler_text)
        # CLASS
        db_handler_text = f"{db_handler_text}\nclass DBConnectionHandler:\n    '''Sqlalchemy database connection'''\n\n"
        # __init__
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_1']}def __init__(self)->None:\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}self.__connection_string ="
        if type_database == 'postgresql':
            db_handler_text = db_handler_text + '"postgresql://{}:{}@{}:{}/{}".format(DB_CONFIG["db_username"],DB_CONFIG["db_password"],DB_CONFIG["db_host"], DB_CONFIG["db_port"], DB_CONFIG["db_name"])\n'
        if type_database =='mysql' or type_database =='mariadb':
            db_handler_text = db_handler_text + +'"postgresql://{}:{}@{}:{}/{}".format(DB_CONFIG["db_username"],DB_CONFIG["db_password"],DB_CONFIG["db_host"], DB_CONFIG["db_port"], DB_CONFIG["db_name"])\n'
        if type_database =='sqlite':
            db_handler_text = db_handler_text + '"postgresql://{}:{}@{}:{}/{}".format(DB_CONFIG["db_username"],DB_CONFIG["db_password"],DB_CONFIG["db_host"], DB_CONFIG["db_port"], DB_CONFIG["db_name"])\n'
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}self.session = None\n\n"
        # get_engine
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_1']}def get_engine(self):\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}engine = create_engine(self.__connection_string)\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}return engine\n\n"
        # __enter__
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_1']}def __enter__(self):\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}engine = create_engine(self.__connection_string)\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}session_maker = sessionmaker()\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}self.session = session_maker(bind=engine)\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}return self\n\n"
        # __exit__
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_1']}def __exit__(self, exc_type, exc_val, exc_tb):\n"
        db_handler_text = f"{db_handler_text}{CONFIG['spacing_2']}self.session.close()\n\n"
        return db_handler_text
    

    ### corrigir importar do config
    def db_base_text(self) ->str:
        return 'from sqlalchemy.ext.declarative import declarative_base\n\nBase = declarative_base()'

    def concate_field_type(self, field:dict) -> str:
        if field['additional_parameter'] == None:
            return f"{field['name']}=Column({field['type']})"
        elif field['type'] == "Integer":
            return f"{field['name']}=Column({field['type']}, {field['additional_parameter']})"
        else:
            return f"{field['name']}=Column({field['type']}({field['additional_parameter']}))"


    # create return model __repr__
    def create_return_repr_model(self, fields_name:list) ->str:
        empty_text = ''
        for field_name in fields_name:
            empty_text = empty_text + f'"{field_name}": "{KEY_NAME_LEFT}self.{field_name}{KEY_NAME_RIGHT}",'
        return f"{empty_text[:-1]}"
    

    # create Model Text
    def model_text(self, fields:list, table_name:str)-> None:
        text_model = ''
        fields_temp = []
        text_model = self.decode_dict_values_from_text(dict_infos=SQLALCHEMIST_IMPORTS, base_text=text_model)
        text_model = f'{text_model}{ESPECIAL_IMPORTS["base"]}\n\n'
        text_model = f'{text_model}class {self.convert_snakecase_to_camelcase(text=table_name)}(Base):\n'
        text_model = f"{text_model}{CONFIG['spacing_1']}__tablename__ = '{table_name}'\n"
        for field in fields:
            fields_temp.append(field['name'])
            text_model = f"{text_model}{CONFIG['spacing_1']}{self.concate_field_type(field=field)}\n"
        text_model = f"{text_model}{CONFIG['spacing_1']}created_at=Column(String())\n"
        text_model = f"{text_model}{CONFIG['spacing_1']}updated_at=Column(String())\n"
        text_model = f"{text_model}{CONFIG['spacing_1']}deleted_at=Column(String())\n"
        text_model = f"{text_model}\n\n{CONFIG['spacing_1']}def __repr__(self) -> str:\n"
        text_model = f"{text_model}{CONFIG['spacing_2']}return f'{self.create_return_repr_model(fields_name=fields_temp)}"
        text_model = f'{text_model},"created_at"="{KEY_NAME_LEFT}self.created_at{KEY_NAME_RIGHT}","updated_at" ="{KEY_NAME_LEFT}self.updated_at{KEY_NAME_RIGHT}", "deleted_at" ="{KEY_NAME_LEFT}self.deleted_at{KEY_NAME_RIGHT}"'
        text_model = f"{text_model}'"
        return text_model
    


    # create databasesHandler Text
    def db_handler_text(self, models:list)-> None:
        db_handler_text = f'{ESPECIAL_IMPORTS["db_connection_handler"]}\n'
        for model in models:
            name_camecase = self.convert_snakecase_to_camelcase(text=model['table_name'])
            db_handler_text = f"{db_handler_text}from src.models.{name_camecase} import {name_camecase}\n"
        db_handler_text = f"{db_handler_text}\n"
        db_handler_text = f"{db_handler_text}class DataBasesHandler\n"
        db_handler_text = f"{db_handler_text}\n\n{CONFIG['spacing_1']}def __init__(self) -> None:\n"
        db_handler_text = f"{db_handler_text}\n\n{CONFIG['spacing_2']}self.engine = DBConnectionHandler().get_engine()\n"
        db_handler_text = f"{db_handler_text}\n\n{CONFIG['spacing_1']}def create_datebase(self)->None:\n"
        for model in models:
            name_camecase = self.convert_snakecase_to_camelcase(text=model['table_name'])
            db_handler_text = f"{db_handler_text}\n\n{CONFIG['spacing_2']}{name_camecase}.metadata.create_all(self.engine)\n"
        return db_handler_text

     # create init models
    def init_models_text(self, models:list)-> None:
        init_models_text = ''
        for model in models:
            name_camecase = self.convert_snakecase_to_camelcase(text=model['table_name'])
            init_models_text = f"{init_models_text}from .{name_camecase} import {name_camecase}\n"
        return init_models_text
        
        
    ##### REPOSITORIES
    def result_handle_repositories_text(self) ->str:
        text_result_handle = ''
        text_result_handle = f"{text_result_handle}\n\nclass ResultHandlerRepository():\n"
        # init
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_1']}def __init__(self):\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}self.answer = {KEY_NAME_LEFT}{KEY_NAME_RIGHT}\n"
        # join
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_1']}def __join_data(self, record:dict)->None:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}for key in record:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}self.answer[key].append(record[key])\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}pass\n\n"
        # make_answer
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_1']}def __make_answer_structure(self, data:dict)->None:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}answer = {KEY_NAME_LEFT}{KEY_NAME_RIGHT}\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}keys_data = list(data[0].keys())\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}for key in keys_data:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}answer[key] = []\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}self.answer = answer\n\n"
        # filter answer
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_1']}def __filter_answer_clean_data(self, fields:list)->None:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}temp_answer = self.answer.copy()\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}for key in self.answer:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}if key not in fields:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_4']}temp_answer.pop(key)\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}return temp_answer\n\n"
        #filter data
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_1']}def filter_data(self, data:list, fields:list=None)->list:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}self.__make_answer_structure(data=data)\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}for record in data:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}self.__join_data(record=record) \n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}if fields == None:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}return self.answer\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}elif len(fields) > 0:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}return  self.__filter_answer_clean_data(fields)\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_2']}else:\n"
        text_result_handle = f"{text_result_handle}{CONFIG['spacing_3']}return self.answer\n"
        return text_result_handle


    def get_abbreviation_type(self, type_name:str)-> str:
        if type_name == 'Integer':
            return 'int'
        if type_name == 'Boolean':
            return 'bool'
        if type_name == 'Float':
            return 'float'
        else:
            return 'str'

    
    def create_filter_by_select(self, table_name:str, fields:list) -> str:
        model_text = ''
        for field in fields:
            model_text = model_text + f"{CONFIG['spacing_3']}if {field['name']} != None:\n{CONFIG['spacing_4']}query = query.filter_by({field['name']}={field['name']})\n"
        model_text = model_text + f"{CONFIG['spacing_3']}if order_by is not None:\n{CONFIG['spacing_4']}if order_by[1] == 'asc':\n{CONFIG['spacing_5']}query = query.order_by(getattr({self.convert_snakecase_to_camelcase(table_name)}, order_by[0]))\n"
        model_text = model_text + f"{CONFIG['spacing_4']}elif order_by[1] == 'desc':\n{CONFIG['spacing_5']}query = query.order_by(getattr({self.convert_snakecase_to_camelcase(table_name)}, order_by[0]).desc())\n"
        model_text = model_text + f"{CONFIG['spacing_3']}if limit is not None:\n{CONFIG['spacing_4']}query = query.limit(limit)\n"
        model_text = model_text + f"{CONFIG['spacing_3']}data =  query.all()\n"
        model_text = model_text + f"{CONFIG['spacing_3']}return self.__tratar_return_query(returned_query=data, fields=fields)"
        return model_text


    def create_entry_parameters_select(self, fields:list)-> str:    
        fields_temp = []
        start_str = '(self,'
        for field in fields:
            fields_temp.append(field['name'])
            start_str = f"{start_str} {field['name']}:{self.get_abbreviation_type(field['type'])}=None,"
        return start_str[:-1]

    def create_entry_parameters_insert(self, fields:list)->str:
        fields_temp = []
        start_str = '(self,'
        for field in fields:
            fields_temp.append(field['name'])
            start_str = f"{start_str} {field['name']}:{self.get_abbreviation_type(field['type'])},"
        start_str = f"{start_str[:-1]}):"
        return start_str
    
    def create_condicional_text_update(self, fields:list, table_name:str) ->str:
        model_text = ''
        model_text = f'{model_text}{CONFIG["spacing_3"]}if {table_name}:\n'
        for field in fields:
            model_text = f'{model_text}{CONFIG["spacing_4"]}if {field["name"]}!= None:\n'
            model_text = f'{model_text}{CONFIG["spacing_5"]}{table_name}.{field["name"]} = {field["name"]}\n'
        return model_text

    def repositories_text(self, model:dict) ->str:
        repository_file = ''
        #imports
        repository_file = f'{repository_file}{ESPECIAL_IMPORTS["db_connection_handler"]}\n'
        repository_file = f'{repository_file}{ESPECIAL_IMPORTS["result_handle"]}\n'
        repository_file = f"{repository_file}from src.models.{self.convert_snakecase_to_camelcase(text=model['table_name'])} import {self.convert_snakecase_to_camelcase(text=model['table_name'])}\n"
        repository_file = f'{repository_file}{ESPECIAL_IMPORTS["uuid"]}\n'
        repository_file = f'{repository_file}{ESPECIAL_IMPORTS["json"]}\n'
        repository_file = f'{repository_file}{ESPECIAL_IMPORTS["datetime"]}\n'
        repository_file = f'{repository_file}{SQLALCHEMIST_IMPORTS["sqlalchemy"]}\n\n\n'
        #filter by fields
        repository_file = f'{repository_file}class {self.convert_snakecase_to_camelcase(text=model["table_name"])}(Result_handler_repository):\n'
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def __filter_by_field(self, fields:list, record:dict):\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}new_dictionary = {KEY_NAME_LEFT}key: value for key, value in record.items() if key in fields{KEY_NAME_RIGHT}\n"
        repository_file = f"{repository_file}{CONFIG['spacing_2']}return new_dictionary\n\n"
        # tratar_return_query
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def __tratar_return_query(self, returned_query:object, fields) -> dict:\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}answer = []\n"
        repository_file = f"{repository_file}{CONFIG['spacing_2']}for record in returned_query:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}str_record = str(record)\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}record_str = {KEY_NAME_LEFT}str_record{KEY_NAME_RIGHT}\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}value = json.loads(record_str)\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}if fields  != None:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}value =  self.__filter_by_field(fields=fields, record=value)\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}answer.append(value)\n"
        repository_file = f"{repository_file}{CONFIG['spacing_2']}return answer\n\n"
        # select
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def select_{model["table_name"]} {self.create_entry_parameters_select(fields=model["fields"])}, fields:list=None, limit:int=None, order_by:list=None) -> dict:\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}with DBConnectionHandler() as db_connection:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}db_connection.session.query({self.convert_snakecase_to_camelcase(text=model['table_name'])})\n"
        repository_file = f"{repository_file}{self.create_filter_by_select(table_name=model['table_name'], fields=model['fields'])}\n\n"
        # INSERT
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def insert_{model["table_name"]} {self.create_entry_parameters_insert(fields=model["fields"])}\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}with DBConnectionHandler() as db_connection:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}new_record = {self.convert_snakecase_to_camelcase(text=model['table_name'])}{self.insert_repositories_text(fields=model['fields'])}\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}db_connection.session.add(new_record)\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}db_connection.session.commit()\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}id_saved = new_record.id\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}rerutn = id_saved\n\n"
        # usada para recuperar um registro pelo id
        QUERY_ID = f"{CONFIG['spacing_3']}{model['table_name']} =  db_connection.session.query({self.convert_snakecase_to_camelcase(text=model['table_name'])}).filter_by(id=id).first()\n"
        #update
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def update_{model["table_name"]} {self.create_entry_parameters_select(fields=model["fields"])}) -> bool:\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}with DBConnectionHandler() as db_connection:\n"
        repository_file = f"{repository_file}{QUERY_ID}"
        repository_file = f"{repository_file}{self.create_condicional_text_update(fields=model['fields'], table_name=model['table_name'])}\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}{model['table_name']}.updated_at=datetime.now()\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}db_connection.session.commit()\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}return True\n"
        repository_file = f"{repository_file}{CONFIG['spacing_3']}else:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}return False\n\n"
        #full delete
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def full_delete_{model["table_name"]}(self, id:int) -> bool:\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}with DBConnectionHandler() as db_connection:\n"
        repository_file = f"{repository_file}{QUERY_ID}"
        repository_file = f'{repository_file}{CONFIG["spacing_3"]}if {model["table_name"]}:\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}db_connection.session.delete({model["table_name"]})\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}db_connection.session.commit()\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}return True\n'
        repository_file = f"{repository_file}{CONFIG['spacing_3']}else:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}return False\n\n"
        #soft delete
        repository_file = f'{repository_file}{CONFIG["spacing_1"]}def soft_delete_{model["table_name"]}(self, id:int) -> bool:\n'
        repository_file = f"{repository_file}{CONFIG['spacing_2']}with DBConnectionHandler() as db_connection:\n"
        repository_file = f"{repository_file}{QUERY_ID}"
        repository_file = f'{repository_file}{CONFIG["spacing_3"]}if {model["table_name"]}:\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}{model["table_name"]}.deleted_at = datetime.now()\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}db_connection.session.commit()\n'
        repository_file = f'{repository_file}{CONFIG["spacing_4"]}return True\n'
        repository_file = f"{repository_file}{CONFIG['spacing_3']}else:\n"
        repository_file = f"{repository_file}{CONFIG['spacing_4']}return False\n\n"

        




        return repository_file


        

        '''
                              def insert_perfil_media(self, uuid:str, person_id:int, nickname:str, perfil_media_id:int, url_perfil:str, id_user_perfil:str, email_main:str, date_create_social:str, created_at:str, deleted_at:str, updated_at:str):
        with DBConnectionHandler() as db_connection:
            new_record = PerfilSocialMedia(
            person_id=person_id,
            uuid=uuid4(),
            nickname=nickname,
            perfil_media_id=perfil_media_id,
            url_perfil=url_perfil,
            id_user_perfil=id_user_perfil,
            email_main=email_main,
            date_create_social=date_create_social,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db_connection.session.add(new_record)
        db_connection.session.commit()
        id_saved = new_record.id
        return id_saved

                              
                              '''
        
        
####################################### PAREI AQUI, NA LINHA 31 DO PERSONREPOSITORYES SOCIAL FOLLOWTRACK





        # function __filter_by_field
        
    '''
        
        repository_file.write('\n')
        repository_file.write(CONFIG['spacing_1'] + 'def select_'+ table_name + self.__manipule_entry_parameters(fields=fields))
        repository_file.write('\n')
        repository_file.write(f"{CONFIG['spacing_2']} with DBConnectionHandler() as db_connection:\n{CONFIG['spacing_3']}query = db_connection.session.query({self.manipule_name_file(table_name=table_name)})")
        repository_file.write('\n')
        repository_file.write(self.__create_filter_by_select(fields=fields))
    '''