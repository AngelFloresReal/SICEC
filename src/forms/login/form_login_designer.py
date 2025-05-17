from tkinter import ttk
from tkinter.font import BOLD, NORMAL
import tkinter as tk
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

        logo = utl.leer_imagen("./src/assets/img/logo.jpeg", (200, 200))

        # Crear un contenedor principal para centrar todo
        contenedor_principal = tk.Frame(self.ventana, bg="#ffffff")
        contenedor_principal.place(relx=0.5, rely=0.5, anchor="center")

        # Ancho del 60% de la ventana (800 * 0.6 = 480)
        ancho_contenedor = 480
        
        contenedor = tk.Frame(contenedor_principal, bg="#ffffff", width=ancho_contenedor)
        contenedor.pack()

        titulo = tk.Label(contenedor, text="SICEC", font=('Arial', 30, 'bold'), fg="#000000", bg="#ffffff")
        titulo.pack(pady=(0, 20))

        label_logo = tk.Label(contenedor, image=logo, bg="#ffffff")
        label_logo.image = logo
        label_logo.pack(pady=(0, 20))

        # Estilo visual para Entry
        style = ttk.Style()
        style.configure("TEntry", padding=10, relief="flat", font=('Arial', 14, 'bold'))
        style.map("TEntry",
            focusbackground=[('focus', '#cccccc')],
            fieldbackground=[('!disabled', 'white')],
        )
        
        # Estilo personalizado para inputs redondeados (usando un marco contenedor)
        class RoundedEntry(tk.Frame):
            def __init__(self, parent, *args, **kwargs):
                tk.Frame.__init__(self, parent, bg='#ffffff', highlightbackground="#536FB5", 
                                 highlightcolor="#536FB5", highlightthickness=2, bd=0)
                self.radius = 15  # Radio de la esquina
                
                # Crear el widget Entry dentro del frame
                self.entry = ttk.Entry(self, *args, **kwargs)
                self.entry.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                
                # Configurar bordes redondeados
                self.config(borderwidth=0, relief="flat")
                self.bind("<Configure>", self._on_configure)
                
            def _on_configure(self, event):
                # Este método se activa cuando el widget cambia de tamaño
                pass
                
            def get(self):
                return self.entry.get()
                
            def insert(self, index, string):
                self.entry.insert(index, string)
                
            def delete(self, first, last=None):
                self.entry.delete(first, last)
                
            def bind(self, sequence, func, add=None):
                self.entry.bind(sequence, func, add)

        # Frame para contener los controles con ancho fijo
        controles_frame = tk.Frame(contenedor, bg="#ffffff", width=ancho_contenedor)
        controles_frame.pack(fill=tk.X)
        controles_frame.pack_propagate(False)  # Impide que el frame se redimensione automáticamente

        # Campo usuario con placeholder
        usuario_frame = RoundedEntry(controles_frame)
        self.usuario = usuario_frame.entry
        self.usuario.insert(0, "Usuario")
        self.usuario.bind("<FocusIn>", lambda e: self._clear_placeholder(e, "Usuario"))
        self.usuario.bind("<FocusOut>", lambda e: self._add_placeholder(e, "Usuario"))
        usuario_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

        # Campo contraseña con placeholder
        password_frame = RoundedEntry(controles_frame)
        self.password = password_frame.entry
        self.password.insert(0, "Contraseña")
        self.password.bind("<FocusIn>", lambda e: self._clear_placeholder(e, "Contraseña", is_password=True))
        self.password.bind("<FocusOut>", lambda e: self._add_placeholder(e, "Contraseña", is_password=True))
        password_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

        # Botón Iniciar sesión con esquinas redondeadas
        def create_rounded_button(parent, text, command, bg_color="#536FB5", fg_color="white"):
            button_frame = tk.Frame(parent, bg="#ffffff")
            button_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
            
            # Crear botón personalizado con esquinas redondeadas
            button = tk.Button(
                button_frame, 
                text=text, 
                font=('Arial', 15, 'bold'), 
                bg=bg_color, 
                fg=fg_color,
                bd=0,
                relief="flat",
                command=command,
                highlightthickness=0,
                padx=20,
                pady=10,
                cursor="hand2"
            )
            button.pack(fill=tk.X)

            # Aplicar bordes redondeados (esto funciona solo en sistemas que soportan esta configuración)
            try:
                button.config(borderwidth=0, highlightthickness=0)
                button.bind("<Configure>", lambda e: button.config(relief="flat"))
                
                # Intentar aplicar esquinas redondeadas mediante ttk
                if 'win' in tk.TkVersion.__module__:  # En Windows
                    style = ttk.Style()
                    style.configure("Round.TButton", borderwidth=0, relief="flat")
                    button = ttk.Button(button_frame, style="Round.TButton", text=text, command=command)
                    button.pack(fill=tk.X)
            except:
                # Si falla, mantener el botón normal
                pass
                
            return button
            
        # Crear botón redondeado
        boton_login = create_rounded_button(controles_frame, "Iniciar sesión", self.verificar)

        # Establece el tamaño fijo para el frame de controles
        controles_frame.config(width=ancho_contenedor, height=150)

        self.ventana.bind("<Return>", lambda event: self.verificar())
        self.ventana.mainloop()

    def _clear_placeholder(self, event, placeholder, is_password=False):
        # Como ahora usamos un widget personalizado, accedemos al Entry interno
        if hasattr(event.widget, 'entry'):
            widget = event.widget.entry
        else:
            widget = event.widget
            
        if widget.get() == placeholder:
            widget.delete(0, tk.END)
            if is_password:
                widget.config(show="*")

    def _add_placeholder(self, event, placeholder, is_password=False):
        # Como ahora usamos un widget personalizado, accedemos al Entry interno
        if hasattr(event.widget, 'entry'):
            widget = event.widget.entry
        else:
            widget = event.widget
            
        if widget.get() == "":
            widget.insert(0, placeholder)
            if is_password:
                widget.config(show="")