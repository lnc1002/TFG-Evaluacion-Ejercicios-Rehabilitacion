"""
Created on Wed Jun 8 2022

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
        Función que permite mostrar el recorte generado. Para ello, recortará el vídeo, se guardará en el resultado generado
        y posteriormente se visualizará en la casilla corespondiente al vídeo resultado. 
        El recorte deberá de ser guardado 
        """
        try : 
            if self.window.togglebutton.config('text')[-1] == 'OFF':
                index=self.window.selectVideo2
                clip = VideoFileClip(self.window.playlistFull[index])
                frames = int(clip.fps * clip.duration)
                #Se realiza una regla de tres para obtener el segundo de recorte a partir de los frames especificados
                start_time=int(self.window.textFrameBegin.get())*int(clip.duration) / frames 
                end_time=int(self.window.textFrameEnd.get())*int(clip.duration) / frames 
                self.cutVideo(index,start_time,end_time)

            else:
                #Modo (ON)
                #Recortar según los frames obtenidos con el programa
                index1=self.window.selectVideo1
                index2=self.window.selectVideo2
                if index1 == 0:
                    #Ejercicio 1
                    clip = VideoFileClip(self.window.playlistSpecific[0])
                    self.cutVideo(index2,6.84,32.48)
                elif index1 == 3:
                    #Ejercicio 9
                    clip = VideoFileClip(self.window.playlistSpecific[0])
                    self.cutVideo(index2,8.64,24.7)
                elif index1 == 1:
                    #Ejercicio 22
                    clip = VideoFileClip(self.window.playlistSpecific[0])
                    self.cutVideo(index2,4.83,35.30)
                elif index1 == 2:
                    #Ejercicio 23
                    clip = VideoFileClip(self.window.playlistSpecific[0])
                    self.cutVideo(index2,17.14,50.64)
        except:
            if self.window.togglebutton.config('text')[-1] == 'OFF':
                tkinter.messagebox.showerror('Frames no especificados', 'No se han especificado correctamente los frames de inicio y final del vídeo.')
            else:
                tkinter.messagebox.showerror('Vídeos no especificados', 'No se han especificado correctamente los vídeos, seleccione un vídeo concreto y un vídeo completo por favor.')

