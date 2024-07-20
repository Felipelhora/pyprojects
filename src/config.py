import platform
import os


def bar_system()-> str:
    if platform.system() == 'Windows':
        return '/'
    if platform.system() == 'Linux':
        return '/'

BAR = bar_system()
KEY_NAME_LEFT = '{'
KEY_NAME_RIGHT = '}'


CONFIG =    {
                    "local_path" : os.getcwd(),
                    "spacing_1" : f"{' ' * 4}",
                    "spacing_2" : f"{' ' * 8}",
                    "spacing_3" : f"{' ' * 12}",
                    "spacing_4" : f"{' ' * 16}",
                    "spacing_5" : f"{' ' * 20}",
                    "spacing_6" : f"{' ' * 24}",
                    #"models_text_imports": "from sqlalchemy import Column, String, Integer, DateTime\nfrom sqlalchemy.orm import relationship\nfrom src.models.db_base import BASE\nimport ast\n\n",
                    "common_folders" : ['src', 'resources','temp', 'tests', 'docs', f'src{BAR}controllers', f'src{BAR}services', f'src{BAR}utils'],
                    "mvc_paths": [f'src{BAR}views', f'src{BAR}models', f'src{BAR}repositories'],
                    "rest_simple_paths": [f'src{BAR}routes', f'src{BAR}midwares'],
                    "rest_paths": [f'src{BAR}routes', f'src{BAR}midwares', f'src{BAR}models', f'src{BAR}repositories']
            }

GENERAL_IMPORTS =   {
                        "os" : "import os",
                        "platform" : "import platform",
                        "decouple": "from decouple import config"
                    }

FLASK_IMPORTS =     {
                        "flask": "from flask import Flask",
                        "flask_uploads": "from flask_uploads import UploadSet, configure_uploads, IMAGES",
                    }

SQLALCHEMIST_IMPORTS =  {
                            "sqlalchemy": "from sqlalchemy import create_engine, Column, String, Integer, DateTime, func",
                            "sqlalchemy.orm": "from sqlalchemy.orm import relationship, sessionmaker",
                            "db_config": "from src.config import DB_CONFIG"
                        }

ESPECIAL_IMPORTS =  {
                        "base" : "from src.models.db_base import Base",
                        "db_connection_handler":  "from src.models.DBConnectionHandler import DBConnectionHandler",
                        "result_handle" : "from src.repositories.ResultHandlerRepository import ResultHandlerRepository",
                        "uuid": "from uuid import uuid4",
                        "json": "import json",
                        "datetime" : "from datetime import datetime"

                    }
