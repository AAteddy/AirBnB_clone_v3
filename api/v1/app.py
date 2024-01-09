#!/usr/bin/python3
""" Flask Application thet integrates with AirBnB static"""
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
from models import storage
import os


# Global Flask Application Variable: app
app = Flask(__name__)

# Cross-Origin Resource Sharing
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# app_views BluePrint defined in api.v1.views with url prefix
app.register_blueprint(app_views, url_prefix="/api/v1")


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exp):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(404)
def handles_404(exp):
    """Handles 404 errors."""
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def handles_400(exp):
    """Handles 400 errors."""
    message = exp.description
    return message, 400


#@app.teardown_appcontext
#def close(ctx):
#    storage.close()



# flask server environmental setup
if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_PORT"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000


if __name__ == "__main__":
    """Main Flask App."""
    # start Flask app
    app.run(host=host, port=port, threaded=True)
