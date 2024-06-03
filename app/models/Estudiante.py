from database import db
from sqlalchemy import Column, Integer, String, Boolean

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id_estudiante = Column(Integer, primary_key=True)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    doc_identidad = Column(String(8), nullable=False, unique=True)
    numero_celular = Column(String(9), nullable=False, unique=True)
    codigo = Column(String(10), nullable=False, unique=True)
    titulo_tesis = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True, nullable=False)

    def __init__(self, nombres, apellidos, email, doc_identidad, numero_celular, codigo, titulo_tesis):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.doc_identidad = doc_identidad
        self.numero_celular = numero_celular
        self.codigo = codigo
        self.titulo_tesis = titulo_tesis
    
    def __repr__(self):
        return f"<Estudiante(id_estudiante={self.id_estudiante}, nombres={self.nombres}, apellidos={self.apellidos}, email={self.email}, estado={self.estado})>"