# app/__init__.py
from flask import Flask
from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)

    # Importa e registra os blueprints (rotas)
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)

    return app