from database import db

class GrupoHorario(db.Model):
    
    __tablename__ = 'grupo_horario'
    
    id_grupo_horario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), nullable=False, unique=True)
    abreviatura = db.Column(db.String(5), nullable=False, unique=True)
    estado = db.Column(db.Boolean, nullable=False, default=True)
    
    def __init__(self, nombre, abreviatura):
        self.nombre = nombre
        self.abreviatura = abreviatura

    def __repr__(self):
        return f"<GrupoHorario(nombre={self.nombre})>"