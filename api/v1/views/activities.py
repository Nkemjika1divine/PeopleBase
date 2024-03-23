#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.activity import Activity

@app_views.route('/activities', methods=['GET'], strict_slashes=False)
def get_activities():
    from models import storage
    all_activities = storage.all("Activity").values()
    activities = []
    for activity in all_activities:
        activities.append(activity.to_dict())
    return jsonify(activities)




@app_views.route('/user-activity/<username>', methods=['GET'], strict_slashes=False)
def get_specific_activity(username):
    """Route for retrieving crimes using a phone number or an email"""
    from models import storage
    activities = []
    data = storage.get_user_activity(username).values()
    if not data:
        abort(404)
    else:
        for activity in data:
            activities.append(activity.to_dict())
    
    return jsonify(activities)



@app_views.route('/activities', methods=['POST'], strict_slashes=False)
def post_activity():
    """route for adding a new user to the server"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    if "user_id" not in request.get_json():
        abort(400, description="Missing 'user_id'")
    if "information_accessed" not in request.get_json():
        abort(400, description="Missing 'information_accessed'")
    
    parsed_data = request.get_json()

    foreign_key_check = storage.check_activity_foreign_key(parsed_data["user_id"])
    if foreign_key_check == False:
        abort(400, description="user_id is not associated with any primary key")

    activity = Activity(**parsed_data)
    activity.save()
    return make_response(jsonify(activity.to_dict()), 201)




@app_views.route('/activity/<username>/<activity_id>', methods=['DELETE'], strict_slashes=False)
def delete_activity(username, activity_id):
    """This deletes an activity"""
    from models import storage
    
    activity = storage.get_activity(username, activity_id)
    if not activity:
        abort(404)
    
    storage.delete(activity)
    storage.save()
    return make_response(jsonify({}), 200)