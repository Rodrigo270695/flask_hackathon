from flask import Blueprint, render_template, redirect, url_for,flash,jsonify
from app.controllers.controllerSemestre import ControllerSemestre
from app.forms.semestre.register_semestre import RegisterSemestre


controller_semestre = ControllerSemestre()
semestre_routes = Blueprint('semestre_routes', __name__)

@semestre_routes.route('/listar_semestres', methods=['GET'])
def listar_semestres():
    form = RegisterSemestre()
    semestres = controller_semestre.listar_semestres()
    return render_template('Semestre/semestres.html', semestres=semestres, form=form)


@semestre_routes.route('/registrar_semestre', methods=['POST'])
def registrar_semestre():

    form = RegisterSemestre()

    if form.validate_on_submit():
        controller_semestre.crear_semestre(form.nombre.data, form.fecha_inicio.data, form.fecha_fin.data)
        flash('Semestre registrado correctamente!', 'success')
        return redirect(url_for('semestre_routes.listar_semestres'))
    else:
        flash('Error al registrar el semestre', 'error')
        return render_template('Semestre/semestres.html', form=form, error=True) 



        
        


    
