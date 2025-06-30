from app.models import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False) # 'credit' ou 'debit'
    transaction_date = db.Column(db.Date, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    # Adicionando o vínculo direto com a mensalidade para rastreabilidade
    mensalidade_id = db.Column(db.Integer, db.ForeignKey('Mensalidade.id'), nullable=True)

    account = db.relationship('Account', backref='transactions')