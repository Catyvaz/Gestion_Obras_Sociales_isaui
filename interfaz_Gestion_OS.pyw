from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Gestion_Obra_Social(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="#e4c09f", height= 600, width=1200)
        self.master = master
        self.pack_propagate(False)
        self.pack(expand=True)
        self.createWidgets()

    def createWidgets(self):
        contenedor_total = Frame(self, padx=10, pady=10, bg="#c9c2b2")
        contenedor_total.pack()

        #primer frame, contiene la imagen y el titulo de la ventana
        contenedor_titulo = Frame(contenedor_total, bg="#c9c2b2")
        contenedor_titulo.pack()

        # Cargar la imagen de fondo
        img_fondo = Image.open("fondo3.png")
        img_fondo = img_fondo.resize((1000, 100), Image.Resampling.LANCZOS)
        self.img_fondo = ImageTk.PhotoImage(img_fondo)

        # Crear un Label para la imagen de fondo
        fondo_label = Label(contenedor_titulo, image=self.img_fondo)
        fondo_label.pack(expand=True, fill="both")

        # Crear un Label para el texto y colocarlo encima del Label de la imagen
        texto_label = Label(contenedor_titulo, text="Gestión de Obras Sociales", font=("Robot", 25), bg="Black", fg="White")
        texto_label.place(relx=0.5, rely=0.5, anchor="center")

        #segundo frame, contiene el buscador y el boton de agregar
        #buscador de os
        frame_busqueda = Frame(contenedor_total, bg="#e6c885")
        frame_busqueda.pack(fill= "x")
        frame_busqueda.columnconfigure(4, weight=1)

        #Widgets de búsqueda dentro del frame más chico
        Label(frame_busqueda, text="Buscar:", bg="#e6c885",font=("Robot",15)).grid(row=1, column=1, padx=5, pady=5, sticky= W)

        self.entrada_buscar = Entry(frame_busqueda,width="50",font=("Robot",13))
        self.entrada_buscar.grid(row=1, column=2, padx=5, pady=5, sticky= W)

        img_buscar = Image.open("buscar1.png").resize((30, 30), Image.Resampling.LANCZOS)
        img_buscar = ImageTk.PhotoImage(img_buscar)
        btn_buscar = Button(frame_busqueda, image=img_buscar, width=30, height=30,bg="#e6c885")
        btn_buscar.grid(row=1, column=3, sticky= W)
        btn_buscar.image = img_buscar

        boton_agregar = Button(frame_busqueda, text="Agregar   +", width=15, bg="chartreuse3", activebackground="chartreuse4", font=("Robot",15))
        boton_agregar.grid(row=1, column=5, padx=10, pady=10, sticky= E)


        #Tercer frame, contiene la tabla de OS
        #Frame para el Treeview y el scrollbar
        frame_tabla = Frame(contenedor_total, bg="#c9c2b2", height= 300, width= 1000)  # Frame para contener la tabla y el scrollbar
        frame_tabla.pack(expand=True)
        
        stilo = ttk.Style()
        stilo.configure("Treeview", font=("Robot",11), rowheight=25)  # Cambia la fuente y el alto de las filas
        stilo.configure("Treeview.Heading", font=("Robot",14))  # Cambia la fuente de las cabeceras
        
        #Treeview para mostrar la tabla de tratamientos dentro del frame_tabla
        self.tree = ttk.Treeview(frame_tabla, columns=("Siglas", "Nombre", "CUIT"), show='headings', height=5)
        self.tree.grid(row=0, column=0, sticky="nsew")

        #Títulos de columnas
        self.tree.heading("Siglas", text="Siglas")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("CUIT", text="CUIT")

        #Ancho de las columnas y datos centrados
        self.tree.column("Siglas", anchor='center', width=250)
        self.tree.column("Nombre", anchor='center', width=350)
        self.tree.column("CUIT", anchor='center', width=250)

        """
        #Ejemplo
        self.tree.insert("", "end", values=("1234", "Tratamiento 1", "$100"))
        self.tree.insert("", "end", values=("5678", "Tratamiento 2", "$150"))
        self.tree.insert("", "end", values=("91011", "Tratamiento 3", "$200"))
        """

        #Scrollbar para la tabla dentro del frame_tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')  #Se expande desde arriba hacia abajo
        self.tree.configure(yscrollcommand=scrollbar.set)

        #Cuarto frame, contiene los botones de ver, modificar y eliminar
        frame_btn = Frame(contenedor_total)
        frame_btn.pack()

        #Botones(ver, modificar, eliminar)
        btn_ver = Button(frame_btn, text="Ver", width=15, font=("Robot",15),bg="#e6c885")
        btn_ver.grid(row=0, column=1,padx=50)

        btn_editar = Button(frame_btn, text="Modificar", width=15, font=("Robot",15),bg="#e6c885")
        btn_editar.grid(row=0, column=2,padx=50)
        
        btn_eliminar = Button(frame_btn, text="Eliminar", width=15,font=("Robot",15),bg="#e6c885")
        btn_eliminar.grid(row=0, column=3, padx=50)

        """

        #Para que siempre esté atrás de los widgets
        fondo_label.lower()

        

    def agregar_OS(self):
        ventana_agregar = Toplevel(self)
        ventana_agregar.title("Agregar Tratamiento")
        ventana_agregar.config(bg="#e4c09f") 
        ventana.resizable(False,False)

        frame_agregar = LabelFrame(ventana_agregar, text="Agregar Nuevo Tratamiento", font= ("Robot", 12),padx=10, pady=10, bg="#c9c2b2")
        frame_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        campos = ["Código", "Procedimiento", "Precio", "Tipo", "Siglas", "Descripción completa"]
        entradas = {}

        for i, campo in enumerate(campos):     #Devuelve índice y valor de cada elemento 
            etiquetas = Label(frame_agregar, text=campo + ":", bg="#c9c2b2", font=("Robot", 10))
            etiquetas.grid(row=i, column=0, padx=10, pady=5)
            entry = Entry(frame_agregar, width=40, font=("Robot", 10))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entradas[campo] = entry

        btn_nuevo_tratamiento = Button(frame_agregar, text="Agregar", font=("Robot", 10),bg="#e6c885", command=lambda: self.guardar_nuevo_tratamiento(entradas, ventana_agregar))
        btn_nuevo_tratamiento.grid(row=len(campos), column=0, columnspan=2, padx=10, pady=10)

    def ver_tratamiento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, seleccione un tratamiento.")
            return
        
        tratamiento_seleccionado = self.tree.item(seleccion[0], 'values')   #Item= valor del elemento
        self.abrir_ventana_tratamiento(tratamiento_seleccionado,seleccion[0],modo="ver")

    def modificar_tratamiento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, seleccione un tratamiento.")
            return
        
        tratamiento_seleccionado = self.tree.item(seleccion[0], 'values')
        self.abrir_ventana_tratamiento(tratamiento_seleccionado, seleccion[0],modo="modificar")    
    
    def abrir_ventana_tratamiento(self, tratamiento, id_seleccionado, modo="ver"):
        ventana = Toplevel(self)
        ventana.title("Detalles del Tratamiento")
        ventana.config(bg="#e4c09f")
        ventana.resizable(False,False)
        ventana.geometry("510x345+400+160")
        
        ventana.grid_columnconfigure(0, weight=1)
        ventana.grid_rowconfigure(0, weight=1)

        frame_detalles = LabelFrame(ventana, text="Detalles del Tratamiento", font=("Robot", 10), padx=10, pady=10, bg="#c9c2b2")
        frame_detalles.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        campos = ["Código", "Procedimiento", "Precio", "Tipo", "Siglas", "Descripción completa"]
        valores = list(tratamiento) + ["Tipo Ejemplo", "Siglas Ejemplo", "Descripción del tratamiento"]  #ejemplo
        entradas ={}

        for i, campo in enumerate(campos):
            etiqueta = Label(frame_detalles, text=campo + ":", bg="#c9c2b2", font=("Robot", 10))
            etiqueta.grid(row=i, column=0, padx=10, pady=5)
            entry = Entry(frame_detalles, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, valores[i])
            entradas[campo] = entry
            

            if modo == "ver":
                entry.config(state="readonly")
                btn_editar = Button(ventana, text="Modificar", width=15, font=("Robot", 13), bg="#e6c885",
                                    command=lambda: self.activar_edicion(entradas, btn_guardar))
                btn_editar.grid(row=len(campos), column=0, pady=10)

    
                btn_guardar = Button(frame_detalles, text="Guardar Cambios", command=lambda: self.guardar_cambios(entradas, ventana))
                btn_guardar.grid(row=len(campos), column=0, columnspan=2, padx=10, pady=10)
                btn_guardar.config(state="disabled")  # Iniciar como deshabilitado
                                

        if modo == "modificar":
            btn_modificar = Button(frame_detalles, text="Guardar Cambios", command=lambda: self.guardar_cambios(entradas, ventana, id_seleccionado))
            btn_modificar.grid(row=len(campos), column=0, columnspan=2, padx=10, pady=10)

    def activar_edicion(self, entradas, btn_guardar):
    # Habilitar la edición en las entradas
        for entry in entradas.values():
            entry.config(state="normal")  # Permitir edición en todos los Entry
        
        # Activar el botón "Guardar Cambios"
        btn_guardar.config(state="normal")  # Activar el botón directamente

    def guardar_cambios(self, entradas, ventana,seleccion):
        #base de datos
        #messagebox.showinfo("Información", "Cambios guardados correctamente.")# Obtener los nuevos valores de todas las entradas
        nuevos_valores = {campo: entradas[campo].get() for campo in entradas}
        self.tree.item(seleccion, values=list(nuevos_valores.values()))
        
        # Mostrar mensaje de confirmación
        messagebox.showinfo("Información", "Cambios guardados correctamente.")
        
        # Cerrar la ventana después de guardar
        ventana.destroy()

    def eliminar_tratamiento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, seleccione un tratamiento para eliminar.")
            return
        #Pregunta al usuario si está seguro de eliminar 
        respuesta = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar el tratamiento seleccionado?")
        if respuesta:  
            self.tree.delete(seleccion)
            messagebox.showinfo("Atención", "Tratamiento eliminado correctamente.")
        else:
            messagebox.showinfo("Atención", "Eliminación cancelada.")

    def agregar_OS(self):
        ventana_agregar = Toplevel(self)
        ventana_agregar.title("Agregar Tratamiento")
        ventana_agregar.config(bg="#e4c09f")
        ventana.resizable(False,False)
        
        frame_agregar = LabelFrame(ventana_agregar, text="Agregar Nuevo Tratamiento", font= ("Robot", 11),padx=10, pady=10, bg="#c9c2b2")
        frame_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        campos = ["Código", "Procedimiento", "Precio", "Tipo", "Siglas", "Descripción completa"]
        entradas = {}

        for i, campo in enumerate(campos):
            etiquetas = Label(frame_agregar, text=campo + ":", bg="#c9c2b2", font=("Robot", 10))
            etiquetas.grid(row=i, column=0, padx=10, pady=5)
            entry = Entry(frame_agregar, width=40, font=("Robot", 10))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entradas[campo] = entry

        btn_nuevo_tratamiento = Button(frame_agregar, text="Agregar", font=("Robot", 10),bg="#e6c885", command=lambda: self.guardar_nuevo_tratamiento(entradas, ventana_agregar))
        btn_nuevo_tratamiento.grid(row=len(campos), column=0, columnspan=2, padx=10, pady=10)

    def guardar_nuevo_tratamiento(self, entry, ventana):
        codigo = entry["Código"].get()      #Obtenemos los valores que el usuario ingresó.
        procedimiento = entry["Procedimiento"].get()
        precio = entry["Precio"].get()
        tipo = entry["Tipo"].get()
        siglas = entry["Siglas"].get()
        descripcion = entry["Descripción completa"].get()
        # Validar datos y agregar al Treeview
        if codigo and procedimiento and precio and tipo and siglas and descripcion:
            self.tree.insert("", "end", values=(codigo, procedimiento, precio))
            messagebox.showinfo("Información", "Tratamiento agregado correctamente.")
            ventana.destroy()
        else:
            messagebox.showwarning("Atención", "Complete todos los campos.")

    def buscar_tratamiento(self):
        busqueda = self.entrada_buscar.get().strip().lower()
        tratamiento_encontrado = False
    
        if not busqueda:
            self.tree.delete(*self.tree.get_children())
            self.cargar_tratamiento()
        #Obtenemos búsqueda
        for item in self.tree.get_children():         #Recorre cada fila usando identificador en la lista devuelta por children
            valores = self.tree.item(item, 'values')  #Obtiene los valores de las columnas de la fila correspondiente al identificador item.
            codigo = valores[0].lower()
            procedimiento = valores[1].lower()
            if busqueda in codigo or busqueda in procedimiento:
                self.tree.selection_set(item)         #Selecciona el tratamiento.
                self.tree.see(item)                   #Hace visible el tratamiento.
                tratamiento_encontrado = True
            else:
                self.tree.detach(item)                #Oculta los otros tratamientos
            
        if not tratamiento_encontrado:
            #self.tree.delete(*self.tree.get_children())
            #self.cargar_tratamiento()
            messagebox.showwarning("Atención", "No se encontró el tratamiento.")

    def cargar_tratamiento(self):
        self.tree.insert("", "end", values=("1234", "Tratamiento 1", "$100"))
        self.tree.insert("", "end", values=("5678", "Tratamiento 2", "$150"))
        self.tree.insert("", "end", values=("91011", "Tratamiento 3", "$200"))
        """

ventana = Tk()
ventana.title("Gestion de Tratamientos")
ventana.resizable(False,False)
ventana.geometry("+60+55")
root = Gestion_Obra_Social(ventana)
ventana.mainloop()