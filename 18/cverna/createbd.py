from app import create_app
from app.models import db

create_app().app_context().push()
db.create_all()
