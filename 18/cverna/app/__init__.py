from flask import Flask
from app.main import main
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')
    app.register_blueprint(main)
    return app

app = create_app()
db = SQLAlchemy(app)
db.create_all()
