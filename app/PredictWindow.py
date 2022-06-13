"""
Se le llama cuando se presiona el boón de recortar
Bloquear el botón si no se cumplen las condiciones
Modo Ejemplo = Recortar según los pickle cargados
    Len(pickle)=nº de frames
    sacar los segundos totales del vídeoç
    si len(pickle) -->  x segundos
       frame incio --> x segundo
       frame final --> x segundo

Modo NO Ejemplo = recortar según los frames indicados
¿Hacer un botón guardar?
"""

class PredictWindow():
    """
    Clase que proporciona la predicción
    """

    def __init__(self, window):
        self.window = window 

    #def cutVideo(self):

    def showVideo(self):
        """
        Lo primero que se tendrá que comprobar es si 
        """
        #Se sacal los vídeos de las casillas show
        video1 = self.window.showVideo1 #Analizar este parámetro current_duration
        print("algo")
        print(self.window.selectVideo1) #self.window.playlistSpecific[index]
        video2 = self.window.showVideo1
        #if self.window.togglebutton.config('text')[-1] == 'ON':
            #Modo ejemplo (ON)
        #else:
            #Modo demo (OFF)
