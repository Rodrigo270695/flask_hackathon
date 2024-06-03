from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.Semestre import Semestre

class RegisterSemestre(FlaskForm):
    semestre_id = HiddenField()  
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=10)])
    fecha_inicio = DateField('Fecha de inicio', validators=[DataRequired()])
    fecha_fin = DateField('Fecha de fin', validators=[DataRequired()])
    submit = SubmitField('Registrar')
    
    def validate_nombre(self, nombre):
        if self.semestre_id.data: 
            semestre = Semestre.query.filter(Semestre.id_semestre != self.semestre_id.data, Semestre.nombre == nombre.data).first()
        else:
            semestre = Semestre.query.filter_by(nombre=nombre.data).first()
        if semestre:
            raise ValidationError('El semestre ya existe')

