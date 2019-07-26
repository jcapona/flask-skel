import os
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

from app.config import get_config
from app.models import db


def create_app():
    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(get_config(env))

    # Use json error messages
    for code in default_exceptions.keys():
        app.register_error_handler(code, create_json_error)

    # Register db to the app
    db.init_app(app)

    return app

def create_json_error(e):
    code = (e.code if isinstance(e, HTTPException) else 500)
    err = str(e)
    return jsonify({'error': err}), code
