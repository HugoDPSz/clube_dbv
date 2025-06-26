from app.models import db
from datetime import datetime
from .desbravador_especialidade import DesbravadorEspecialidade

class Desbravador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    unidade_id = db.Column(db.Integer, db.ForeignKey('unidade.id'))
    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'))

    especialidades_conquistadas = db.relationship('DesbravadorEspecialidade', back_populates='desbravador')
    mensalidades = db.relationship("Mensalidade", back_populates="desbravador")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime('%Y-%m-%d'),
            "unidade_id": self.unidade_id,
            "classe_id": self.classe_id
        }