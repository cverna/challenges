from flask import Flask


from app.views.stories import stories


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')

    from app.models import db
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    app.register_blueprint(stories)
    return app
