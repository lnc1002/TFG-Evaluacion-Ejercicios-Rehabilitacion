# -*- coding: utf-8 -*-

from fishubuia import Interfaz
import pickle 
import numpy as np

ia = Interfaz()

def opt(key, value, output="/"):
      # Esta función es configurada manualmente por el programador
    pos, esq, ang, posT  = ia.obtenerPosicion(value, 2)
    with open('posiciones.pickle', 'ab') as f:
        pickle.dump(posT, f)
    with open("angulos.txt", "a") as f:
        f.writelines(str(ang))
    # Hacemos un pickle de la posición
    pk.dump(pos, os.path.join(output,"pos_"+str(key))+".pickle")
    # pk.dump(pos, "data.pickle")
    return key, esq

def ang(key, value, output="/"):
    pos, esq, ang  = ia.obtenerPosicion(value, 2)
    return ang
