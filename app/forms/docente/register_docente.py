from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError, Email
from app.models.Docente import Docente


class RegisterDocente(FlaskForm):
    docente_id = HiddenField()
    nombres = StringField('Nombres', validators=[DataRequired(), Length(max=50)])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    doc_identidad = StringField('Documento de Identidad', validators=[DataRequired(), Length(max=8)])
    numero_celular = StringField('Número de Celular', validators=[DataRequired(), Length(max=9)])
    id_rol = IntegerField('ID Rol', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_email(self, email):
        if self.docente_id.data:
            docente = Docente.query.filter(Docente.id_docente != self.docente_id.data, Docente.email == email.data).first()
        else:
            docente = Docente.query.filter_by(email=email.data).first()
        if docente:
            raise ValidationError('El email ya existe.')

    def validate_doc_identidad(self, doc_identidad):
        if self.docente_id.data:
            docente = Docente.query.filter(Docente.id_docente != self.docente_id.data, Docente.doc_identidad == doc_identidad.data).first()
        else:
            docente = Docente.query.filter_by(doc_identidad=doc_identidad.data).first()
        if docente:
            raise ValidationError('El documento de identidad ya existe.')

    def validate_numero_celular(self, numero_celular):
        if self.docente_id.data:
            docente = Docente.query.filter(Docente.id_docente != self.docente_id.data, Docente.numero_celular == numero_celular.data).first()
        else:
            docente = Docente.query.filter_by(numero_celular=numero_celular.data).first()
        if docente:
            raise ValidationError('El nmero de celular ya existe.')

