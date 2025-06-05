import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from forms.login.form_login import FormLogin

class MasterPanel:
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('SICEC ')

        self.ventana.config(bg='#ffffff')          
        self.ventana.state('zoomed')
        self.ventana.resizable(width=1, height=1)
        self.ventana.minsize(width=800, height=600)
        
        # Crear el header
        self.crear_header()
        
        # Contenido principal
        logo = utl.leer_imagen("./src/assets/img/logo.png", (200, 200))                
        label = tk.Label(self.ventana, image=logo, bg='#ffffff')
        label.place(x=0, y=50, relwidth=1, relheight=0.9)

        self.ventana.mainloop()
    
    def crear_header(self):
        # Frame para el header
        header_frame = tk.Frame(self.ventana, bg="#EBEBF2", height=50)
        header_frame.pack(side="top", fill="x")
        
        # Título de la aplicación en el header
        titulo = tk.Label(
            header_frame, 
            text="¡Bienvenido a SICEC!", 
            font=("Arial", 14, BOLD),
            bg="#536FB5",
            fg="white"
        )
        titulo.pack(side="left", padx=20)
        
        # Botón de cerrar sesión en el header
        logout_button = tk.Button(
            header_frame,
            text="Cerrar sesión",
            font=("Arial", 12, BOLD),
            bg="#346C8A",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=10,
            command=self.logout
        )
        # Efecto hover para el botón
        logout_button.bind("<Enter>", lambda e: logout_button.config(bg="#346C8A"))
        # logout_button.bind("<Leave>", lambda e: logout_button.config(bg="#3A4F7F"))
        logout_button.pack(side="right", padx=20, pady=5)

    def logout(self):
        self.ventana.destroy()
        FormLogin()