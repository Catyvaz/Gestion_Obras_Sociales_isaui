from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 


class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 1100, height = 600, bg = "#E4C09F")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.contendor()

    def contendor(self):
        contenedor_todo = Frame(self, width= 1000, height= 500, bg= "#818181")
        contenedor_todo.pack(expand= True, ipadx= 10, ipady= 10)
        contenedor_todo.pack_propagate(False)

        contenedor_buscado = Frame(contenedor_todo, width= 9500, height= 200, bg= "Gray62")
        contenedor_buscado.pack(pady=20, padx= 20)
        contenedor_buscado.pack_propagate(False)

        img_buscar = imagen.opne

        Label(contenedor_buscado, text="Gestión de Obras Sociales", bg= "Black", font= ("Times New Roman", 24, "bold"), justify=CENTER, fg= "White" ).grid(row=0, columnspan=3, padx= 30, pady= 10)
        self.buscador_OS = Entry(contenedor_buscado, width= 40, font= ("Times New Roman", 15))
        self.buscador_OS.grid(row= 1, column= 0, columnspan= 2, ipady= 6, padx= 20, pady= 15)
        self.btn_buscar = Button(contenedor_buscado, )
        self.btn_agregar = Button(contenedor_buscado, text= "AGREGAR +", font= ("Times New Roman", 10, "bold"), justify= CENTER)
        self.btn_agregar.grid(row= 1, column=2, ipady= 6, padx= 15, pady= 15)

ventana = Tk()
ventana.wm_title("Gestión Obra Social")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()