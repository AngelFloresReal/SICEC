from cryptography.fernet import Fernet

def encrypted(password: str):   
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii') 
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')

print(encrypted("admin123"))
