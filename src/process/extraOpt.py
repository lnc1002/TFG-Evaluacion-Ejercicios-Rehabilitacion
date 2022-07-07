# -*- coding: utf-8 -*-

from fishubuia import Interfaz
import pickle 
import numpy as np

ia = Interfaz()

def opt(key, value, output="/"):
    pos, esq, ang, posT  = ia.obtenerPosicion(value, 2)
    with open('/mnt/data/posiciones.pickle', 'ab') as f:
        pickle.dump(posT, f)
    return key, esq

def ang(key, value, output="/"):
    pos, esq, ang  = ia.obtenerPosicion(value, 2)
    return ang
