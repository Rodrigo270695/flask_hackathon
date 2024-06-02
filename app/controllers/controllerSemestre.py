from app.models.Semestre import Semestre
from database import db
import traceback

class ControllerSemestre:

    def listar_semestres(self):
        try:
            semestres = Semestre.query.order_by(Semestre.id_semestre.desc()).all()
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

    def obtener_semestre(self, id):
        try:
            semestre = Semestre.query.get(id)
            return semestre
        except Exception as e:
            return None

    def actualizar_semestre(self, id, nombre, fecha_inicio, fecha_fin):
        try:
            semestre = Semestre.query.get(id)
            if semestre:
                semestre.nombre = nombre
                semestre.fecha_inicio = fecha_inicio
                semestre.fecha_fin = fecha_fin
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
        
    def cambiar_estado(self, id, nuevo_estado):
        print(id, nuevo_estado)
        try:
            semestre = Semestre.query.get(id)
            if semestre:
                semestre.estado = nuevo_estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False

