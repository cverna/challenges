from flask import Blueprint, render_template, request, jsonify
from app.models import db, PythonStory


stories = Blueprint('stories', __name__, template_folder='templates')


@stories.route('/', methods=['GET'])
def index():
   return render_template('index.html')


@stories.route('/add', methods=['POST'])
def add_story():
    hn_story = request.get_json()
    story = PythonStory(title=hn_story['title'],
                        url=hn_story['url'],
                        score=hn_story['score'])

    db.session.add(story)
    db.session.commit()
    response = {'success': True}
    return jsonify(response), 200
