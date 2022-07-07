"""
Created on Wed Jun 1 2022

@author: Lucía Núñez
"""
from doctest import master
from email.mime import image
import os
from sre_parse import State
from turtle import bgcolor, width
from cv2 import VideoCapture
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkvideo import tkvideo
from tkVideoPlayer import TkinterVideo


class MiddleWindow():
    """
    Clase mediadora. Esta clase se encarga de la comunicación entre los elementos que se muestran en la ventana de inicio.
    Esta clase actúa sobre los eventos de carga y reproducción de vídeos.
    Contiene diversos métodos para el funcionamiento de las característicar requeridas.

    authora: Lucía Núñez
    
    Atributos
    ----------
    window : Window
        Objeto de tipo Window que soporta la parte gráfica de la aplicación.

    """
    def __init__(self, window):
        """
        Constructor de la clase MiddleWindow que nos proporciona los métodos necesários para la carga y reproducción de vídeo
        
        Parametros
        ----------
        window : Window
            Instancia de la clase que crea la ventana.
        """
        self.window = window 

    def showExample(self,filedirectory,playbox,value,path):
        """
        Función que muestra los vídeos sin la ruta completa de los mismos. Sirve para mostrar los videos sin la ruta completa S

        Parametros
        ----------
        filedirectory : Directorio en el que se localizan los vídeos. 
        playbox : lista en la que se van a mostrar los vídeos.
        value : Informa sobre en que lista se va a guardar el vídeo cargado, si en la lista de los vídeos específicos o en la lista de vídeos concretos.
        path : Ruta completa en la que se localizan los vídeos.
        """
        for i,f in enumerate(filedirectory): 
            playbox.insert("end", f"{os.path.basename(f).split('.')[0]}")
            if value == 'S':
                self.window.playlistSpecific.insert(i,path+f)
            else:
                self.window.playlistFull.insert(i,path+f)

    
    def colourButton(self,text):
        """
        Función que implementa el cambio de color de los diferentes botones al cambiar el modo de ejecución

        Parametros
        ----------
        text : especifica el modo que se va a establecer 
        """
        if text=="OFF":
            #lila
            color_play='#B8A0C9'
            color_pause='#C2ADD1'
            color_stop='#D0BBDE'
            color_backg='#F1E3FB'
            colour_button='#DEBBF5'
            colour_cab='#CB8CF5'
            self.window.togglebutton.config(text='OFF',bg='#DEBBF5')
        else:
            color_play='#79CDCD'
            color_pause='#8DEEEE'
            color_stop='#97FFFF'
            color_backg='#E0EEEE'
            colour_button='#B0E2FF'
            colour_cab='#66CDAA'
            self.window.togglebutton.config(text='ON',bg='#B0E2FF')

        #Botones principales
        self.window.buttonAdd1.config(bg=colour_button)
        self.window.buttonAdd2.config(bg=colour_button)
        self.window.buttonDel1.config(bg=colour_button)
        self.window.buttonDel2.config(bg=colour_button)
        self.window.playvideo1box.config(bg=colour_button)
        self.window.playvideo2box.config(bg=colour_button)
        #Botones play/pause/stop
        self.window.play1.config(bg=color_play)
        self.window.play2.config(bg=color_play)
        self.window.play3.config(bg=color_play)
        self.window.pause1.config(bg=color_pause)
        self.window.pause2.config(bg=color_pause)
        self.window.pause3.config(bg=color_pause)
        self.window.stop1.config(bg=color_stop)
        self.window.stop2.config(bg=color_stop)
        self.window.stop3.config(bg=color_stop)
        #Fondos de las Labels
        self.window.title.config(bg=colour_cab)
        self.window.modeExample.config(bg=colour_cab)
        self.window.specificVideoLoad.config(bg=color_backg)
        self.window.fullVideoLoad.config(bg=color_backg)
        self.window.specificVideo.config(bg=color_backg)
        self.window.fullVideo.config(bg=color_backg)
        self.window.videoResult.config(bg=color_backg)
        self.window.frameBegin.config(bg=color_backg)
        self.window.frameEnd.config(bg=color_backg)
        #Cabecera y botón de recortar
        self.window.colourSup.config(bg=colour_cab)
        self.window.convert.config(bg=colour_cab)
        #Color de fondo
        self.window.root['bg'] = color_backg


    def simpletoggle(self):
        """
        Esta función sirve para cambiar el modo de la aplicación.
        Al seleccionar sobre el botón "ON/OFF" se deben modificar ciertos botones como:
            1) En el modo ON las casillas correspondientes a los valores de los frames estarán bloqueadas
            2) Los videos mostrados en cada modo son diferentes 
        """
        if self.window.togglebutton.config('text')[-1] == 'ON':
            #Si existe algún vídeo cargado lo elimina
            self.delVideo(1)
            self.delVideo(2)
            #Desbloquean las casillas de frame
            self.window.textFrameBegin.config(state="normal")
            self.window.textFrameEnd.config(state="normal")
            #Se vacían las listas de vídeos
            self.window.playvideo1box.delete(0,END)
            self.window.playvideo2box.delete(0,END)
            #Muestra los vídeos correspondientes 
            self.showExample(os.listdir('VideosConcretos_Ej_OFF'),self.window.playvideo1box,'S',os.path.abspath('VideosConcretos_Ej_OFF')+'\\')
            self.showExample(os.listdir('VideosCompletos_Ej_OFF'),self.window.playvideo2box,'F',os.path.abspath('VideosCompletos_Ej_OFF')+'\\')
            self.colourButton("OFF")

            
        else:
            #Si existe algún vídeo cargado lo elimina
            self.delVideo(1)
            self.delVideo(2)
            #Bloquean las casillas de frame
            self.window.textFrameBegin.config(state="disabled")
            self.window.textFrameEnd.config(state="disabled")
            #Se vacían las listas de vídeos 
            self.window.playvideo1box.delete(0,END)
            self.window.playvideo2box.delete(0,END)
            #Muestra los vídeos correspondientes
            self.showExample(os.listdir('VideosConcretos_Ej_ON'),self.window.playvideo1box,'S',os.path.abspath('VideosConcretos_Ej_ON')+'\\')
            self.showExample(os.listdir('VideosCompletos_Ej_ON'),self.window.playvideo2box,'F',os.path.abspath('VideosCompletos_Ej_ON')+'\\')
            self.colourButton("ON")


    def delVideo(self,value):
        """
        Esta función no llega a eliminar el video que se está emitiendo pero si que lo bloquea

        Parametros
        ----------
        value : Valor que indica el vídeo que se desea eliminar
        """
        if value == 1:
            self.window.showVideo1.load(0)
            self.window.showVideo1.config(state="disabled")
        else:
            self.window.showVideo2.load(0)
            self.window.showVideo2.config(state="disabled")


    def addplayVideo(self,value):
        """
        Esta función muestra y reproduce el vídeo seleccionado

        Parametros
        ----------
        value : Valor que indica el vídeo que se desea mostrar
        """
        if value == 1:
            self.window.showVideo1.config(state="normal")
            index=self.window.playvideo1box.curselection()[0]
            self.window.selectVideo1=index
            self.window.showVideo1.load(self.window.playlistSpecific[index])
            self.window.showVideo1.play()
        else:
            self.window.showVideo2.config(state="normal")
            index2 = self.window.playvideo2box.curselection()[0]
            self.window.selectVideo2=index2
            self.window.showVideo2.load(self.window.playlistFull[index2])
            self.window.showVideo2.play()


    def playVideo(self,value):
        """
        Esta función reproduce el vídeo seleccionado

        Parametros
        ----------
        value : Valor que indica el vídeo que se desea reproducir
        """
        try:
            if value == 1:
                self.window.showVideo1.play()
            elif value == 2:
                self.window.showVideo2.play()
            else:
                self.window.showVideo3.play()
        except:
            tkinter.messagebox.showerror('Vídeo no selecionado', 'No hay ningun vídeo seleccionado.')
         

    def pauseVideo(self,value):
        """
        Esta función pausa el vídeo seleccionado

        Parametros
        ----------
        value : Valor que indica el vídeo que se desea pausar
        """
        if value == 1: 
            self.window.showVideo1.pause()
        elif value == 2:
            self.window.showVideo2.pause()
        else:
            self.window.showVideo3.pause()


    def stopVideo(self,value):
        """
        Esta función para el vídeo seleccionado, hace la función de "stop", una vez se pulsa, el vídeo volverá a 
        reproducirse desde el inicio en caso de que posteriormente se pulse el "play"

        Parametros
        ----------
        value : Valor que indica el vídeo que se desea parar
        """
        if value == 1:
            self.window.showVideo1.stop()
        elif value==2:
            self.window.showVideo2.stop()
        else:
            self.window.showVideo2.pause()

    def about_us(self):
        """
        Esta función muestra un mensaje de información sobre la autoría del proyecto.
        """
        tkinter.messagebox.showinfo('Proyecto', 'Trabajo Fin de Grado.\n\nTipo de proyecto: Proyecto de investigación sobre la detección de ejercicios \n\nAlumno: Lucía Núñez \n\nTutores: José Francisco Díez Pastor, José Miguel Ramírez Sanz, José Luis Garrido Labrador')
        
    def mode(self):
        """
        Esta función muestra un mensaje de información sobre los modos de ejecución de la aplicación.
        """
        tkinter.messagebox.showinfo('Modo ejemplo','Modo ejemplo ON: El modo ejemplo servirá para presentar una muestra visual de lo obtenido durante el proyecto al tribunal del TFG. \n\nModo ejemplo OFF: Este modo ha sido utilizado para comprobar el correcto funcionamiento del programa y es el que se podrá implementar más adelante para ser usado por terapeutas')
    
