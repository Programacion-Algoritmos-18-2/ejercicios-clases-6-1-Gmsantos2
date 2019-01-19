from paquete_archivos.miarchivo import MiArchivo  #importacion de clases a utilizar 
from modelado.ArregloBinario import *

m = MiArchivo()
lista = m.obtener_informacion()
entero = int(input("Ingrese el numero que desea encontrar: "))  # clave de b�squeda
#posicion= 0 # ubicaci�n de la clave de b�squeda en el arreglo  
lista = [l.split(",") for l in lista] #la primera lista toma como valores  todo elemento   y separa por una ,
data = []

for  a in lista: # ciclo donde recorremos la lista
    for i in a:  #ciclo donde recomrremos  la posicion a de la lista 
        data.append(int(i)) # a la lista vacia se le agrega los valores transformados a 
    
print(sorted(data)) #presentamos al lista ordenada 



        
arregloBusqueda = ArregloBinario(data)  #creamos un objeto donde le mandamos los datos para la busqueda
#print(arregloBusqueda);
        
posicion = arregloBusqueda.busquedaBinaria(entero) #le mandamos el entero con el que se va a comparar cada elemento de la lista
if (posicion == -1):        #condicionales  donde se presenta si esque  se encontro el entero y e que posicion y en caso de no encontrar presenta mensaje
    print("El entero %d no se encontro.\n" %(entero))
else:
    print("El entero %d se encontro en la posicion %d.\n" %(entero,posicion))