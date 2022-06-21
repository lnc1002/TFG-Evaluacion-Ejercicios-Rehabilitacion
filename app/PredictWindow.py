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
from moviepy.video.io.VideoFileClip import VideoFileClip

class PredictWindow():
    """
    Clase que proporciona la predicción
    """

    def __init__(self, window):
        self.window = window 

    def cutVideo(self,index,start,end):
        ffmpeg_extract_subclip(self.window.playlistFull[index], start, end,targetname="Recorte2.mp4")
        #Guardar losvídeos recortados en una carpeta y con un nombre concreto
        self.window.showVideo3.load("Recorte2.mp4")
        self.window.showVideo3.play()

    def showVideo(self):
        """
        Lo primero que se tendrá que comprobar es si 
        """
        #1) Recortarlo 2) Guardarlo en una variable 3) Mostrarlo con el load + play
        #Los vídeos están a 30fps

        if self.window.togglebutton.config('text')[-1] == 'OFF':
            #Modo (OFF)
            index=self.window.selectVideo2
            clip = VideoFileClip(self.window.playlistFull[index])
            start_time=int(self.window.textFrameBegin.get())*int(clip.duration) / 960
            end_time=int(self.window.textFrameEnd.get())*int(clip.duration) / 960
            
            
            print(int(self.window.textFrameBegin.get()),int(self.window.textFrameEnd.get()), start_time, end_time, clip.duration, clip.fps) 
            #Con clip.duration sabemos la duración del video y con clip.fps los fps que tiene el video. 
            #Ahora nos queda saber cuandos frames genera y hacer la regla de 3
            #Esto creo que me crea otro víde en targetname
            
            self.cutVideo(index,start_time,end_time)

        else:
            #Modo (ON)
            #Recortar según los frames obtenidos con el programa
            index=self.window.selectVideo2
            if index == 0:
                clip = VideoFileClip(self.window.playlistSpecific[0])
                print(clip.duration, clip.fps)
                self.cutVideo(index,2,12)

            elif index == 1:
                self.cutVideo(index,12,22)
            elif index == 2:
                self.cutVideo(index,2,12)
            elif index == 3:
                self.cutVideo(index,12,22)
