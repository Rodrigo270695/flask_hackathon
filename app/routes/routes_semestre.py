from flask import Blueprint, render_template
from app.controllers.controllerSemestre import ControllerSemestre
from app.forms.semestre.register_semestre import RegisterSemestre

controller_semestre = ControllerSemestre()

semestre_routes = Blueprint('semestre_routes', __name__)

@semestre_routes.route('/listar_semestres', methods=['GET'])
def listar_semestres():
    semestres = controller_semestre.listar_semestres()
    return render_template('Semestre/semestres.html', semestres=semestres)


@semestre_routes.route('/registrar_semestre', methods=['GET'])
def registrar_semestre():
    return render_template('Semestre/modal_registrar_semestre.html')