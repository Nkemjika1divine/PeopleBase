#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify
from models.dataset import Dataset

@app_views.route('/dataset', methods=['GET'], strict_slashes=False)
def get_dataset():
    """Route for retrieveing all data in the Dataset table"""
    from models import storage
    all_dataset = storage.all("Dataset").values()
    data = []
    for dataset in all_dataset:
        data.append(dataset.to_dict())
    return jsonify(data)



@app_views.route('/dataset/<phone_or_email>', methods=['GET'], strict_slashes=False)
def get_specific_dataset(phone_or_email):
    """Route for retrieving a data in Dataset using a phone number or an email"""
    from models import storage
    dataset = storage.get_dataset(phone_or_email)
    if not dataset:
        abort(404)
    
    return jsonify(dataset.to_dict())
