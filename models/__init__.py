#!/usr/bin/python3
import os
from dotenv import load_dotenv

load_dotenv()

if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "file":
    from models.engine.filestorage import FileStorage
    storage = FileStorage()
    storage.reload()
if os.environ.get("PEOPLEBASE_STORAGE_TYPE") == "db":
    from models.engine.dbstorage import DBStorage
    storage = DBStorage()
    storage.reload()