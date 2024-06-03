from app.models.GrupoHorario import GrupoHorario
from database import db
import traceback

class ControllerGrupoHorario:

    def listar_grupos_horarios(self):
        try:
            grupos = GrupoHorario.query.order_by(GrupoHorario.id_grupo_horario.desc()).all()
            return grupos
        except Exception as e:
            return str(e)

    def crear_grupo_horario(self, nombre, abreviatura):
        try:
            grupo = GrupoHorario(nombre=nombre, abreviatura=abreviatura)
            db.session.add(grupo)
            db.session.commit()
            return grupo
        except Exception as e:
            return str(e)

    def obtener_grupo_horario(self, id): 
        try:
            grupo = GrupoHorario.query.get(id)
            return grupo
        except Exception as e:
            return None

    def actualizar_grupo_horario(self, id, nombre, abreviatura):
        try:
            grupo = GrupoHorario.query.get(id)
            if grupo:
                grupo.nombre = nombre
                grupo.abreviatura = abreviatura
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False

    def cambiar_estado(self, id, nuevo_estado):
        try:
            grupo = GrupoHorario.query.get(id)
            if grupo:
                grupo.estado = nuevo_estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False
    
    def eliminar_grupo_horario(self, id):
        try:
            grupo = GrupoHorario.query.get(id)
            if grupo:
                db.session.delete(grupo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False