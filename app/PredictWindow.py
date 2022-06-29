"""
Created on Wed Jun x 2022

@author: Lucía Núñez
"""
import tkinter

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip

class PredictWindow():
    """
    Clase que proporciona el resultado por el cual ha sido creada la aplicación, el vídeo recortado.
    Contiene métodos que permiten realizar la tarea requerida.

    authora: Lucía Núñez
    
    Atributos
    ----------
    window : Window
        Objeto de tipo Window que soporta la parte gráfica de la aplicación.
    """

    def __init__(self, window):
        """
        Constructor de la clase PredictWindow que nos proporciona los métodos necesários para el recorte de los vídeos
        
        Parametros
        ----------
        window : Window
            Instancia de la clase que crea la ventana.
        """
        self.window = window 

    def cutVideo(self,index,start,end):
        """
        Función que recorta el vídeo.

        Parametros
        ----------
        index : íncide de la lista que contiene todos los vídeos. Este índice indica el vídeo que se ha de recortar.
        start : segundo del vídeo que corresponderá con el inicio del vídeo recortado.
        end : segundo del vídeo que corresponderá con el fin del vídeo recortado.
        """
        nameVideo="Recorte"+str(index)+".mp4"
        ffmpeg_extract_subclip(self.window.playlistFull[index], start, end, targetname=nameVideo)
        #Guardar los vídeos recortados en una carpeta y con un nombre concreto
        self.window.showVideo3.load(nameVideo)
        self.window.showVideo3.play()

    def showVideo(self):
        """
        Función que permite mostrar el recorte generado.
        El recorte deberá de ser guardado 
        """
        #1) Recortarlo 2) Guardarlo en una variable 3) Mostrarlo con el load + play
        #Los vídeos están a 30fps
        try : 
            if self.window.togglebutton.config('text')[-1] == 'OFF':
                index=self.window.selectVideo2
                clip = VideoFileClip(self.window.playlistFull[index])
                #El total de frames se ha de sacar del vídeo largo, es decir, del que hay que recortar
                frames = int(clip.fps * clip.duration)
                start_time=int(self.window.textFrameBegin.get())*int(clip.duration) / frames #11381 # 960
                print(start_time, self.window.showVideo2.pause() )
                end_time=int(self.window.textFrameEnd.get())*int(clip.duration) / frames #11381 # 960
                
                
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
        except:
            tkinter.messagebox.showerror('Frames no especificados', 'No se han especificado correctamente los frames de inicio y final del vídeo.')

