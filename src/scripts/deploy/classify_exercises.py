#Autora : Lucía Núñez Calvo
import argparse
import statistics
import pickle
import numpy as np
from tslearn.metrics import dtw_subsequence_path

def part(array,p,x_y):
    """
    Esta función descompone cada una de las posiciones que se le pasa
    
    Parámetros
    ----------
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

def main():
    parser = argparse.ArgumentParser()
    #Creamos el primer argumento que recibirá un pickle
    parser.add_argument("pk1")
    args = parser.parse_args()

    pk_exercise=openPickle(args.pk1)
    
   
    classifyExercise(pk_exercise)

if __name__ == '__main__':
    main()
