from datetime import date
from app.models import db

class Caixa(db.Model):
    __tablename__ = "caixa"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, default=date.today)
    tipo = db.Column(db.String(10))  # entrada ou saida
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200))

    def to_dict(self):
        return {
            "id": self.id,
            "data": self.data.isoformat(),
            "tipo": self.tipo,
            "valor": self.valor,
            "descricao": self.descricao,
        }