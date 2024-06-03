from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from app.models.Usuario import Usuario
from app.controllers.controllerRol import ControllerRol

controller_rol = ControllerRol()

class RegisterUsuario(FlaskForm):
    usuario_id = HiddenField() 
    nombres = StringField('Nombres', validators=[DataRequired(), Length(max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    doc_identidad = StringField('Documento de Identidad', validators=[DataRequired(), Length(max=8)])
    numero_celular = StringField('Número de Celular', validators=[DataRequired(), Length(max=9)])
    id_rol = SelectField('Rol', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(RegisterUsuario, self).__init__(*args, **kwargs)
        self.id_rol.choices = [(rol.id_rol, rol.nombre) for rol in controller_rol.get_roles()]

    def validate_email(self, email):
        if self.usuario_id.data:
            usuario = Usuario.query.filter(Usuario.id_usuario != self.usuario_id.data, Usuario.email == email.data).first()
        else:
            usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('El email ya existe.')

    def validate_doc_identidad(self, doc_identidad):
        if self.usuario_id.data:
            usuario = Usuario.query.filter(Usuario.id_usuario != self.usuario_id.data, Usuario.doc_identidad == doc_identidad.data).first()
        else:
            usuario = Usuario.query.filter_by(doc_identidad=doc_identidad.data).first()
        if usuario:
            raise ValidationError('El documento de identidad ya existe.')

    def validate_numero_celular(self, numero_celular):
        if self.usuario_id.data:
            usuario = Usuario.query.filter(Usuario.id_usuario != self.usuario_id.data, Usuario.numero_celular == numero_celular.data).first()
        else:
            usuario = Usuario.query.filter_by(numero_celular=numero_celular.data).first()
        if usuario:
            raise ValidationError('El número de celular ya existe.')
    