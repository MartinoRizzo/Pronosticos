from flask import Flask
from app.routes import main  
from app.config import Config
from app.models import User, db
from flask_login import LoginManager

# Inicializar la aplicación Flask
app = Flask(__name__,template_folder='app/templates')
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Configura la ruta de login
login_manager.login_view = 'main.login'  # Especifica la vista de login

# Registra el 'user_loader' aquí
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Devuelve el usuario según el ID

# Registrar el blueprint
app.register_blueprint(main)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

