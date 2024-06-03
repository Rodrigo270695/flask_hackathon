from app.models.Rol import Rol

class ControllerRol:

    def get_roles(self):
        try:
            roles = Rol.query.all()
            return roles
        except Exception as e:
            return str(e)
        


