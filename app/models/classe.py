from app.models import db

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    desbravadores = db.relationship('Desbravador', backref='classe')

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }