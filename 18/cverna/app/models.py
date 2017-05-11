from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class PythonStory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    url = db.Column(db.String(100))
    score = db.Column(db.Integer)

    def __init__(self, title, url, score):
        self.title = title
        self.url = url
        self.score = score
