#===============================================================
# Del directorio apliación, el subdirectorio repositorio, el
# archivo basededatos.py : trae el objeto basededatos 
#===============================================================

from aplicacion.repositorio.basededatos import BaseDeDatos


#===============================================================
# Del directorio aplicación el subdirectorio repositorio, 
# el archivo s3.py : trae el objeto S3
#===============================================================

from aplicacion.repositorio.s3 import S3

#=====================================================================
# DEl directorio aplicacion, el subdirectorio repositorio, 
# el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#======================================================================

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos 

#=========================================================================
# Del directorio aplicación, el subdirectorio modelos,
# el archivo.py : trae el obejto usuario
#=========================================================================

from aplicacion.modelos.usuario  import Usuario
#==========================================================================
# Del directorio aplicacion, el subdirectorio negocios, 
# el archivo manedeinscripciones.py : trae el objeto ManejoDeInscripciones 
#==========================================================================

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones 

#=========================
# Crear el objeto Usuario 
#=========================

usuario = Usuario("Roberto","Jimenez",18)

#========================
# Crear el objeto s3
#========================

repositorioS3 = S3("321321321", "sdf324223", "MiCubeta")

#=============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=============================================================

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#=========================================
# Crear el objeto sistemadearchivos 
#=========================================

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#==============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones 
#==============================================================

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#====================================
# Crear el objeto basededatos 
#====================================

repositorioBaseDeDatos = BaseDeDatos("localhost", "admin","admin123")

#==============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones 
#==============================================================

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

