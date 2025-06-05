import tkinter as tk
from tkinter import ttk, messagebox
from forms.login.form_login_designer import FormLoginDesigner
from persistence.model import Auth_User
import util.encoding_decoding as end_dec
from persistence.repository.auth_user_repository import AuthUserRepository
from forms.signin.form import FormRegister


class FormLogin(FormLoginDesigner):
    
    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()
    
    def verificar(self):
        user_db: Auth_User = self.auth_repository.getUserByUserName(
            self.usuario.get())
        if(self.isUser(user_db)):
            self.isPassword(self.password.get(), user_db)
            
    def userRegister(self):
        # import tkinter as tk
        # ventana = tk.Toplevel()
        # form_register = FormRegister()
        # form_register.pack(fill='both', expand=True)
        # ventana.mainloop()    
        FormRegister().mainloop()
        
    def isUser(self, user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe, por favor registrese", title= "Error")
        return status
    
    def isPassword(self, password: str, user: Auth_User):
        from forms.master.form_master import MasterPanel  # Importar aquí dentro para evitar ciclo
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(
                message="La contraseñas es incorrecta", title="Error")
