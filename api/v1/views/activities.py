#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify
from models.activity import Activity

@app_views.route('/activities', methods=['GET'], strict_slashes=False)
def get_activities():
    from models import storage
    all_activities = storage.all("Activity").values()
    activities = []
    for activity in all_activities:
        activities.append(activity.to_dict())
    return jsonify(activities)