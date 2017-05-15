docker run -v `pwd`:/git:Z -p 5000:5000 -it python-flask /bin/bash
source set_env.sh
flask run
