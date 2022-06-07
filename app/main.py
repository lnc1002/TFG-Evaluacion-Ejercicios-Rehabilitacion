
from asyncio.base_tasks import _task_get_stack
from distutils.cmd import Command
from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import ttk #_Relief
from tkinter import font  as tkfont 
from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk
import os

from MiddleWindow import MiddleWindow

class Window(object):

    def __init__(self):
        """
        Inicializa todas los botones etc para cargar los vídeos
        """

        self.root = Tk()
        self.cap = None
        self.root.geometry('1366x868')
        self.root.title('Extracción de ejercicios')
        self.middleWindw = MiddleWindow(self)


        # "Pie de página"
        self.tittlebar = ttk.Label(self.root, 
                                    text="Bienvenido al reconocimiento de ejercicios utilizados para paliar la enfermedad de Parkinson", 
                                    relief=SUNKEN, anchor=W, 
                                    font='Times 10 italic')
        self.tittlebar.pack(side=BOTTOM, fill=X)

        #Establecemos una imagen de fondo
        #self.imagen= PhotoImage(file="Fondo2.jpg")
        #self.background = ttk.Label(self.root, image = self.imagen, text = "Imagen S.O de fondo")
        #self.background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #Label(self.root, image=imagen, bd=0).pack()

        #self.root.configure(bg='red')
        self.root['bg'] ='#FAF0E6'


        # Create the menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # Create the submenu
        subMenu = Menu(self.menubar, tearoff=0)

        #Añadir cosas al menú y al submenú cuando funcione la app

        #Vamos a empezar a crear los botones
        #self.buttonAdd1 = ttk.Button(self.root,text="+ Añadir vídeo LARGO")
        #self.buttonAdd1.pack(anchor=W, padx=100, pady=50)

        #Modo ejemplo
        self.modeExample = ttk.Label(self.root, text='Modo ejemplo').place(relx=0.08,rely=0.15)
        #Al lado hacemos un botón que esté en on y al clicar sobre él se ponga en off
        self.togglebutton =ttk.Button(self.root, text="ON", command=self.middleWindw.simpletoggle)
        self.togglebutton.place(relx=0.18,rely=0.15)

        
        # Save full path + filename
        self.playlistConcretos = []
        self.playlistCompletos = []
        self.index = 0 #iniciamos el indice que se usará en la lista
        #Se crean las listas para seleccionar los vídeos 
        self.videosConcretosCargados = ttk.Label(self.root, text='Videos concretos cargados:').place(relx=0.08,rely=0.22)
        self.playvideo1box = Listbox(self.root, relief=RAISED)
        self.playvideo1box.place(relx=0.05,rely=0.25,relheight=0.1,relwidth=0.2)
        self.videosCompletoCargados = ttk.Label(self.root, text='Videos completos cargados:').place(relx=0.33,rely=0.22)
        self.playvideo2box = Listbox(self.root, relief=RAISED)
        self.playvideo2box.place(relx=0.3,rely=0.25,relheight=0.1,relwidth=0.2)
        
        #Con esto consigo que salga sólo el nombre
        # filedirectory = os.listdir("<path>")
        # for f in filedirectory: 
        #   listbox.insert("end", f"{os.path.basename(f).split('.')[0]}") 


        #Para hacer el for quitar el fichero que especificp en la ruta, dejar solo la suta de la carpeta
        filedirectory=os.listdir('VideosConcretos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo1box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistConcretos.insert(i,os.path.abspath(f))
         

        filedirectory=os.listdir('VideosCompletos_Ej_ON')
        for i,f in enumerate(filedirectory): 
           self.playvideo2box.insert("end", f"{os.path.basename(f).split('.')[0]}") 
           self.playlistCompletos.insert(i,os.path.abspath(f))
        #    self.playvideo1box.insert(f)

        
        #Vamos a comprobar aqui si seleccionando el video lo muestra en su ventana
        #self.select_video = self.playvideo1box.curselection() #Guardamos la selección
        #Vamos a poner un par de botones para añadir el video
        self.buttonAdd1= ttk.Button(self.root, text='Add',command=self.middleWindw.addplayVideo)
        self.buttonAdd1.place(relx=0.22,rely=0.30)
        self.buttonAdd2= ttk.Button(self.root, text='Add',command=self.middleWindw.addplayVideo)
        self.buttonAdd2.place(relx=0.52,rely=0.30)


         
        #Creamos las casillas donde se localizarán los vídeos 
        self.videoConcreto = ttk.Label(self.root, text='Video concreto').place(relx=0.11,rely=0.37)
        self.showVideo1 = ttk.Label(self.root, relief=RAISED)
        self.showVideo1.place(relx=0.05,rely=0.4,relheight=0.45,relwidth=0.2)
        self.videoCompleto = ttk.Label(self.root, text='Video completo').place(relx=0.36,rely=0.37)
        self.showVideo2 = ttk.Label(self.root, relief=RAISED).place(relx=0.3,rely=0.4,relheight=0.45,relwidth=0.2)

        #Se intenta guardar en el vídeo
        #self.middleWindw.visualizar2(select_video)

        #Creamos el video de resultado
        self.videoResultado = ttk.Label(self.root, text='Video resultado').place(relx=0.76,rely=0.37)
        self.showVideo3 = ttk.Label(self.root, relief=RAISED).place(relx=0.7,rely=0.4,relheight=0.45,relwidth=0.2)

        #Habilitamos unas casillas para indicar los frames por los que se recortará
        self.frameInicio = ttk.Label(self.root, text='Frame incicio').place(relx=0.72,rely=0.22)
        self.textFrameInicio = ttk.Entry(self.root,state="disabled")
        self.textFrameInicio.place(relx=0.72,rely=0.25,relheight=0.05,relwidth=0.07)
        self.frameFinal = ttk.Label(self.root, text='Frame final').place(relx=0.82,rely=0.22)
        self.textFrameFinal = ttk.Entry(self.root,state="disabled")
        self.textFrameFinal.place(relx=0.82,rely=0.25,relheight=0.05,relwidth=0.07)

        #Ponemos un botón para convertir
        self.convertir = ttk.Button(self.root, text="Recortar")
        self.convertir.place(relx=0.55,rely=0.6)

        #Añadimos botones play, stop y pause al final de la ejecución 
        self.play1 = ttk.Button(self.root, text='play')
        self.play1.place(relx=0.05, rely=0.86)
        self.pause1 = ttk.Button(self.root, text='pause')
        self.pause1.place(relx=0.12, rely=0.86)
        self.stop1 = ttk.Button(self.root, text='stop')
        self.stop1.place(relx=0.19, rely=0.86)

        self.play2 = ttk.Button(self.root, text='play')
        self.play2.place(relx=0.3, rely=0.86)
        self.pause2 = ttk.Button(self.root, text='pause')
        self.pause2.place(relx=0.37, rely=0.86)
        self.stop2 = ttk.Button(self.root, text='stop')
        self.stop2.place(relx=0.44, rely=0.86)

        self.play3 = ttk.Button(self.root, text='play')
        self.play3.place(relx=0.7, rely=0.86)
        self.pause3 = ttk.Button(self.root, text='pause')
        self.pause3.place(relx=0.76, rely=0.86)
        self.stop3 = ttk.Button(self.root, text='stop')
        self.stop3.place(relx=0.83, rely=0.86)

        """ 
        #Creamos un Frame para la cabecera
        self.topFrame =  Frame(self.root).pack(side='top', fill=Y, padx=0,pady=0)

        self.buttonAdd1 = ttk.Button(self.topFrame,
                                    text="+ Añadir vídeo LARGO",
                                    command=self.middleWindw.add_files,
                                    )
        self.buttonAdd1.pack(side="left",pady=50,padx=100,anchor=N)
        self.buttonAdd1.config()
        #self.buttonAdd2.pack(padx=100, pady=0)
        
        self.buttonDel1 = ttk.Button(self.topFrame,
                                    text="- Borrar vídeo LARGO",
                                    ).pack(side="left",pady=50,padx=50,anchor=N)

        self.buttonAdd2 = ttk.Button(self.topFrame,
                                          text="+ Añadir vídeo CORTO",
                                          ).pack(side="left",pady=50,padx=50,anchor=N)
        
        self.buttonDel2 = ttk.Button(self.topFrame,
                                    text="- Borrar vídeo CORTO",
                                    ).pack(side="left",pady=50,padx=50,anchor=N)

        #Creamos las label donde irán los vídeos
        #Creamos otro Frame
        self.videoFrame =  Frame(self.root).pack(side='top', fill=Y, padx=0,pady=50)
        self.showFile1 = ttk.Label(self.videoFrame)
        self.showFile1.place(x=100, y=100, width=500, height=300)
        self.showFile2 = ttk.Label(self.videoFrame).place(x=700, y=100, width=500, height=300)

        #Creamos otro para los botones 
        self.playPhoto = PhotoImage(file='button_play.png',height=50,width=50)
        self.playFile1 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="play").place(x=625, y=200, width=70)
        self.playFile2 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="play").place(x=1225, y=200, width=70)

        self.pauseFile1 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="pause").place(x=625, y=250, width=70)  

        self.pauseFile2 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="pause").place(x=1225, y=250, width=70)         
        
        self.stopFile1 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="pause").place(x=625, y=300, width=70)  

        self.stopFile2 = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="pause").place(x=1225, y=300, width=70)       

        #Vamos a hacer otro cuadro para el resultado
        self.showFile3 = ttk.Label(self.videoFrame,text="algoo").place(x=400, y=450, width=500, height=300)    
        #un botón para que haga el recorte
        self.cutVideo = ttk.Button(self.videoFrame,
                                    compound="c", 
                                    #image=self.playPhoto,
                                    text="cut").place(x=200, y=600, width=70)           
        """
        self.root.mainloop()

if __name__ == '__main__':
    Window()
