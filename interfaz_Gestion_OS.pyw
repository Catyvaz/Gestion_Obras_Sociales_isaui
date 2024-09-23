from tkinter import *
from tkinter import ttk
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

        contenedor_buscado = Frame(contenedor_todo, width= 950, height= 200, bg= "Gray62")
        contenedor_buscado.pack(pady=20, padx= 20)
        contenedor_buscado.pack_propagate(False)

        Label(contenedor_buscado, text="Gestión de Obras Sociales", bg= "Black", font= ("Times New Roman", 24, "bold"), justify=CENTER, fg= "White" ).grid(row=0, columnspan=4, padx= 30, pady= 10)
        self.buscador_OS = Entry(contenedor_buscado, width= 40, font= ("Times New Roman", 15))
        self.buscador_OS.grid(row= 1, column= 0, columnspan= 2, ipady= 6, padx= 20, pady= 15)
        self.btn_buscar = Button(contenedor_buscado, text="Buscar", font= ("Times New Roman", 10, "bold"), justify= CENTER)
        self.btn_buscar.grid(row= 1, column=2, ipady= 6, padx= 15, pady= 15)
        self.btn_agregar = Button(contenedor_buscado, text= "AGREGAR +", font= ("Times New Roman", 10, "bold"), justify= CENTER)
        self.btn_agregar.grid(row= 1, column=3, ipady= 6, padx= 15, pady= 15)

        contenedor_lista = Frame(contenedor_todo, width= 950, height= 200, bg= "Gray62")
        contenedor_lista.pack(pady=20, padx= 20, ipadx= 25, ipady= 25)

        self.lista_OS = ttk.Treeview(contenedor_lista, columns=("nombre", "cuit"))
        self.lista_OS.column("#0", width = 100, stretch = False)
        self.lista_OS.column("nombre", width = 100, stretch = False)
        self.lista_OS.column("cuit", width = 100, stretch = False)

        self.lista_OS.heading("#0", text = "Alias", anchor = CENTER)
        self.lista_OS.heading("nombre", text = "Nombre", anchor = CENTER)
        self.lista_OS.heading("cuit", text = "Cuit", anchor = CENTER)

        self.lista_OS.pack(pady= 20)

ventana = Tk()
ventana.wm_title("Gestión Obra Social")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()