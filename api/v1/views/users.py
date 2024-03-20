#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Route for retrieveing all data in the user table"""
    from models import storage
    all_users = storage.all("User").values()
    users = []
    for user in all_users:
        users.append(user.to_dict())
    return jsonify(users)



@app_views.route('/user/<username>', methods=['GET'], strict_slashes=False)
def get_specific_user(username):
    """Route for retrieveing a data in the user table by username"""
    from models import storage
    user = storage.get_user(username)
    if not user:
        abort(404)
    return jsonify(user.to_dict())