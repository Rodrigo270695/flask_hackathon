from flask import Flask
from database import init_app
from check_db_connection import check_database_connection
import os


app = Flask(__name__)
app.config['SECRET_KEY_APP'] = os.getenv('FLASK_SECRET_KEY_APP')
app.secret_key = app.config['SECRET_KEY_APP']
SECRET_KEY = app.secret_key

init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#comprobar la conexión
check_database_connection()


if __name__ == '__main__':
    app.run(debug=True)
















