from flask import Blueprint, flash, render_template, redirect, url_for, request
from app.models import db  # Importamos db desde app.models, no desde app
from app.models import User  # Importamos el modelo User de app.models
from flask_login import login_required, logout_user, login_user, current_user

main = Blueprint('main', __name__)

# Usamos el login_manager que ya está definido en __init__.py
# @login_manager.user_loader ya está definido en __init__.py, no es necesario definirlo aquí

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']

        # Verificar si el usuario ya existe
        user = User.query.filter_by(username=username).first()
        if user:
            flash('El nombre de usuario ya existe. Por favor, elige otro.', 'error')
            return redirect(url_for('main.register'))  # Usamos 'main.register' ya que es el Blueprint

        # Crear nuevo usuario
        new_user = User(username=username, email=email, country=country)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('main.login'))  # Redirigir a login después del registro exitoso
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrió un error: {str(e)}', 'error')
            return redirect(url_for('main.register'))  # Usamos 'main.register'

    return render_template('register.html')



@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Has iniciado sesión exitosamente.", "success")
            return redirect(url_for('main.index'))  # Redirige a la página principal
        else:
            flash("Nombre de usuario o contraseña incorrectos.", "error")
            return redirect(url_for('main.login'))
    
    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión.", "success")
    return redirect(url_for('main.login'))

@main.route('/')
@login_required
def index():
    return render_template('main.html')


"""
@main.route('/')
def home():
    return "Página de inicio cargada correctamente"

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica para el login
        return redirect(url_for('main.home'))  # Redirige al home después de login
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        country = request.form.get('country')

        if not email:
            flash("El correo electrónico es obligatorio.", "error")
            return redirect(url_for('main.register'))

        # Crear el nuevo usuario
        new_user = User(username=username, email=email, country=country)
        new_user.set_password(password)

        # Agregar y guardar el usuario en la base de datos
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error al registrar el usuario: {e}", "error")
            return redirect(url_for('main.register'))

    return render_template('register.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']

        # Crear un nuevo usuario
        new_user = User(username=username, email =email,password_hash=password, country=country)

        db.session.add(new_user)
        db.session.commit()  # Guarda el usuario en la base de datos

        return redirect(url_for('main.login'))  # Redirige a login después del registro

    return render_template('register.html')



from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        country = request.form.get('country')

        # Validar si el usuario ya existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre de usuario ya está en uso. Por favor elige otro.')
            return redirect(url_for('main.register'))

        # Crear nuevo usuario y cifrar la contraseña
        new_user = User(username=username, country=country)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Buscar al usuario por nombre de usuario
        user = User.query.filter_by(username=username).first()

        # Verificar si el usuario existe y si la contraseña es correcta
        if user and user.check_password(password):
            flash('Inicio de sesión exitoso. ¡Bienvenido!')
            return redirect(url_for('main.home'))
        else:
            flash('Nombre de usuario o contraseña incorrectos. Intenta nuevamente.')
            return redirect(url_for('main.login'))

    return render_template('login.html')



from flask import Blueprint, render_template, request
from app.models import db, User  # Importa db y User para interactuar con la base de datos

# Crear el blueprint
main = Blueprint('main', __name__)



@main.route('/')
def home():
    print("Página de inicio cargada")
    return 'Página de inicio cargada correctamente'

@main.route('/register', methods=['GET', 'POST'])
def register():
    print("Ruta de registro cargada")
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    print("Ruta de login cargada")
    return render_template('login.html')
"""




