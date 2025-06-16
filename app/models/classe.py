from app.models import db

classe_especialidade = db.Table(
    'classe_especialidade',
    db.Column('classe_id', db.Integer, db.ForeignKey('classe.id'), primary_key= True),
    db.Column('especialidade_id', db.Integer, db.ForeignKey('especialidade.id'), primary_key= True)
)

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    especialidades_obrigatorias = db.relationship(
        'Especialidade',
        secondary=classe_especialidade,
        backref='classes_obrigatorias'
    )

    desbravadores = db.relationship('Desbravador', backref='classe')

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'especialidades_obrigatorias': [
                {'id': e.id, 'nome': e.nome} for e in self.especialidades_obrigatorias
            ]
        }