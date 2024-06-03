from app.models.Docente import Docente
from database import db
from werkzeug.security import generate_password_hash
import traceback

class ControllerDocente:
    
    def listar_docentes(self):
        try:
            docentes = Docente.query.order_by(Docente.id_docente.desc()).all()
            return docentes
        except Exception as e:
            return str(e)
    
    def crear_docente(self, nombres, apellidos, email, doc_identidad, numero_celular, id_rol):
        try:
            hashed_password = generate_password_hash(doc_identidad)
            docente = Docente(nombres, apellidos, email, hashed_password, doc_identidad, numero_celular, id_rol)
            db.session.add(docente)
            db.session.commit()
            return docente
        except Exception as e:
            return str(e)
    
    def obtener_docente(self, id):
        try:
            docente = Docente.query.get(id)
            return docente
        except Exception as e:
            return str(e)

    def actualizar_docente(self, id, nombres, apellidos, email, doc_identidad, numero_celular):
        try:
            docente = Docente.query.get(id)
            if docente:
                docente.nombres = nombres
                docente.apellidos = apellidos
                docente.email = email
                docente.doc_identidad = doc_identidad
                docente.numero_celular = numero_celular
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
        
    def cambiar_estado(self, id, nuevo_estado):
        try:
            docente = Docente.query.get(id)
            if docente:
                docente.estado = nuevo_estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            return False        




