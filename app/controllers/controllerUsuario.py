from app.models.Usuario import Usuario
from database import db
from werkzeug.security import generate_password_hash
import traceback

class ControllerUsuario:
    
    def listar_usuarios(self):
        try:
            usuarios = Usuario.query.order_by(Usuario.id_usuario.desc()).all()
            return usuarios
        except Exception as e:
            return str(e)
        
        
    def crear_usuario(self, nombres, apellidos, email, doc_identidad, numero_celular, id_rol):
        try:
            hashed_password = generate_password_hash(doc_identidad)
            usuario = Usuario(nombres, apellidos, email, hashed_password, doc_identidad, numero_celular, id_rol)
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            return str(e)

        
    def obtener_usuario(self, id):
        try:
            usuario = Usuario.query.get(id)
            return usuario
        except Exception as e:
            return str(e)

    def actualizar_usuario(self, id, nombres, apellidos, email, doc_identidad, numero_celular, id_rol):
        try:
            usuario = Usuario.query.get(id)
            if usuario:
                usuario.nombres = nombres
                usuario.apellidos = apellidos
                usuario.email = email
                usuario.doc_identidad = doc_identidad
                usuario.numero_celular = numero_celular
                usuario.id_rol = id_rol
                db.session.commit()
                return True
            return False
        except Exception as e:
            traceback.print_exc()
            return False
        
    def cambiar_estado(self, id, nuevo_estado):
        try:
            usuario = Usuario.query.get(id)
            if usuario:
                usuario.estado = nuevo_estado
                db.session.commit()
                return True
            return False
        except Exception as e:
            return False        




