#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models.activity import Activity
from models.crime import Crime
from models.dataset import Dataset
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def return_status():
    return jsonify({"status": "ok"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def return_statistics():
    from models import storage
    classes = ["Activity", "Crime", "Dataset", "User"]
    class_names = ["activity", "crime", "dataset", "user"]

    data = {}
    for i in range(len(classes)):
        data[class_names[i]] = storage.count(classes[i])
    
    return jsonify(data)