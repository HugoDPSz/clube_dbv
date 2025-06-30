from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from .routes import desbravador, unidade, classe, especialidade, desbravador_especialidade, mensalidade
        app.register_blueprint(desbravador.bp_desbravador)
        app.register_blueprint(unidade.bp_unidade)
        app.register_blueprint(classe.bp_classe)
        app.register_blueprint(especialidade.bp_especialidade)
        app.register_blueprint(desbravador_especialidade.bp_conquistas)  
        app.register_blueprint(mensalidade.bp_mensalidade) 
        
        db.create_all()
    return app