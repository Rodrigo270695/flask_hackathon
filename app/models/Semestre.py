from database import db

class Semestre(db.Model):
    
    __tablename__ = 'semestre'
    
    id_semestre = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), nullable=False, unique=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    
    def __init__(self, nombre, fecha_inicio, fecha_fin):


        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __repr__(self):
        return f"<Semestre(nombre={self.nombre})>"   
    