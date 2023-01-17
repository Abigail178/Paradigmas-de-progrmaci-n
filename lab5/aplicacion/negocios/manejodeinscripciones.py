from aplicacion.modelos.usuario import Usuario 
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#===============================
# Clase storemanager
# NO TIENE VARIABLES !!!
#===============================

class ManejoDeInscripciones:

    #========================================================================
    # Decoradir staticmethod
    # El objetivo sólo tiene la función inscribirUSuario
    # ENVUELVE LA FUNCION SIN LLAMAR VARIABLES LOCALES
    # el objetivo ManejoDeInscripciones es la interface intercambiable
    #=======================================================================
    @staticmethod
    
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
       
        print("------> Guardando usuario .. \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
