from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from app.controllers.controllerUsuario import ControllerUsuario
from app.forms.usuario.register_usuario import RegisterUsuario

controller_usuario = ControllerUsuario()
usuario_routes = Blueprint('usuario_routes', __name__)


@usuario_routes.route('/listar_usuarios', methods=['GET'])
def listar_usuarios():
    form = RegisterUsuario()
    usuarios = controller_usuario.listar_usuarios()
    return render_template('Usuario/usuarios.html', usuarios=usuarios, form=form)


@usuario_routes.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    form = RegisterUsuario(request.form)
    if form.validate_on_submit():
        controller_usuario.crear_usuario(form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data, form.id_rol.data)
        flash('Usuario registrado correctamente', 'success')
        return jsonify(success=True)
    else:
        flash('Error al registrar el usuario', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@usuario_routes.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = controller_usuario.obtener_usuario(id)
    if usuario:
        return jsonify({
            'id_usuario': usuario.id_usuario,
            'nombres': usuario.nombres,
            'apellidos': usuario.apellidos,
            'email': usuario.email,
            'clave_acceso': usuario.clave_acceso,
            'doc_identidad': usuario.doc_identidad,
            'numero_celular': usuario.numero_celular,
            'id_rol': usuario.id_rol
        })
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404


@usuario_routes.route('/editar_usuario/<int:id>', methods=['POST'])
def editar_usuario(id):
    usuario = controller_usuario.obtener_usuario(id)
    form = RegisterUsuario(request.form, usuario_id=usuario.id_usuario if usuario else None)
    if form.validate_on_submit():
        if controller_usuario.actualizar_usuario(id, form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data, form.id_rol.data):
            flash('Usuario actualizado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al actualizar el usuario', 'error')
            return jsonify(success=False, message="Error al actualizar el usuario")
    else:
        flash('Error al actualizar el usuario', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)



@usuario_routes.route('/cambiar_estado_usuario/<int:id>', methods=['POST'])
def cambiar_estado_usuario(id):
    try:
        usuario = controller_usuario.obtener_usuario(id)
        if usuario:
            nuevo_estado = not usuario.estado 
            if controller_usuario.cambiar_estado(id, nuevo_estado):
                flash('Cambio de estado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al cambiar el estado', 'error')
                return jsonify(success=False, message="Error al cambiar el estado")
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        flash('Error al cambiar el estado', 'error')
        return jsonify(success=False, message=str(e)), 500