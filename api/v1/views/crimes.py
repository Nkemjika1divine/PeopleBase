#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models.crime import Crime

@app_views.route('/crimes', methods=['GET'], strict_slashes=False)
def get_crimes():
    """Route for retrieveing all data in the crime table"""
    from models import storage
    all_crimes = storage.all("Crime").values()
    crimes = []
    for crime in all_crimes:
        crimes.append(crime.to_dict())
    return jsonify(crimes)

