#!/usr/bin/python3

class FileStorage:
    __file_path = "filestorage.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects