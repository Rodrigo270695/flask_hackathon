from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.GrupoHorario import GrupoHorario

class RegisterGrupoHorario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=10)])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(), Length(max=5)])
    submit = SubmitField('Registrar')

    def validate_nombre(self, nombre):
        grupo = GrupoHorario.query.filter_by(nombre=nombre.data).first()
        if grupo:
            raise ValidationError('El grupo horario ya existe')