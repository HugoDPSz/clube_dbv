from app.models import db
from datetime import datetime

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # Tipos: 'Ativo', 'Passivo', 'Patrimônio Líquido', 'Receita', 'Despesa'
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    transactions = db.relationship('Transaction', backref='account', lazy=True)

    def __repr__(self):
        return f'<Account {self.name}>'