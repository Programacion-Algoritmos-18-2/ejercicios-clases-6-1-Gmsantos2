import codecs
import sys
from modelado.ArregloBinario import *

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/datos.txt","r")


    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()

