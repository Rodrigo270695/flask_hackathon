from database import db

class Rol(db.Model):
    
    __tablename__ = 'rol'
    
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(15), nullable=False,unique=True)
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __repr__(self):
        return f'Rol {self.nombre}'
    



