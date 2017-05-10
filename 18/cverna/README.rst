docker run -v `pwd`:/git:Z -p 5000:5000 -it python-flask /bin/bash
export FLASK_APP=`pwd`/devapp.py
export FLASK_DEBUG=1
flask run
