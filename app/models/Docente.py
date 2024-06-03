from database import db

class Docente(db.Model):
    
    __tablename__ = 'docente'
    
    id_docente = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'), nullable=False)
    nombres = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    clave_acceso = db.Column(db.String(255), nullable=False)
    doc_identidad = db.Column(db.String(8), nullable=False)
    numero_celular = db.Column(db.String(9), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    
    rol = db.relationship('Rol', backref='docente', lazy=True)
    
    
    def __init__(self,  nombres, apellidos, email, clave_acceso, doc_identidad, numero_celular,id_rol):
        
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.clave_acceso = clave_acceso
        self.doc_identidad = doc_identidad
        self.numero_celular = numero_celular
        self.id_rol = id_rol

    def __repr__(self):
        return f'Docente({self.id_docente}, {self.id_rol}, {self.nombres}, {self.apellidos}, {self.email}, {self.doc_identidad}, {self.numero_celular}, {self.estado})'



