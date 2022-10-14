#pipenv install flask pymysql flask-bcrypt
#pipenv shell
#python3 server.py

from flask_app import app
from flask_app.controllers import users_controller, grades_controller


if __name__ == "__main__":
    app.run(debug=True)
