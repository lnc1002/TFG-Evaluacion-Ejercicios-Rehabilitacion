"""
Created on Wed Jun x 2019
@author: Lucía Núñez
"""

from email.mime import image
import os
from sre_parse import State
from turtle import width
import cv2
#import imutils
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


from tkinter import ttk
from tkvideo import tkvideo
#from pygame import mixer
import imageio



class MiddleWindow():
    """
    Clase mediadora
    """
    def __init__(self, window):
        self.window = window 

    def showExample(self,filedirectory,playbox):
        """
        Sirve para mostrar los videos sin la ruta completa 
        """
        for f in filedirectory: 
           playbox.insert("end", f"{os.path.basename(f).split('.')[0]}") 

    def addPlayList(self,filename):
        self.window.playlist.insert(self.window.index, filename)
        

    def simpletoggle(self):
        """
        Esta función es para cuando se clica sobre él, que en el fondo valdría para modificar los valores 
        Si el modo ejemplo está activo, se mostrarán una serie de vídeos y se bloquearán las casillas correspondientes a los frames
        Cada vez que se pulse este botón tienen que cambiar el estado de las casillas
        """
        if self.window.togglebutton.config('text')[-1] == 'ON':
            #En caso de cambiar de ON a OFF se bloquean las casillas de frame
            self.window.textFrameInicio.config(state="normal")
            self.window.textFrameFinal.config(state="normal")
            #También se cambia las casillas para mostrar otros ejemplos
            #Vaciar lista 
            self.window.playvideo1box.delete(0,END)
            self.window.playvideo2box.delete(0,END)
            self.showExample(os.listdir('VideosConcretos_Ej_OFF'),self.window.playvideo1box)
            self.showExample(os.listdir('VideosCompletos_Ej_OFF'),self.window.playvideo2box)
            self.window.togglebutton.config(text='OFF')

            
        else:
            self.window.textFrameInicio.config(state="disabled",background="red")
            self.window.textFrameFinal.config(state="disabled",background="red")
            #Vaciar lista 
            self.window.playvideo1box.delete(0,END)
            self.window.playvideo2box.delete(0,END)
            #¿Se tendrá que actualizar la lista?
            self.showExample(os.listdir('VideosConcretos_Ej_ON'),self.window.playvideo1box)
            self.showExample(os.listdir('VideosCompletos_Ej_ON'),self.window.playvideo2box)
            self.window.togglebutton.config(text='ON')



    def addplayVideo(self):
        #print(self.window.playvideo1box.curselection())
        index = self.window.playvideo1box.curselection()[0]
        player = tkvideo(self.window.playlistConcretos[index], self.window.showVideo1, loop=1)


    #Vamos a hacer una función que clicando sobre el vídeo lo muestre en la casilla habilitada para ello

    def visualizar2(self,cap):
        #self.window.cap
        if self.window.cap is not None:
            ret, frame = self.window.cap.read()
            if ret == True:
                #frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.window.showVideo1.configure(image=img)
                self.window.showVideo1.image = img
                self.window.showVideo1.after(10, self.visualizar())
            else:
                self.window.showVideo1.image = ""
                self.window.cap.release()











    def visualizar(self):
        #self.window.cap
        if self.window.cap is not None:
            ret, frame = self.window.cap.read()
            if ret == True:
                #frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                self.window.showFile1.configure(image=img)
                self.window.showFile1.image = img
                self.window.showFile1.after(10, self.visualizar())
            else:
                self.window.showFile1.image = ""
                self.window.cap.release()

    def add_files(self):
        """
        Será la encargada de cargar los archivos
        """
        
        if self.window.cap is not None:
            self.window.showFile1.image = ""
            self.window.cap.release()
            self.window.cap = None
        video_path = filedialog.askopenfilename(filetypes = [
            ("all video format", ".mp4"),
            ("all video format", ".avi")])
        if len(video_path) > 0:
            #lblInfoVideoPath.configure(text=video_path)
            self.window.cap = cv2.VideoCapture(video_path)
            self.visualizar()



    def play_files(self,files):
        
        #No se si hacerlo asi
        self.window.playfile1.insert(self.window.index, files[1])
        self.window.playfile2.insert(self.window.index, files[2])
    
    def play_video(self):
        if self.window.paused:
            ""

    def stop_video(self):
        ""

    def pause_video(self):
        ""
    
    def rewind_music(self):
        ""
    
    def on_closing(self):
        ""