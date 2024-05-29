from app.models.Semestre import Semestre
from database import db

class ControllerSemestre:

    
    def listar_semestres(self):
        try:
            semestres = Semestre.query.all()
            return semestres
        except Exception as e:
            return str(e)

        
    def crear_semestre(self, nombre, fecha_inicio, fecha_fin):
        try:
            semestre = Semestre(nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            db.session.add(semestre)
            db.session.commit()

            return semestre
        except Exception as e:
            return str(e)

        
        
