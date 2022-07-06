import argparse
import statistics
import pickle
import numpy as np
import time
from tslearn.metrics import dtw_subsequence_path

def cutFrames(array_puntos_largo):
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
    Esta función retornará el frame de inicio y final del ejecercicio concreto dentro de la secuencia larga
    """
    #Lo primero será convertir los pickle en array
    #long_seq = np.array(pk_long).flatten()
    #short_seq = np.array(pk_short).flatten()

    #Eliminamos los valores nulos de la secuencia larga
    #long_seq = long_seq[~np.isnan(long_seq)]

    #Comprobar más adelante cuanto hay que recortar los frames

    path, dist = dtw_subsequence_path(short_seq,long_seq)

    path=np.array(path)
    a_ast = path[0, 1]
    b_ast = path[-1, 1]


    print("El Ejercicio comienza en el frame =",a_ast)
    print("El Ejercicio finaliza en el frame =",b_ast)


def parte(array,p,x_y):
    """
    Esta función descompone cada una de las posiciones que se le pasa
    Entrada
        array: posición de un esqueleto
        p: parte del cuerpo de la que se quiere obtener el resultado
        x_y: Dimensión sobre la que se quiere obtener el resultado
    """
    r=[]
    for i in range(len(array)-1):
        r.append(array[i][p][x_y]) 
    return r

def classifyExercise(pk_short):
    #Sacaremos las posiciones de las rodillas y los codos

    #Ángulo rodilla izquierda
    sigma_rodilla_iz=np.array(parte(pk_short,18,0)).flatten().std()
    #Angulo rodilla derecha 
    sigma_rodilla_d=np.array(parte(pk_short,19,0)).flatten().std()
    #Angulo codo izquierdo
    sigma_codo_iz=np.array(parte(pk_short,6,0)).flatten().std()
    #Angulo codo derecho
    sigma_codo_d=np.array(parte(pk_short,7,0)).flatten().std()

    if sigma_rodilla_iz>sigma_codo_iz and sigma_rodilla_iz>sigma_codo_d  and sigma_rodilla_d>sigma_codo_iz and sigma_rodilla_d>sigma_codo_d:
        print("Ejercicio sobre las extremidades INFERIORES")
    elif sigma_rodilla_iz<sigma_codo_iz and sigma_rodilla_iz<sigma_codo_d  and sigma_rodilla_d<sigma_codo_iz and sigma_rodilla_d<sigma_codo_d:
        print("Ejercicio sobre las extremidades SUPERIORES")
    else:
        print("No se puede determinar el tipo de ejercicio")


def openPickle(file):
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

    #Se sacan los frames totales del vídeo
    frames_2d=len(pk_long)

    #Se eleminan los ceros 
    pk_short1=del_cero(np.array(pk_short).flatten())
    pk_long1=del_cero(np.array(pk_long).flatten())
    print(len(pk_long1))

    #Elimina los nulos
    pk_long = pk_long[~np.isnan(pk_long)]
    
    #Recorta los frames
    pk_short2=cutFrames(pk_short1)
    pk_long2=cutFrames(pk_long1)

    #Se guarda la longitud larga ¿?
    #frames_1d=len(pk_long)
    print(pk_long2)
    
    inicio = time.time()
    #Se procede a la búsqueda de la secuencia
    findFrames(pk_short2,pk_long2)
    fin = time.time()

    print("time",fin-inicio)
    #Finalmente se clasifica el ejercicio
    #classifyExercise(pk_short)

if __name__ == '__main__':
    main()

