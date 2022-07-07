#Autora: Lucía Núñez Calvo

import argparse
import statistics
import pickle
import numpy as np
import time
from tslearn.metrics import dtw_subsequence_path

def openPickle(file):
    """
    Función encargada de extraer los datos almacenados en el fichero con extensión .pickle 
    y almacenarlos en una variable.
    
    Parámetros
    ---------
    file : fichero con extensión .pickle del que se van a extraer los datos.
    
    Salida
    ---------
    matriz con las posiciones correspondientes a la secuencia de ejercicios.
    """
    data_list = []
    with open(file, "rb") as f:
        while True:
            try:
                current_id=pickle.load(f)
                data_list.append(current_id)
            except EOFError:
                break
    #print(data_list)
    return data_list

def del_cero(array):
    """
    Función que descarta los valores igual a cero.
    
    Parámetros de entrada
    ---------------------
    array= Secuencia de la que se pretende eliminar los ceros
    
    Salida
    ------
    Retorna la misma secuencia de entrada pero con los valores igual a cero descartados.
    """
    p1=[]
    
    for p in array:
        if p != 0.0:
            p1.append(p)
    return np.array(p1)

def cutFrames(array_puntos_largo):
    """
    Función encargada de recortar los frames y quedarse con aproximadamente el 67% de ellos.
    
    Parámetros
    ----------
    puntos : vector que contiene la secuencia de posiciones
    
    Salida
    ----------
    Vector que contiene aproximadamente el 67% posiciones 
    """
    array_puntos=[]
    guardar=0
    for ang in array_puntos_largo:
        guardar=guardar+1
        if guardar==3:
            guardar=0
        else:
            array_puntos.append(ang)
    return array_puntos

def findFrames(pk_short,pk_long):
    """
    Función encarga de de encontrar la posición de inicio y final de la correspondiente secuencia
    concreta dentro de la secuencia que contiene múltiples ejercicios.
    
    Parámetros
    ----------
    pk_short : Secuencia concreta que se analizará
    pk_long : Secuencia larga en la que se buscará la secuencia concreta

    Salida
    ------
    Retorna una secuencia con los valores correspondientes al inicio y final de la secuencia sin realizar la equivalencia
    """

    path, dist = dtw_subsequence_path(pk_short,pk_long)

    path=np.array(path)
    a_ast = path[0, 1]
    b_ast = path[-1, 1]

    #Para realizar pruebas, descomentar estas salidas por pantalla
    #print("El Ejercicio comienza en el frame =",a_ast)
    #print("El Ejercicio finaliza en el frame =",b_ast)

    return [a_ast,b_ast]

def equiv(seq_real, seq_cut, seq_obt):
    """
    Función que realiza la equivalencia y trasnforma el resultado para poder seer utilizado en la aplicación de escritorio.
    (Visicar cuaderno C10_Resultados_finales.ipynb para más información sobre este cálculo)

    Parámetros
    ----------
    seq_real : Longitud de la secuencia larga pasada como parámetro.
    seq_cut : Longitud de la secuencia larga redimensionada y recortada.
    seq_obt : Vector que contiene las secuencias de inicio y final previas a la equivalencia.

    Salida
    -------
    Muestra por pantalla las secuencias de inicio y final equivalentes y con una tasa de error.
    ------
    """
    #print(seq_real, seq_cut, seq_obt)
    seq_without_error_a=(seq_obt[0]*seq_real)/seq_cut
    seq_without_error_b=(seq_obt[1]*seq_real)/seq_cut
    #print(seq_without_error_a,seq_without_error_b)
    error_a=0.1*seq_without_error_a
    error_b=0.1*seq_without_error_b

    print("El Ejercicio comienza en el frame =",seq_without_error_a-error_a)
    print("El Ejercicio finaliza en el frame =",seq_without_error_b+error_b)

    #return [seq_obt[0]-error_a, seq_obt[1]+error_b]

def part(array,p,x_y):
    """
    Esta función descompone cada una de las posiciones que se le pasa
    
    Parámetros
    ----------
    array : posición de un esqueleto
    p : parte del cuerpo de la que se quiere obtener el resultado
    x_y : Dimensión sobre la que se quiere obtener el resultado
    """
    r=[]
    for i in range(len(array)-1):
        r.append(array[i][p][x_y]) 
    return r

def classifyExercise(pk_short):
    """
    Función encargada de clasificar el ejercicio según las extremidades que estén en movimiento

    Parámetros
    ----------
    pk_short : Secuencia de ejercicios completos. Es muy importante que esta secuencia no se encuentre redimensionada
    """
    #Sacaremos las posiciones de las rodillas y los codos

    #Ángulo rodilla izquierda
    sigma_rodilla_iz=np.array(part(pk_short,18,0)).flatten().std()
    #Angulo rodilla derecha 
    sigma_rodilla_d=np.array(part(pk_short,19,0)).flatten().std()
    #Angulo codo izquierdo
    sigma_codo_iz=np.array(part(pk_short,6,0)).flatten().std()
    #Angulo codo derecho
    sigma_codo_d=np.array(part(pk_short,7,0)).flatten().std()

    if sigma_rodilla_iz>sigma_codo_iz and sigma_rodilla_iz>sigma_codo_d  and sigma_rodilla_d>sigma_codo_iz and sigma_rodilla_d>sigma_codo_d:
        print("Ejercicio sobre las extremidades INFERIORES")
    elif sigma_rodilla_iz<sigma_codo_iz and sigma_rodilla_iz<sigma_codo_d  and sigma_rodilla_d<sigma_codo_iz and sigma_rodilla_d<sigma_codo_d:
        print("Ejercicio sobre las extremidades SUPERIORES")
    else:
        print("No se puede determinar el tipo de ejercicio")


def main():
    parser = argparse.ArgumentParser()
    #Creamos el primer argumento que recibirá un pickle
    parser.add_argument("pk1")
    #Creamos el segundo argumento que recibirá un pickle
    parser.add_argument("pk2")
    args = parser.parse_args()

    #Se carga el archivo
    pk_short=openPickle(args.pk1)
    pk_long=openPickle(args.pk2)

    #Se almacenan los frames totales del vídeo
    frames_2d=len(pk_long)

    #Se eleminan los ceros 
    pk_short1=del_cero(np.array(pk_short).flatten())
    pk_long1=del_cero(np.array(pk_long).flatten())

    #Elimina los nulos
    pk_long1 = pk_long1[~np.isnan(pk_long1)]
    
    #Recorta los frames
    pk_short2=cutFrames(pk_short)
    pk_long2=cutFrames(pk_long1)
    
    #Se almacenan los frames totales recortados
    frames_1d=len(pk_long2)

    pk_short3=np.array(pk_short2).flatten()
    pk_long3=np.array(pk_long2).flatten()

    #Se mide el tiempo de ejecución
    inicio = time.time()
    #Se procede a la búsqueda de la secuencia
    result=findFrames(pk_short3,pk_long3)

    #Se realiza la equivalencia
    equiv(frames_2d,frames_1d,result)
    
    fin = time.time()

    print("\nEl tiempo de ejecución ha sido de: ",fin-inicio," segundos")
    #Finalmente se clasifica el ejercicio
    classifyExercise(pk_short)

if __name__ == '__main__':
    main()
