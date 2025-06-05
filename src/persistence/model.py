from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Auth_User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))
    surname = Column(String(150))
    username = Column(String(150))
    password = Column(String(150))
    role = Column(Integer)