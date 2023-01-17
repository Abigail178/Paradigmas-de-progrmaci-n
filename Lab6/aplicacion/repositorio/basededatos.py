from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#====================================================
# Para llenar la interface hay que heredar la clase
#====================================================

class BaseDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __init__(mi, host:str, user:str, password:str):
        mi.__host = host
        mi.__user = user
        mi.__password = password 
        
    def abrir(mi) -> None:
        print(f"Abriendo la conexión de la base de datos: {mi.__host}:{mi.__user}@{mi.__password}")

    def guardar(mi, usuario:Usuario) -> None:
        userElements= {"nombre": usuario.getNombre(),
                       "apellidos": usuario.getApellidos(),
                       "edad":usuario.getEdad()}

        print(f"Guardando el usuario en la base de datos {usuario.getNombre()}\n")

        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}','{userElements['apellidos']}', {userElements['edad']})")

    def cerrar (mi) -> None:
        print("Cerrando la conexión")

