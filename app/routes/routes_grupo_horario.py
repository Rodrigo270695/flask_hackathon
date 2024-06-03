from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from app.controllers.controllerGrupoHorario import ControllerGrupoHorario
from app.forms.grupohorario.register_grupo_horario import RegisterGrupoHorario

controller_grupo_horario = ControllerGrupoHorario()
grupo_horario_routes = Blueprint('grupo_horario_routes', __name__)

@grupo_horario_routes.route('/listar_grupos_horarios', methods=['GET'])
def listar_grupos_horarios():
    form = RegisterGrupoHorario()
    grupos = controller_grupo_horario.listar_grupos_horarios()
    return render_template('GrupoHorario/index.html', grupos=grupos, form=form)

@grupo_horario_routes.route('/registrar_grupo_horario', methods=['POST'])
def registrar_grupo_horario():
    form = RegisterGrupoHorario(request.form)
    if form.validate_on_submit():
        controller_grupo_horario.crear_grupo_horario(form.nombre.data, form.abreviatura.data)
        flash('Grupo horario registrado correctamente', 'success')
        return jsonify(success=True)
    else:
        flash('Error al registrar el grupo horario', 'error') 
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@grupo_horario_routes.route('/grupo_horario/<int:id>', methods=['GET'])
def get_grupo_horario(id):
    grupo = controller_grupo_horario.obtener_grupo_horario(id)
    if grupo:
        return jsonify({
            'id_grupo_horario': grupo.id_grupo_horario,
            'nombre': grupo.nombre,
            'abreviatura': grupo.abreviatura
        })
    else:
        return jsonify({'error': 'Grupo horario no encontrado'}), 404

@grupo_horario_routes.route('/editar_grupo_horario/<int:id>', methods=['POST'])
def editar_grupo_horario(id):
    form = RegisterGrupoHorario(request.form)
    if form.validate_on_submit():
        if controller_grupo_horario.actualizar_grupo_horario(id, form.nombre.data, form.abreviatura.data):
            flash('Grupo horario actualizado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al actualizar el grupo horario', 'error')
            return jsonify(success=False, message="Error al actualizar el grupo horario")
    else:
        flash('Error al actualizar el grupo horario', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@grupo_horario_routes.route('/cambiar_estado_grupo_horario/<int:id>', methods=['POST'])
def cambiar_estado_grupo_horario(id):
    try:
        grupo = controller_grupo_horario.obtener_grupo_horario(id)
        if grupo:
            nuevo_estado = not grupo.estado  # Cambia el estado actual
            if controller_grupo_horario.cambiar_estado(id, nuevo_estado):
                flash('Cambio de estado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al cambiar el estado', 'error')
                return jsonify(success=False, message="Error al cambiar el estado")
        else:
            return jsonify({'error': 'Grupo horario no encontrado'}), 404
    except Exception as e:
        flash('Error al cambiar el estado', 'error')
        return jsonify(success=False, message=str(e)), 500

@grupo_horario_routes.route('/eliminar_grupo_horario/<int:id>', methods=['POST'])
def eliminar_grupo_horario(id):
    try:
        if controller_grupo_horario.eliminar_grupo_horario(id):
            flash('Grupo horario eliminado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al eliminar el grupo horario', 'error')
            return jsonify(success=False, message="Error al eliminar el grupo horario")
    except Exception as e:
        flash('Error al eliminar el grupo horario', 'error')
        return jsonify(success=False, message=str(e)), 500

