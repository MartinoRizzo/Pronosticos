from flask import Flask
from flask_login import LoginManager  # Asegúrate de importar LoginManager
from app.routes import main  # Importa el blueprint
from app.models import User, db  # Importa la base de datos
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuración de la app (archivo config.py)
    
    print("Aplicación Flask creada")  # Agregar esta línea para verificar que la app se crea

    db.init_app(app)  # Inicializa la base de datos con la app

    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'main.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    app.register_blueprint(main)

    print("Aplicación Flask configurada con LoginManager")  # Agregar esta línea

    return app




"""
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuración de la app (archivo config.py)

    db.init_app(app)  # Inicializa la base de datos con la app

    # Inicializar LoginManager **después** de crear la app
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Configura la ruta de inicio de sesión
    login_manager.login_view = 'main.login'

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    app.register_blueprint(main)  # Registra el blueprint

    return app
"""




"""
from flask import Flask
from app.config import Config
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuración de la app (archivo config.py)

    from app.models import db  # Importar aquí, después de crear la app

    db.init_app(app)  # Inicializa la base de datos con la app

      
 # Inicializar LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Configura la ruta de inicio de sesión
    login_manager.login_view = 'main.login'

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    from app.routes import main  # Importar routes después de db
    app.register_blueprint(main)  # Registra el blueprint



    return app


"""
"""
from flask import Flask
from app.routes import main # Importa el blueprint
from app.models import db   # Importa la base de datos  
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuración de la app (archivo config.py)

    db.init_app(app)  # Inicializa la base de datos con la app

    with app.app_context():
        db.create_all()  # Crea las tablas en la base de datos

    app.register_blueprint(main)  # Registra el blueprint

    return app
"""
