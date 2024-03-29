#!/usr/bin/python3
from flask import Flask, make_response, jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """Closes storage"""
    from models import storage
    storage.close()


@app.errorhandler(404)
def return_404(error):
    """Handles 404 error"""
    return make_response(jsonify({"error 404": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)