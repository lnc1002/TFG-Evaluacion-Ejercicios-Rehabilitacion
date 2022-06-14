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
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

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
        #1) Recortarlo 2) Guardarlo en una variable 3) Mostrarlo con el load + play
        #Los vídeos están a 30fps

        if self.window.togglebutton.config('text')[-1] == 'OFF':
            #Modo (OFF)
            index=self.window.selectVideo2
            start_time=30/int(self.window.textFrameBegin.get())
            end_time=30/int(self.window.textFrameEnd.get())
            print(start_time, end_time)
            #Esto creo que me crea otro víde en targetname
            ffmpeg_extract_subclip(self.window.playlistFull[index], start_time, end_time,targetname="Recorte1.mp4")
            self.window.showVideo3.load("Recorte.mp4")
            self.window.showVideo3.play()
        #else:
            #Modo (ON)
            #Recortar según los frames obtenidos con el programa
