from flask import Blueprint, render_template, flash, jsonify, request
from app.controllers.controllerDocente import ControllerDocente
from app.forms.docente.register_docente import RegisterDocente

controller_docente = ControllerDocente()
docente_routes = Blueprint('docente_routes', __name__)


@docente_routes.route('/listar_docentes', methods=['GET'])
def listar_docentes():
    form = RegisterDocente()
    docentes = controller_docente.listar_docentes()
    return render_template('Docente/docentes.html', docentes=docentes, form=form)


@docente_routes.route('/registrar_docente', methods=['POST'])
def registrar_docente():
    form = RegisterDocente(request.form)
    if form.validate_on_submit():
        controller_docente.crear_docente(form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data, form.id_rol.data)
        flash('Docente registrado correctamente', 'success')
        return jsonify(success=True)
    else:
        flash('Error al registrar el docente', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)

@docente_routes.route('/docente/<int:id>', methods=['GET'])
def get_docente(id):
    docente = controller_docente.obtener_docente(id)
    if docente:
        return jsonify({
            'id_docente': docente.id_docente,
            'nombres': docente.nombres,
            'apellidos': docente.apellidos,
            'email': docente.email,
            'clave_acceso': docente.clave_acceso,
            'doc_identidad': docente.doc_identidad,
            'numero_celular': docente.numero_celular,
        
        })
    else:
        return jsonify({'error': 'Docente no encontrado'}), 404


@docente_routes.route('/editar_docente/<int:id>', methods=['POST'])
def editar_docente(id):
    docente = controller_docente.obtener_docente(id)
    form = RegisterDocente(request.form, docente_id=docente.id_docente if docente else None)
    if form.validate_on_submit():
        if controller_docente.actualizar_docente(id, form.nombres.data, form.apellidos.data, form.email.data, form.doc_identidad.data, form.numero_celular.data):
            flash('Docente actualizado correctamente', 'success')
            return jsonify(success=True)
        else:
            flash('Error al actualizar el docente', 'error')
            return jsonify(success=False, message="Error al actualizar el docente")
    else:
        flash('Error al actualizar el docente', 'error')
        errors = {field: error[0] for field, error in form.errors.items()}
        return jsonify(success=False, errors=errors)



@docente_routes.route('/cambiar_estado_docente/<int:id>', methods=['POST'])
def cambiar_estado_docente(id):
    try:
        docente = controller_docente.obtener_docente(id)
        if docente:
            nuevo_estado = not docente.estado 
            if controller_docente.cambiar_estado(id, nuevo_estado):
                flash('Cambio de estado correctamente', 'success')
                return jsonify(success=True)
            else:
                flash('Error al cambiar el estado', 'error')
                return jsonify(success=False, message="Error al cambiar el estado")
        else:
            return jsonify({'error': 'Docente no encontrado'}), 404
    except Exception as e:
        flash('Error al cambiar el estado', 'error')
        return jsonify(success=False, message=str(e)), 500