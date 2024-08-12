from flask import Flask
from dotenv import load_dotenv
import os


def create_app():
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    app = Flask(__name__)

    # Configuración básica de Flask
    app.config.from_pyfile("../config.py")

    # Registro de las rutas
    from .routes import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
