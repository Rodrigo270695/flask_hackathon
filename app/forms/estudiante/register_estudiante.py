from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.Estudiante import Estudiante

class RegisterEstudiante(FlaskForm):
    estudiante_id = HiddenField()
    nombres = StringField('Nombres', validators=[DataRequired(), Length(max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    doc_identidad = StringField('Documento de Identidad', validators=[DataRequired(), Length(max=8)])
    numero_celular = StringField('Número de Celular', validators=[DataRequired(), Length(max=9)])
    codigo = StringField('Código', validators=[DataRequired(), Length(max=10)])
    titulo_tesis = StringField('Título de Tesis', validators=[DataRequired(), Length(max=255)])
    estado = BooleanField('Estado', default=True)
    submit = SubmitField('Registrar')

    def validate_email(self, email):
        if self.estudiante_id.data:
            estudiante = Estudiante.query.filter(Estudiante.id_estudiante != self.estudiante_id.data, Estudiante.email == email.data).first()
        else:
            estudiante = Estudiante.query.filter_by(email=email.data).first()
        if estudiante:
            raise ValidationError('El email ya existe.')

    def validate_doc_identidad(self, doc_identidad):
        if self.estudiante_id.data:
            estudiante = Estudiante.query.filter(Estudiante.id_estudiante != self.estudiante_id.data, Estudiante.doc_identidad == doc_identidad.data).first()
        else:
            estudiante = Estudiante.query.filter_by(doc_identidad=doc_identidad.data).first()
        if estudiante:
            raise ValidationError('El documento de identidad ya existe.')

    def validate_numero_celular(self, numero_celular):
        if self.estudiante_id.data:
            estudiante = Estudiante.query.filter(Estudiante.id_estudiante != self.estudiante_id.data, Estudiante.numero_celular == numero_celular.data).first()
        else:
            estudiante = Estudiante.query.filter_by(numero_celular=numero_celular.data).first()
        if estudiante:
            raise ValidationError('El número de celular ya existe.')
        
    def validate_codigo(self, codigo):
        if self.estudiante_id.data:
            estudiante = Estudiante.query.filter(Estudiante.id_estudiante != self.estudiante_id.data, Estudiante.codigo == codigo.data).first()
        else:
            estudiante = Estudiante.query.filter_by(codigo=codigo.data).first()
        if estudiante:
            raise ValidationError('El código ya existe.')
