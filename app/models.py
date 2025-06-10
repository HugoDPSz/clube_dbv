from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Unidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desbravadores = db.relationship('Desbravador', backref='unidade')

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desbravadores = db.relationship('Desbravador', backref='classe')

class Desbravador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'))
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'))