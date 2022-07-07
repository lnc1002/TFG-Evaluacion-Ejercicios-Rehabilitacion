from asyncio.base_tasks import _task_get_stack
from lib2to3.pgen2.token import LEFTSHIFT
import tkinter as tk
from tkinter import ttk #_Relief
from tkinter import font  as tkfont 
from tkinter import *
from turtle import backward, bgcolor
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
   menubar : Menu
   subMenu : Menu
   colourSup : Frame
   title : Label
   modeExample : Label
   togglebutton : Button
   specificVideoLoad : Label
   playvideo1box : Listbox
   fullVideoLoad : Label 
   playvideo2box : Listbox
   buttonAdd1 : Button
   warning : Label
   buttonAdd2 : Button
   buttonDel1 : Button
   buttonDel2 : Button
   specificVideo : Label
   showVideo1 : TkinterVideo
   fullVideo : Label
   showVideo2 : TkinterVideo
   videoResult : Label
   showVideo3 : TkinterVideo
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
        Inicializa todas los botones, colores y funciones necesárias para mostrar los vídeos y el resultado esèrado.
        """
        self.root = Tk()
        #self.cap = None
        self.root.geometry('1366x868')
        self.root.title('Extracción de ejercicios')
        self.middleWindw = MiddleWindow(self)
        self.predictWindow = PredictWindow(self)
        self.selectVideo1 = []
        self.selectVideo2 = []

        #Etiquetas de estilo
        style = ttk.Style()
        style.configure("BW.Blue", background="Red")

        # Pie de página
        self.tittlebar = ttk.Label(self.root, 
                                    text="Reconocimiento de ejercicios completos en pacientes con la enfermedad de Parkinson", 
                                    relief=SUNKEN, anchor=W, 
                                    font='Times 12 italic')
        self.tittlebar.pack(side=BOTTOM, fill=X)

        # Configuración del color de fondo
        self.root['bg'] = '#E0EEEE' 

        # Create the menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        
        # Creación del submenu
        subMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Ayuda", menu=subMenu)
        subMenu.add_command(label="Proyecto", command=self.middleWindw.about_us)
        subMenu.add_command(label="Modo ejemplo", command=self.middleWindw.mode)


        # Cabecera superior con color
        self.colourSup = tk.Frame(self.root, bg='#66CDAA')
        self.colourSup.place(relheight=0.15,relwidth=1)

        self.root.title("Parkinson Detection Exercises")

        self.title = tk.Label(self.root, text='Detección de ejercicios',font='Calibri 28',background='#66CDAA')
        self.title.place(relx=0.38, rely=0.04)

        # Modo ejemplo
        self.modeExample = tk.Label(self.root, text='Modo ejemplo',font='Calibri 18',background='#66CDAA')
        self.modeExample.place(relx=0.04,rely=0.1)
        self.togglebutton =tk.Button(self.root, text="ON", bg = '#B0E2FF',command=self.middleWindw.simpletoggle)
        self.togglebutton.place(relx=0.16,rely=0.11,relwidth=0.05)

        # Se debe guardar la ruta completa junto con el nombre del fichero
        self.playlistSpecific = []
        self.playlistFull = []
        # Creación de un par de listas para que el usuario pueda escoger los vídeos
        self.specificVideoLoad = tk.Label(self.root, text='Videos concretos cargados',font='Calibri 14',background='#E0EEEE')
        self.specificVideoLoad .place(relx=0.046,rely=0.21)
        self.playvideo1box = Listbox(self.root, relief=RAISED,background='#B0E2FF',font='Calibri 12')
        self.playvideo1box.place(relx=0.05,rely=0.25,relheight=0.1,relwidth=0.12)
        self.fullVideoLoad = tk.Label(self.root, text='Videos completos cargados',font='Calibri 14',background='#E0EEEE')
        self.fullVideoLoad.place(relx=0.326,rely=0.21)
        self.playvideo2box = Listbox(self.root, relief=RAISED,background='#B0E2FF',font='Calibri 12')
        self.playvideo2box.place(relx=0.33,rely=0.25,relheight=0.1,relwidth=0.12)

        # Carga de los ejemplos que se encuentran en los diferentes directorios
        filedirectory=os.listdir('VideosConcretos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo1box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistSpecific.insert(i,os.path.abspath('VideosConcretos_Ej_ON')+'\\'+f)

        filedirectory=os.listdir('VideosCompletos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo2box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistFull.insert(i,os.path.abspath('VideosCompletos_Ej_ON')+'\\'+f)
        
        self.buttonAdd1= tk.Button(self.root, text='Mostrar',font='Calibri 12',bg='#B0E2FF',command=lambda:self.middleWindw.addplayVideo(1))
        self.buttonAdd1.place(relx=0.18,rely=0.255,relwidth=0.055)
        self.buttonAdd2= tk.Button(self.root, text='Mostrar',font='Calibri 12',bg='#B0E2FF',command=lambda:self.middleWindw.addplayVideo(2))
        self.buttonAdd2.place(relx=0.46,rely=0.255,relwidth=0.055)
        self.warning = tk.Label(self.root, text='Descarta un vídeo antes de añadir uno nuevo',font='Calibri 8',bg='#FCE8BE').place(relx=0.52,rely=0.26)
        
        self.buttonDel1= tk.Button(self.root, text='Descartar',font='Calibri 12',bg='#B0E2FF',command=lambda:self.middleWindw.delVideo(1))
        self.buttonDel1.place(relx=0.18,rely=0.3)
        self.buttonDel2= tk.Button(self.root, text='Descartar',font='Calibri 12',bg='#B0E2FF',command=lambda:self.middleWindw.delVideo(2))
        self.buttonDel2.place(relx=0.46,rely=0.3)
         
        # Creación de casillas donde se visualizarán los vídeos 
        self.specificVideo = tk.Label(self.root, text='Video concreto',font='Calibri 14',background='#E0EEEE')
        self.specificVideo.place(relx=0.1,rely=0.36)
        self.showVideo1 = TkinterVideo(master=self.root, scaled=True)
        self.showVideo1.place(relx=0.05,rely=0.4,relheight=0.45,relwidth=0.2)
        self.fullVideo = tk.Label(self.root, text='Video completo',font='Calibri 14',background='#E0EEEE')
        self.fullVideo.place(relx=0.38,rely=0.36)
        self.showVideo2 = TkinterVideo(master=self.root, scaled=True)
        self.showVideo2.place(relx=0.33,rely=0.4,relheight=0.45,relwidth=0.2)

        # Creacion de la casilla donde se visualizará el video resultado
        self.videoResult = tk.Label(self.root, text='Video resultado',font='Calibri 14',background='#E0EEEE')
        self.videoResult.place(relx=0.75,rely=0.36)

        self.showVideo3 = TkinterVideo(master=self.root, scaled=True)
        self.showVideo3.place(relx=0.7,rely=0.4,relheight=0.45,relwidth=0.2)

        # Habilitación de unas casillas para especificar los frames por los que se recortará
        self.frameBegin = tk.Label(self.root, text='Frame incicio',font='Calibri 14',background='#E0EEEE')
        self.frameBegin.place(relx=0.72,rely=0.22)
        self.textFrameBegin = tk.Entry(self.root,state="disabled",font='Calibri 14',background='#DEBBF5')
        self.textFrameBegin.place(relx=0.72,rely=0.25,relheight=0.05,relwidth=0.07)
        self.frameEnd = tk.Label(self.root, text='Frame final',font='Calibri 14',background='#E0EEEE')
        self.frameEnd.place(relx=0.82,rely=0.22)
        self.textFrameEnd = tk.Entry(self.root,state="disabled",font='Calibri 14',background='#DEBBF5')
        self.textFrameEnd.place(relx=0.82,rely=0.25,relheight=0.05,relwidth=0.07)

        # Botón para convertir
        self.convert = tk.Button(self.root, text="Recortar",font='Calibri 14',bg='#66CDAA',command=self.predictWindow.showVideo)
        self.convert.place(relx=0.58,rely=0.6,relheight=0.06,relwidth=0.06)

        # Botones play, stop y pause al final de la ejecución 
        self.play1 = tk.Button(self.root, text='play',bg='#79CDCD', command=lambda:self.middleWindw.playVideo(1))
        self.play1.place(relx=0.05, rely=0.86, relwidth=0.06)
        self.pause1 = tk.Button(self.root, text='pause',bg='#8DEEEE',command=lambda:self.middleWindw.pauseVideo(1))
        self.pause1.place(relx=0.12, rely=0.86, relwidth=0.06)
        self.stop1 = tk.Button(self.root, text='stop',bg='#97FFFF',command=lambda:self.middleWindw.stopVideo(1))
        self.stop1.place(relx=0.19, rely=0.86, relwidth=0.06)

        self.play2 = tk.Button(self.root, text='play',bg='#79CDCD',command=lambda:self.middleWindw.playVideo(2))
        self.play2.place(relx=0.33, rely=0.86, relwidth=0.06)
        self.pause2 = tk.Button(self.root, text='pause',	bg='#8DEEEE',command=lambda:self.middleWindw.pauseVideo(2))
        self.pause2.place(relx=0.4, rely=0.86, relwidth=0.06)
        self.stop2 = tk.Button(self.root, text='stop',bg='#97FFFF',command=lambda:self.middleWindw.stopVideo(2))
        self.stop2.place(relx=0.47, rely=0.86, relwidth=0.06)

        self.play3 = tk.Button(self.root, text='play',bg='#79CDCD',command=lambda:self.middleWindw.playVideo(3))
        self.play3.place(relx=0.7, rely=0.86, relwidth=0.06)
        self.pause3 = tk.Button(self.root, text='pause',bg='#8DEEEE',command=lambda:self.middleWindw.pauseVideo(3))
        self.pause3.place(relx=0.77, rely=0.86, relwidth=0.06)
        self.stop3 = tk.Button(self.root, text='stop',bg='#97FFFF',command=lambda:self.middleWindw.stopVideo(3))
        self.stop3.place(relx=0.84, rely=0.86, relwidth=0.06)
      
        self.root.mainloop()

if __name__ == '__main__':
    Window()
