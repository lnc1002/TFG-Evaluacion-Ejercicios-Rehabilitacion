"""
Created on Wed Jun x 2022

@author: Lucía Núñez
"""
from doctest import master
from email.mime import image
import os
from sre_parse import State
from turtle import bgcolor, width
import cv2
from cv2 import VideoCapture
import imutils
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


from tkinter import ttk
from tkvideo import tkvideo
from tkVideoPlayer import TkinterVideo
import imageio

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


    #def addPlayList(self,filename):
    
    #    self.window.playlist.insert(self.window.index, filename)
    
    def colourButton(self,text):
        """
        Función que implementa el cambio de color de los diferentes botones al cambiar el modo de ejecución

        Parametros
        ----------
        text : especifica el modo que se va a establecer 
        """
        if text=="OFF":
            colour='#EEE8AA'
            self.window.togglebutton.config(text='OFF',bg='#EEE8AA')
        else:
            colour='#B0E2FF'
            self.window.togglebutton.config(text='ON',bg='#B0E2FF')

        self.window.buttonAdd1.config(bg=colour)
        self.window.buttonAdd2.config(bg=colour)
        self.window.buttonDel1.config(bg=colour)
        self.window.buttonDel2.config(bg=colour)
        self.window.playvideo1box.config(bg=colour)
        self.window.playvideo2box.config(bg=colour)


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
            #self.window.togglebutton.config(text='OFF',bg='#EEE8AA')
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
            #self.window.togglebutton.config(text='ON',bg='#B0E2FF')
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
       # self.delVideo(value)
        print(self.window.showVideo1,self.window.selectVideo1)

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
                try:
                    self.window.showVideo1.play()
                except:
                    tkinter.messagebox.showerror('Vídeo no selecionado', 'No hay ningun vídeo seleccionado.')

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
    