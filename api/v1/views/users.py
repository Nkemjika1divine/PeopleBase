#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
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





@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """route for adding a new user to the server"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    if "username" not in request.get_json():
        abort(400, description="Missing 'username'")
    if "gender" not in request.get_json():
        abort(400, description="Missing 'gender'")
    if "email" not in request.get_json():
        abort(400, description="Missing 'email'")
    if "address" not in request.get_json():
        abort(400, description="Missing 'address'")
    if "phone_number" not in request.get_json():
        abort(400, description="Missing 'phone_number'")
    if "password" not in request.get_json():
        abort(400, description="Missing 'password'")
    
    parsed_data = request.get_json()

    email_check = storage.check_user_duplicity(parsed_data["email"])
    if email_check == 1:
        abort(400, description="email already exists")
    
    username_check = storage.check_user_duplicity(parsed_data["username"])
    if username_check == 2:
        abort(400, description="username taken")

    phone_number_check = storage.check_user_duplicity(parsed_data["phone_number"])
    if phone_number_check == 3:
        abort(400, description="phone number already exists")

    user = User(**parsed_data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)




@app_views.route('/users/<username>', methods=['PUT'], strict_slashes=False)
def put_user(username):
    """This updates a user"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    
    keys_to_ignore = ["id", "time_created", "time_updated"]

    user = storage.get_user(username)
    if not user:
        abort(404)
    
    parsed_data = request.get_json()
    for key, value in parsed_data.items():
        if key == "username":
            username_check = storage.check_user_duplicity(value)
            if username_check == 2:
                abort(400, description="username taken")
        elif key == "email":
            email_check = storage.check_user_duplicity(value)
            if email_check == 1:
                abort(400, description="email already exists")
        elif key == "phone_number":
            phone_number_check = storage.check_user_duplicity(parsed_data["phone_number"])
            if phone_number_check == 3:
                abort(400, description="phone number already exists")

    for key, value in parsed_data.items():
        if key not in keys_to_ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)





@app_views.route('/user/<username>', methods=['DELETE'], strict_slashes=False)
def delete_user(username):
    """This deletes a user"""
    from models import storage
    
    user = storage.get_user(username)
    if not user:
        abort(404)
    
    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)