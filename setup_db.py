# setup_db.py
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    print("Intentando crear la base de datos...")
    db.create_all()
    print("Base de datos creada exitosamente")
