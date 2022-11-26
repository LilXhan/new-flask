from flask import Flask
from flask_bootstrap import Bootstrap
from .routes.personajes import personaje_router

def create_app():
    app = Flask(__name__)
    
    Bootstrap(app)

    app.register_blueprint(personaje_router)

    return app