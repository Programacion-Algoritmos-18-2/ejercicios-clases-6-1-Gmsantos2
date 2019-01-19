class ArregloBinario(object):
    """docstring for ArregloBinario"""
    def __init__(self,datos):  #innit con variables que recibe
        
        self.datos = sorted(datos)

    def agregarDatos(self, datos):  #metodo conde recibe los datos y los ordena en caso de que no  vengan ordenados
        self.datos = sorted(datos)

    

    def busquedaBinaria(self,elementoBusqueda):  
        inferior = 0      #declaracion de variables locales 
        superior = len(self.datos) - 1 
        medio = int((inferior + superior + 1) / 2)
        ubicacion = -1
 

        while ((inferior <= superior) and (ubicacion == -1)):

            if (elementoBusqueda == self.datos[medio]):
                ubicacion = medio # la ubicaci�n es el elemento medio actual
             # el elemento medio es demasiado alto
            else:
                if (elementoBusqueda < self.datos[medio]):
                    superior = medio - 1 # elimina la mitad superior
                else:
            
                    inferior = medio + 1 # elimina la mitad inferior
            
            medio = int((inferior + superior + 1) / 2) # recalcula el elemento medio
            #print("medio ... %d" %(medio))
         
        return ubicacion
     #fin del m�todo busquedaBinaria

    def __str__():   #str
        temporal = "";

       
        for elemento in self.datos :
            temporal = ("%s %d" % (temporal, elemento))
        
        

        return temporal

    