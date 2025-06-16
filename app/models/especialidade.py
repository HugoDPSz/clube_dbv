from . import db

pre_requisitos = db.Table(
    'pre-requisitos',
    db.Column('especialidade_id', db.Integer, db.ForeignKey('especilidade.id'), primary_key= True),
    db.Column('pre_requisito_id', db.Integer, db.ForeignKey('especilidade.id'), primary_key= True)
)

classe_especialidade = db.Table(
    'classe_especialidade',
    db.Column('classe_id', db.Integer, db.ForeignKey('classe.id'), primary_key= True),
    db.Column('especialidade_id', db.Integer, db.ForeignKey('especilidade.id'), primary_key= True)
)

class Especialidade(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(100), nullable = False)

    pre_requisitos = db.relationship(
        'Especialidade',
        secondary= pre_requisitos,
        primaryjoin=id == pre_requisitos.c.especialidade_id,
        secondaryjoin=id == pre_requisitos.c.pre_requisitos_id,
        backref= 'referida por'
    )

    def to_dict(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'pre-requisitos' : [e.id for e in self.pre_requisitos]
        }