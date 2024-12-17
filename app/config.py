import os

class Config:
    SECRET_KEY = 'tu_clave_secreta'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # Para ver las consultas SQL

"""
# app/config.py
import os

class Config:
    SECRET_KEY = 'tu_clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # Verifica que la ruta sea correcta
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""


