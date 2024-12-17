from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(50), nullable=True)

    def __init__(self, username, email, country):
        self.username = username
        self.email = email
        self.country = country

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Necesarios para Flask-Login
    @property
    def is_active(self):
        # Aquí puedes personalizar el comportamiento de la cuenta activa
        return True  # Por defecto, los usuarios están activos

    @property
    def is_authenticated(self):
        return True  # Los usuarios autenticados siempre devuelven True

    @property
    def is_anonymous(self):
        return False  # Los usuarios no son anónimos

    def get_id(self):
        return str(self.id)  # Flask-Login requiere un método get_id que devuelva el ID del usuario como una cadena



"""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
"""
