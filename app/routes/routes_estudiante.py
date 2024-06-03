from flask import Blueprint, render_template, flash, jsonify, request
from app.controllers.controllerEstudiante import ControllerEstudiante
from app.forms.estudiante.register_estudiante import RegisterEstudiante

controller_estudiante = ControllerEstudiante()
estudiante_routes = Blueprint('estudiante_routes', __name__)

@estudiante_routes.route('/listar_estudiantes', methods=['GET'])
def listar_estudiantes():
    form = RegisterEstudiante()
    estudiantes = controller_estudiante.listar_estudiantes()
    return render_template('Estudiante/index.html', estudiantes=estudiantes, form=form)

@estudiante_routes.route('/registrar_estudiante', methods=['POST'])
def registrar_estudiante():
    form = RegisterEstudiante(request.form)
    if form.validate_on_submit():
        controller_estudiante.crear_estudiante(form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data, form.codigo.data, form.titulo_tesis.data)
        flash('Estudiante registrado correctamente', 'success')
        return jsonify(success=True)
    else:
        flash('Error al registrar el estudiante', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@estudiante_routes.route('/estudiante/<int:id>', methods=['GET'])
def get_estudiante(id):
    estudiante = controller_estudiante.obtener_estudiante(id)
    if estudiante:
        return jsonify({
            'id_estudiante': estudiante.id_estudiante,
            'nombres': estudiante.nombres,
            'apellidos': estudiante.apellidos,
            'email': estudiante.email,
            'doc_identidad': estudiante.doc_identidad,
            'numero_celular': estudiante.numero_celular,
            'codigo': estudiante.codigo,
            'titulo_tesis': estudiante.titulo_tesis,
            'estado': estudiante.estado
        })
    else:
        return jsonify({'error': 'Estudiante no encontrado'}), 404

@estudiante_routes.route('/editar_estudiante/<int:id>', methods=['POST'])
def editar_estudiante(id):
    estudiante = controller_estudiante.obtener_estudiante(id)
    form = RegisterEstudiante(request.form, estudiante_id=estudiante.id_estudiante if estudiante else None)
    if form.validate_on_submit():
        if controller_estudiante.actualizar_estudiante(id, form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data, form.codigo.data, form.titulo_tesis.data):
            flash('Estudiante actualizado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al actualizar el estudiante', 'error')
            return jsonify(success=False, message="Error al actualizar el estudiante")
    else:
        flash('Error al actualizar el estudiante', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@estudiante_routes.route('/cambiar_estado_estudiante/<int:id>', methods=['POST'])
def cambiar_estado_estudiante(id):
    try:
        estudiante = controller_estudiante.obtener_estudiante(id)
        if estudiante:
            nuevo_estado = not estudiante.estado 
            if controller_estudiante.cambiar_estado(id, nuevo_estado):
                flash('Cambio de estado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al cambiar el estado', 'error')
                return jsonify(success=False, message="Error al cambiar el estado")
        else:
            return jsonify({'error': 'Estudiante no encontrado'}), 404
    except Exception as e:
        flash('Error al cambiar el estado', 'error')
        return jsonify(success=False, message=str(e)), 500

@estudiante_routes.route('/eliminar_estudiante/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    try:
        estudiante = controller_estudiante.obtener_estudiante(id)
        if estudiante:
            if controller_estudiante.eliminar_estudiante(id):
                flash('Estudiante eliminado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al eliminar el estudiante', 'error')
                return jsonify(success=False, message="Error al eliminar el estudiante")
        else:
            return jsonify({'error': 'Estudiante no encontrado'}), 404
    except Exception as e:
        flash('Error al eliminar el estudiante', 'error')
        return jsonify(success=False, message=str(e)), 500
