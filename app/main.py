from asyncio.base_tasks import _task_get_stack
#from distutils.cmd import Command
from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import ttk #_Relief
from tkinter import font  as tkfont 
from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
import os
from tkVideoPlayer import TkinterVideo

from MiddleWindow import MiddleWindow
from PredictWindow import PredictWindow

class Window(object):
   """
   Clase encargada de definir todos los elementos gráficos de la aplicación.
   Esta clase únicamente contiene el constructor, en el cual se van a definir los objetos básicos
   con los que el usuario podrá interactuar.

   author: Lucía Núñez 

   Atributos
   ----------
   //Atributos imprescindibles para el correcto funcionamiento
   root : Tk
   middleWindw : MiddleWindow

   //Labels de texto y botones
   tittlebar : Label
   title : Label
   modeExample : Label
   togglebutton : Button
   specificVideoLoad : Label
   playvideo1box : Listbox
   fullVideoLoad : Label 
   playvideo2box : Listbox
   buttonAdd1 : Button
   buttonAdd2 : Button
   buttonDel1 : Button
   buttonDel2 : Button
   specificVideo : Label
   showVideo1 : TkinterVideo
   fullVideo : Label
   showVideo2 : TkinterVideo
   videoResult : Label
   -----falta la del video de reultado
   frameBegin : Label
   textFrameBegin : Entry
   frameEnd : Label
   textFrameEnd : Entry
   convert : Button
   play1 : Button
   pause1 : Button
   stop1 : Button
   play2 : Button
   pause2 : Button
   stop2 : Button
   play3 : Button
   pause3 : Button
   stop3 : Button


   """

   def __init__(self):
        """
        Inicializa todas los botones etc para cargar los vídeos
        """
        self.root = Tk()
        #self.cap = None
        self.root.geometry('1366x868')
        self.root.title('Extracción de ejercicios')
        self.middleWindw = MiddleWindow(self)
        self.predictWindow = PredictWindow(self)
        self.selectVideo1 = []
        self.selectVideo2 = []

        #Pie de página
        self.tittlebar = ttk.Label(self.root, 
                                    text="Reconocimiento de ejercicios completos en pacientes con la enfermedad de Parkinson", 
                                    relief=SUNKEN, anchor=W, 
                                    font='Times 12 italic')
        self.tittlebar.pack(side=BOTTOM, fill=X)

        #Configuración del color de fondo
        self.root['bg'] = '#F7F7F7'

        self.root.title("Parkinson Detection Exercises")

        self.title = ttk.Label(self.root, text='Detección de ejercicios',font='Calibri 25',background='#F7F7F7').place(relx=0.38, rely=0.04)

        #Modo ejemplo
        self.modeExample = ttk.Label(self.root, text='Modo ejemplo',font='Calibri 15',background='#F7F7F7').place(relx=0.04,rely=0.1)
        self.togglebutton =ttk.Button(self.root, text="ON", command=self.middleWindw.simpletoggle)
        self.togglebutton.place(relx=0.14,rely=0.1)

        # Se debe guardar la ruta completa junto con el nombre del fichero
        #self.playlistSpecific = []
        #self.playlistFull = []
        self.playlistSpecific = []
        self.playlistFull = []
        #self.index = 0 #iniciamos el indice que se usará en la lista
        #Se crean un par de listas para que el usuario pueda escoger los vídeos
        self.specificVideoLoad = ttk.Label(self.root, text='Videos concretos cargados',font='Calibri 12',background='#F7F7F7').place(relx=0.045,rely=0.22)
        self.playvideo1box = Listbox(self.root, relief=RAISED,background='#FEB8A9',font='Calibri 12')
        self.playvideo1box.place(relx=0.05,rely=0.25,relheight=0.1,relwidth=0.12)
        self.fullVideoLoad = ttk.Label(self.root, text='Videos completos cargados',font='Calibri 12',background='#F7F7F7').place(relx=0.295,rely=0.22)
        self.playvideo2box = Listbox(self.root, relief=RAISED,font='Calibri 12')
        self.playvideo2box.place(relx=0.3,rely=0.25,relheight=0.1,relwidth=0.12)

        #Cargamos los ejemplos que se encuentran en los diferentes directorios
        filedirectory=os.listdir('VideosConcretos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo1box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistSpecific.insert(i,os.path.abspath('VideosConcretos_Ej_ON')+'\\'+f)

        filedirectory=os.listdir('VideosCompletos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo2box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistFull.insert(i,os.path.abspath('VideosCompletos_Ej_ON')+'\\'+f)
        
        self.buttonAdd1= ttk.Button(self.root, text='Añadir',command=lambda:self.middleWindw.addplayVideo(1))
        self.buttonAdd1.place(relx=0.18,rely=0.27)
        self.buttonAdd2= ttk.Button(self.root, text='Añadir',command=lambda:self.middleWindw.addplayVideo(2))
        self.buttonAdd2.place(relx=0.43,rely=0.27)

        self.buttonDel1= ttk.Button(self.root, text='Descartar',command=lambda:self.middleWindw.delVideo(1))
        self.buttonDel1.place(relx=0.18,rely=0.3)
        self.buttonDel2= ttk.Button(self.root, text='Descartar',command=lambda:self.middleWindw.delVideo(2))
        self.buttonDel2.place(relx=0.43,rely=0.3)
         
        #Se crean las casillas donde se localizarán los vídeos 
        self.specificVideo = ttk.Label(self.root, text='Video concreto',font='Calibri 14',background='#F7F7F7').place(relx=0.1,rely=0.37)
        self.showVideo1 = TkinterVideo(master=self.root, scaled=True)
        self.showVideo1.place(relx=0.05,rely=0.4,relheight=0.45,relwidth=0.2)
        self.fullVideo = ttk.Label(self.root, text='Video completo',font='Calibri 14',background='#F7F7F7').place(relx=0.35,rely=0.37)
        self.showVideo2 = TkinterVideo(master=self.root, scaled=True)
        self.showVideo2.place(relx=0.3,rely=0.4,relheight=0.45,relwidth=0.2)

        #Se crea la casilla del video resultado
        self.videoResult = ttk.Label(self.root, text='Video resultado',font='Calibri 14',background='#F7F7F7').place(relx=0.75,rely=0.37)
        self.showVideo3 = ttk.Label(self.root, relief=RAISED).place(relx=0.7,rely=0.4,relheight=0.45,relwidth=0.2)

        #Habilitamos unas casillas para indicar los frames por los que se recortará
        self.frameBegin = ttk.Label(self.root, text='Frame incicio').place(relx=0.72,rely=0.22)
        self.textFrameBegin = ttk.Entry(self.root,state="disabled")
        self.textFrameBegin.place(relx=0.72,rely=0.25,relheight=0.05,relwidth=0.07)
        self.frameEnd = ttk.Label(self.root, text='Frame final').place(relx=0.82,rely=0.22)
        self.textFrameEnd = ttk.Entry(self.root,state="disabled")
        self.textFrameEnd.place(relx=0.82,rely=0.25,relheight=0.05,relwidth=0.07)

        #Ponemos un botón para convertir
        self.convert = ttk.Button(self.root, text="Recortar",command=self.predictWindow.showVideo)
        self.convert.place(relx=0.55,rely=0.6)
        
        #Añadimos botones play, stop y pause al final de la ejecución 
        self.play1 = ttk.Button(self.root, text='play',command=lambda:self.middleWindw.playVideo(1))
        self.play1.place(relx=0.05, rely=0.86)
        self.pause1 = ttk.Button(self.root, text='pause',command=lambda:self.middleWindw.pauseVideo(1))
        self.pause1.place(relx=0.12, rely=0.86)
        self.stop1 = ttk.Button(self.root, text='stop',command=lambda:self.middleWindw.stopVideo(1))
        self.stop1.place(relx=0.19, rely=0.86)

        self.play2 = ttk.Button(self.root, text='play',command=lambda:self.middleWindw.playVideo(2))
        self.play2.place(relx=0.3, rely=0.86)
        self.pause2 = ttk.Button(self.root, text='pause',command=lambda:self.middleWindw.pauseVideo(2))
        self.pause2.place(relx=0.37, rely=0.86)
        self.stop2 = ttk.Button(self.root, text='stop',command=lambda:self.middleWindw.stopVideo(2))
        self.stop2.place(relx=0.44, rely=0.86)

        self.play3 = ttk.Button(self.root, text='play',command=lambda:self.middleWindw.playVideo(3))
        self.play3.place(relx=0.7, rely=0.86)
        self.pause3 = ttk.Button(self.root, text='pause',command=lambda:self.middleWindw.pauseVideo(3))
        self.pause3.place(relx=0.76, rely=0.86)
        self.stop3 = ttk.Button(self.root, text='stop',command=lambda:self.middleWindw.stopVideo(3))
        self.stop3.place(relx=0.83, rely=0.86)
      
        self.root.mainloop()

if __name__ == '__main__':
    Window()
