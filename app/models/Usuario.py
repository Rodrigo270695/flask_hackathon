from database import db

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    clave_acceso = db.Column(db.String(255), nullable=False)
    doc_identidad = db.Column(db.String(8), nullable=False, unique=True)
    numero_celular = db.Column(db.String(9), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))


    def __init__(self, nombres, apellidos, email, clave_acceso, doc_identidad, numero_celular, id_rol):
        
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.clave_acceso = clave_acceso
        self.doc_identidad = doc_identidad
        self.numero_celular = numero_celular
        self.id_rol = id_rol
    
    def __repr__(self):
        return f'Usuario {self.nombres} {self.apellidos}'

