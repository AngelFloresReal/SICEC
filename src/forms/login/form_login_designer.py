import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormLoginDesigner:

    def verificar(self): 
        print("Verificando usuario...")

    def userRegister(self):
        print("Ir a registro...")

    def __init__(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Inicio de sesión')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#ffffff')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen("./src/assets/img/logo.png", (200, 200))

        # Crear un contenedor principal para centrar todo
        contenedor_principal = tk.Frame(self.ventana, bg="#ffffff")
        contenedor_principal.place(relx=0.5, rely=0.5, anchor="center")

        # Ancho del 60% de la ventana (800 * 0.6 = 480)
        ancho_contenedor = 480
        
        contenedor = tk.Frame(contenedor_principal, bg="#ffffff", width=ancho_contenedor)
        contenedor.pack()

        titulo = tk.Label(contenedor, text="SICEC", font=('Arial', 30, BOLD), fg="#000000", bg="#ffffff")
        titulo.pack(pady=(0, 20))

        label_logo = tk.Label(contenedor, image=logo, bg="#ffffff")
        label_logo.image = logo
        label_logo.pack(pady=(0, 20))

        # Estilo visual para Entry
        style = ttk.Style()
        style.configure("TEntry", padding=10, relief="flat", font=('Arial', 14))
        style.map("TEntry",
            focusbackground=[('focus', '#cccccc')],
            fieldbackground=[('!disabled', 'white')],
        )

        # Frame para contener los controles con ancho fijo
        controles_frame = tk.Frame(contenedor, bg="#ffffff", width=ancho_contenedor)
        controles_frame.pack(fill=tk.X)
        controles_frame.pack_propagate(False)  # Impide que el frame se redimensione automáticamente

        # Campo usuario con placeholder
        self.usuario = ttk.Entry(controles_frame, style="TEntry")
        self.usuario.insert(0, "Usuario")
        self.usuario.bind("<FocusIn>", lambda e: self._clear_placeholder(e, "Usuario"))
        self.usuario.bind("<FocusOut>", lambda e: self._add_placeholder(e, "Usuario"))
        self.usuario.pack(fill=tk.X, padx=20, pady=(0, 10))

        # Campo contraseña con placeholder
        self.password = ttk.Entry(controles_frame, style="TEntry")
        self.password.insert(0, "Contraseña")
        self.password.bind("<FocusIn>", lambda e: self._clear_placeholder(e, "Contraseña", is_password=True))
        self.password.bind("<FocusOut>", lambda e: self._add_placeholder(e, "Contraseña", is_password=True))
        self.password.pack(fill=tk.X, padx=20, pady=(0, 20))

        # Botón Iniciar sesión
        boton_login = tk.Button(controles_frame, text="Iniciar sesión", font=('Arial', 15, BOLD), bg='#536FB5', fg='white', bd=0, command=self.verificar)
        boton_login.pack(fill=tk.X, padx=20, pady=(0, 10))

        # Establece el tamaño fijo para el frame de controles
        controles_frame.config(width=ancho_contenedor, height=150)

        self.ventana.bind("<Return>", lambda event: self.verificar())
        self.ventana.mainloop()

    def _clear_placeholder(self, event, placeholder, is_password=False):
        widget = event.widget
        if widget.get() == placeholder:
            widget.delete(0, tk.END)
            if is_password:
                widget.config(show="*")

    def _add_placeholder(self, event, placeholder, is_password=False):
        widget = event.widget
        if widget.get() == "":
            widget.insert(0, placeholder)
            if is_password:
                widget.config(show="")