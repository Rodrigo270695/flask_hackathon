from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.Semestre import Semestre

class RegisterSemestre(FlaskForm):

    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=10)])
    fecha_inicio = DateField('Fecha de inicio', validators=[DataRequired()])
    fecha_fin = DateField('Fecha de fin', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
    def validar_nombre(self, nombre):
        semestre = Semestre.query.filter_by(nombre=nombre.data).first()
        if semestre:
            raise ValidationError('El semestre ya existe')



