"""
Created on Wed Jun x 2022

@author: Lucía Núñez
"""

#from curses import window
from doctest import master
from email.mime import image
import os
from sre_parse import State
from turtle import width
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
#from pygame import mixer
import imageio

class MiddleWindow():
    """
    Clase mediadora. Esta clase se encarga de la comunicación entre ...
    """
    def __init__(self, window):
        self.window = window 

    def showExample(self,filedirectory,playbox,value,path):
        """
        Sirve para mostrar los videos sin la ruta completa S
        """
        for i,f in enumerate(filedirectory): 
            playbox.insert("end", f"{os.path.basename(f).split('.')[0]}")
            if value == 'S':
                self.window.playlistSpecific.insert(i,path+f)
            else:
                self.window.playlistFull.insert(i,path+f)



    def addPlayList(self,filename):
        self.window.playlist.insert(self.window.index, filename)
    
    def updateMode(self):
        ""

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
            self.window.togglebutton.config(text='OFF')

            
        else:
            self.delVideo(1)
            self.delVideo(2)
            self.window.textFrameBegin.config(state="disabled",background="red")
            self.window.textFrameEnd.config(state="disabled",background="red")
            #Se vacían las listas de vídeos 
            self.window.playvideo1box.delete(0,END)
            self.window.playvideo2box.delete(0,END)
            #Muestra los vídeos correspondientes
            self.showExample(os.listdir('VideosConcretos_Ej_ON'),self.window.playvideo1box,'S',os.path.abspath('VideosConcretos_Ej_ON')+'\\')
            self.showExample(os.listdir('VideosCompletos_Ej_ON'),self.window.playvideo2box,'F',os.path.abspath('VideosCompletos_Ej_ON')+'\\')
            self.window.togglebutton.config(text='ON')


    def delVideo(self,value):
        """
        Se tiene que borrar el vídeo que se está reproduciendo
        """
        if value == 1:
            self.window.showVideo1.load(0)
            self.window.showVideo1.config(state="disabled")
        else:
            self.window.showVideo2.load(0)
            self.window.showVideo2.config(state="disabled")
        # self.window.showVideo1.destroy()
        # self.showVideo1 = TkinterVideo(master=self.window.root, scaled=True)
        # self.showVideo1.place(relx=0.05,rely=0.4,relheight=0.45,relwidth=0.2)

        # self.window.showVideo2.destroy()
        # self.showVideo2 = TkinterVideo(master=self.window.root, scaled=True)
        # self.showVideo2.place(relx=0.3,rely=0.4,relheight=0.45,relwidth=0.2)

        #Añadir las del video resultado

    def addplayVideo(self,value):
        
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
        """
        if value == 1:
            self.window.showVideo1.play()
        else:
            self.window.showVideo2.play()
        #Else, play video resultado

    def pauseVideo(self,value):
        """
        Pausa el vídeo
        """
        if value == 1: 
            self.window.showVideo1.pause()
        else:
            self.window.showVideo2.pause()
        #Else, pause video resultado

    def stopVideo(self,value):
        ""
        if value == 1:
            self.window.showVideo1.stop()
        elif value==2:
            self.window.showVideo2.stop()
