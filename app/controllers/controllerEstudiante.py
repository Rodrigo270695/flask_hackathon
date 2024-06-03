from app.models.Estudiante import Estudiante
from database import db
import traceback

class ControllerEstudiante:
 
    def listar_estudiantes(self):
        try:
            estudiantes = Estudiante.query.order_by(Estudiante.id_estudiante.desc()).all()
            return estudiantes
        except Exception as e:
            return str(e)

    def crear_estudiante(self, nombres, apellidos, email, doc_identidad, numero_celular, codigo, titulo_tesis):
        try:
            estudiante = Estudiante(
                nombres=nombres,
                apellidos=apellidos,
                email=email,
                doc_identidad=doc_identidad,
                numero_celular=numero_celular,
                codigo=codigo,
                titulo_tesis=titulo_tesis,
            )
            db.session.add(estudiante)
            db.session.commit()
            return estudiante
        except Exception as e:
            return str(e)

    def obtener_estudiante(self, id_estudiante):
        try:
            estudiante = Estudiante.query.get(id_estudiante)
            return estudiante
        except Exception as e:
            return None

    def actualizar_estudiante(self, id_estudiante, nombres, apellidos, email, doc_identidad, numero_celular, codigo, titulo_tesis):
        try:
            estudiante = Estudiante.query.get(id_estudiante)
            if estudiante:
                estudiante.nombres = nombres
                estudiante.apellidos = apellidos
                estudiante.email = email
                estudiante.doc_identidad = doc_identidad
                estudiante.numero_celular = numero_celular
                estudiante.codigo = codigo
                estudiante.titulo_tesis = titulo_tesis
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
        
    def cambiar_estado(self, id_estudiante, nuevo_estado):
        try:
            estudiante = Estudiante.query.get(id_estudiante)
            if estudiante:
                estudiante.estado = nuevo_estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
        
    def eliminar_estudiante(self, id_estudiante):
        try:
            estudiante = Estudiante.query.get(id_estudiante)
            if estudiante:
                db.session.delete(estudiante)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False