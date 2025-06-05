import os
from forms.login.form_login import FormLogin
import build_db

db_path = os.path.join("src", "db", "login.sqlite")

if not os.path.exists(db_path):
    print("Base de datos no encontrada. Creando...")
    build_db.create_database()
    

FormLogin()