from datetime import date
from app.models import db

class Mensalidade(db.Model):
    __tablename__ = 'Mensalidade'
    id = db.Column(db.Integer, primary_key=True)
    desbravador_id = db.Column(db.Integer, db.ForeignKey('desbravador.id'))
    mes_referencia = db.Column(db.String(7), nullable=False) #YYYY-MM
    valor = db.Column(db.Float, nullable=False)
    pago = db.Column(db.Boolean, default=False)
    data_pagamento = db.Column(db.Date)

    desbravador = db.relationship("Desbravador", back_populates="mensalidades")

    def to_dict(self):
        return {
            "id": self.id,
            "desbravador_id": self.desbravador_id,
            "mes_referencia": self.mes_referencia,
            "valor": self.valor,
            "pago": self.pago,
            "data_pagamento": self.data_pagamento.isoformat() if self.data_pagamento else None,
        }