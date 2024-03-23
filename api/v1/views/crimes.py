#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
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




@app_views.route('/dataset-crime/<phone_or_email>', methods=['GET'], strict_slashes=False)
def get_specific_crime(phone_or_email):
    """Route for retrieving crimes using a phone number or an email"""
    from models import storage
    crimes = []
    data = storage.get_dataset_crime(phone_or_email).values()
    if not data:
        abort(404)
    else:
        for crime in data:
            crimes.append(crime.to_dict())
    
    return jsonify(crimes)





@app_views.route('/crimes', methods=['POST'], strict_slashes=False)
def post_crime():
    """route for adding a new user to the server"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    if "criminal_id" not in request.get_json():
        abort(400, description="Missing 'criminal_id'")
    if "crime_committed" not in request.get_json():
        abort(400, description="Missing 'crime_committed'")
    if "punishment" not in request.get_json():
        abort(400, description="Missing 'punishment'")
    if "duration_in_months" not in request.get_json():
        abort(400, description="Missing 'duration_in_months'")
    if "duration_starts" not in request.get_json():
        abort(400, description="Missing 'duration_starts'")
    
    parsed_data = request.get_json()

    foreign_key_check = storage.check_crime_foreign_key(parsed_data["criminal_id"])
    if foreign_key_check == False:
        abort(400, description="criminal_id is not associated with any primary key")

    crime = Crime(**parsed_data)
    crime.save()
    return make_response(jsonify(crime.to_dict()), 201)







@app_views.route('/crime/<phone_or_email>/<crime_id>', methods=['PUT'], strict_slashes=False)
def put_crime(phone_or_email, crime_id):
    """This updates a crime"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    
    keys_to_ignore = ["id", "time_created", "time_updated"]

    crime = storage.get_crime(phone_or_email, crime_id)
    if not crime:
        abort(404)
    
    parsed_data = request.get_json()

    for key, value in parsed_data.items():
        if key not in keys_to_ignore:
            setattr(crime, key, value)
    storage.save()
    return make_response(jsonify(crime.to_dict()), 200)






@app_views.route('/crime/<phone_or_email>/<crime_id>', methods=['DELETE'], strict_slashes=False)
def delete_crime(phone_or_email, crime_id):
    """This deletes a crime"""
    from models import storage
    
    crime = storage.get_crime(phone_or_email, crime_id)
    if not crime:
        abort(404)
    
    storage.delete(crime)
    storage.save()
    return make_response(jsonify({}), 200)
    