from . import db
from datetime import date

class DesbravadorEspecialidade(db.Model):
    __tablename__ = 'desbravador_especialidade'

    desbravador_id = db.Column(db.Integer, db.ForeingKey('desbravador.id'), primary_key= True)
    especialidade_id = db.Column(db.Integer, db.ForeingKey('especialidade.id'), primary_key = True)
    data_conclusao = db.Column(db.Date, default= date.today)

    desbravador = db.relationship('Desbravador', back_populates = 'especialidades_conquistadas')
    especialidade = db.relationship('Especialidade', back_populates = 'desbravadores_conquistaram')

    def to_dict(self):
        return {
            'desbravador_id': self.desbravador_id,
            'especialidade_id': self.especialidade_id,
            'especialidade_nome': self.especialidade.nome,
            'data_conclusao': self.data_conclusao.isoformat()
        }