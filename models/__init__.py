#!/usr/bin/python3
import os
from dotenv import load_dotenv
from models.engine.filestorage import FileStorage
from models.engine.dbstorage import DBStorage

load_dotenv()

if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
    storage = FileStorage()
    storage.reload()
elif os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
    storage = DBStorage()
    storage.reload()