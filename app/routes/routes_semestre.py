from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
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
    form = RegisterSemestre(request.form)
    if form.validate_on_submit():
        controller_semestre.crear_semestre(form.nombre.data, form.fecha_inicio.data, form.fecha_fin.data)
        flash('Semestre registrado correctamente', 'success')
        return jsonify(success=True)
    else:
        flash('Error al registrar el semestre', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@semestre_routes.route('/semestre/<int:id>', methods=['GET'])
def get_semestre(id):
    semestre = controller_semestre.obtener_semestre(id)
    if semestre:
        return jsonify({
            'id_semestre': semestre.id_semestre,
            'nombre': semestre.nombre,
            'fecha_inicio': str(semestre.fecha_inicio),
            'fecha_fin': str(semestre.fecha_fin)
        })
    else:
        return jsonify({'error': 'Semestre no encontrado'}), 404

@semestre_routes.route('/editar_semestre/<int:id>', methods=['POST'])
def editar_semestre(id):
    form = RegisterSemestre(request.form)
    if form.validate_on_submit():
        if controller_semestre.actualizar_semestre(id, form.nombre.data, form.fecha_inicio.data, form.fecha_fin.data):
            flash('Semestre actualizado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al actualizar el semestre', 'error')
            return jsonify(success=False, message="Error al actualizar el semestre")
    else:
        flash('Error al actualizar el semestre', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@semestre_routes.route('/cambiar_estado_semestre/<int:id>', methods=['POST'])
def cambiar_estado_semestre(id):
    try:
        semestre = controller_semestre.obtener_semestre(id)
        if semestre:
            nuevo_estado = not semestre.estado  # Cambia el estado actual
            if controller_semestre.cambiar_estado(id, nuevo_estado):
                flash('Cambio de estado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al cambiar el estado', 'error')
                return jsonify(success=False, message="Error al cambiar el estado")
        else:
            return jsonify({'error': 'Semestre no encontrado'}), 404
    except Exception as e:
        flash('Error al cambiar el estado', 'error')
        return jsonify(success=False, message=str(e)), 500

