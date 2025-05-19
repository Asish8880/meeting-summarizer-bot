import os
from flask import Flask
from .routes import main
from .database import init_db

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
        static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    )
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.register_blueprint(main)
    init_db()
    return app
