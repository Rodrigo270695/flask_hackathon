from flask import Flask,render_template
from database import init_app
from check_db_connection import check_database_connection
from app.routes.routes_semestre import semestre_routes
import os
from app.models.Semestre import Semestre

app = Flask(__name__, static_folder='assets')


app.config['SECRET_KEY_APP'] = os.getenv('FLASK_SECRET_KEY_APP')
app.secret_key = app.config['SECRET_KEY_APP']
SECRET_KEY = app.secret_key


init_app(app)
check_database_connection()

@app.route("/")
def hello_world():
    return render_template('blank.html')

app.register_blueprint(semestre_routes, url_prefix='/semestre')

if __name__ == '__main__':
    app.run(debug=True)
















