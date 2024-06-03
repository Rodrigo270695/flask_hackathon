from flask import Flask,render_template
from database import init_app
from check_db_connection import check_database_connection
from app.routes.routes_semestre import semestre_routes
from app.routes.routes_usuario import usuario_routes
from app.routes.routes_docente import docente_routes
from app.routes.routes_estudiante import estudiante_routes
from app.routes.routes_grupo_horario import grupo_horario_routes
import os


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
app.register_blueprint(usuario_routes, url_prefix='/usuario')
app.register_blueprint(docente_routes, url_prefix='/docente')
app.register_blueprint(estudiante_routes, url_prefix='/estudiante')
app.register_blueprint(grupo_horario_routes, url_prefix='/grupo_horario')

if __name__ == '__main__':
    app.run(debug=True)
















