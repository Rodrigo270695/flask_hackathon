from app.models.Semestre import Semestre
import traceback

class ControllerSemestre:
    
    def listar_semestres(self):
        try:
            semestres = Semestre.query.all()
            return semestres
        except Exception as e:
            return str(e)