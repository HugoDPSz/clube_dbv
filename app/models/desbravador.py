from app.models import db
from datetime import datetime

class Desbravador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'))
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d'),
            "unidade_id": self.unidade_id,
            "classe_id": self.classe_id
        }