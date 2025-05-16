import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

class FormSigninDesigner:
    def verificar(self): 
        pass
    def userRegister(self):
        pass
    def register():
        pass
    
    def __init__(self):
        self.ventana = tk.Toplevel()                             
        self.ventana.title('Registro de usuario')
        self.ventana.config(bg='#ffffff')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 600, 480)
        
        logo = utl.leer_imagen("./src/assets/img/logo.jpeg", (200, 200))
        
        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=10, pady=0, bg='#000000')
        frame_logo.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo,bg='#000000')
        label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        # frame_form_top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text="Registrarse", font=('Arial', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)
        
        # end frame_form_top
        
        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        
        # inputs
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Arial', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Arial', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*") 
        
        etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmacion", font=(
            'Arial', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fill, font=('Arial', 14))
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        self.confirmation.config(show="*")
        
        # button
        register = tk.Button(frame_form_fill, text="Registrar",font=('Arial', 15,BOLD),bg='red', bd=0,fg="#fff",command=self.register)
        register.pack(fill=tk.X, padx=20,pady=20)
        
        # logic    
        register.bind("<Return>", (lambda event: self.register()))
        #end frame_form_fill
        
        self.ventana.mainloop()
