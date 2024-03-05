#!/usr/bin/python3
def search(line=None):
    from models import storage

    if line:
        similar_objects = {}