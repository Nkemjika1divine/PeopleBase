#!/usr/bin/python3
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
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





@app_views.route('/dataset', methods=['POST'], strict_slashes=False)
def post_dataset():
    """route for adding a new dataset to the server"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    if "first_name" not in request.get_json():
        abort(400, description="Missing 'first_name'")
    if "last_name" not in request.get_json():
        abort(400, description="Missing 'last_name'")
    if "date_of_birth" not in request.get_json():
        abort(400, description="Missing 'date_of_birth'")
    if "gender" not in request.get_json():
        abort(400, description="Missing 'gender'")
    if "address" not in request.get_json():
        abort(400, description="Missing 'address'")
    if "city" not in request.get_json():
        abort(400, description="Missing 'city'")
    if "state" not in request.get_json():
        abort(400, description="Missing 'state'")
    if "country" not in request.get_json():
        abort(400, description="Missing 'country'")
    if "phone_number" not in request.get_json():
        abort(400, description="Missing 'phone_number'")
    if "email" not in request.get_json():
        abort(400, description="Missing 'email'")
    if "nationality" not in request.get_json():
        abort(400, description="Missing 'nationality'")
    if "occupation" not in request.get_json():
        abort(400, description="Missing 'occupation'")
    if "education_level" not in request.get_json():
        abort(400, description="Missing 'education_level'")
    if "marital_status" not in request.get_json():
        abort(400, description="Missing 'marital_status'")
    # middle_name was skipped because it can be null. The rest however, cannot be null
    
    parsed_data = request.get_json()

    email_check = storage.check_dataset_duplicity(parsed_data["email"])
    if email_check == 1:
        abort(400, description="email already exists")

    phone_number_check = storage.check_dataset_duplicity(parsed_data["phone_number"])
    if phone_number_check == 2:
        abort(400, description="phone number already exists")

    dataset = Dataset(**parsed_data)
    dataset.save()
    return make_response(jsonify(dataset.to_dict()), 201)






@app_views.route('/dataset/<phone_or_email>', methods=['PUT'], strict_slashes=False)
def put_dataset(phone_or_email):
    """This updates a dataset"""
    from models import storage
    if not request.get_json():
        abort(400, description="Not a JSON format")
    
    keys_to_ignore = ["id", "time_created", "time_updated"]

    dataset = storage.get_dataset(phone_or_email)
    if not dataset:
        abort(404)
    
    parsed_data = request.get_json()
    for key, value in parsed_data.items():
        if key == "email":
            email_check = storage.check_dataset_duplicity(value)
            if email_check == 1:
                abort(400, description="email already exists")
        elif key == "phone_number":
            phone_number_check = storage.check_dataset_duplicity(parsed_data["phone_number"])
            if phone_number_check == 2:
                abort(400, description="phone number already exists")

    for key, value in parsed_data.items():
        if key not in keys_to_ignore:
            setattr(dataset, key, value)
    storage.save()
    return make_response(jsonify(dataset.to_dict()), 200)






@app_views.route('/dataset/<phone_or_email>', methods=['DELETE'], strict_slashes=False)
def delete_dataset(phone_or_email):
    """This deletes a dataset"""
    from models import storage
    
    dataset = storage.get_dataset(phone_or_email)
    if not dataset:
        abort(404)
    
    storage.delete(dataset)
    storage.save()
    return make_response(jsonify({}), 200)