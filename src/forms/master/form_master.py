import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from forms.login.form_login import FormLogin

class MasterPanel:
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')

        self.ventana.config(bg='#ffffff')          
        self.ventana.state('zoomed')
        self.ventana.resizable(width=1, height=1)
        self.ventana.minsize(width=800, height=600)
        
        logo = utl.leer_imagen("./src/assets/img/logo.jpeg", (200, 200))                
        label = tk.Label(self.ventana, image=logo, bg='black')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        logout_button = tk.Button(
            self.ventana,
            text="Cerrar sesión",
            font=("Arial", 12, BOLD),
            bg="#d9534f",
            fg="white",
            command=self.logout
        )
        logout_button.pack(pady=20, anchor='ne', padx=20)

        self.ventana.mainloop()

    def logout(self):
        self.ventana.destroy()
        FormLogin()
