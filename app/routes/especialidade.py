from flask import Blueprint, jsonify, request
from app.models.especialidade import Especialidade
from app import db

bp_especialidade = Blueprint('especialidade', __name__, url_prefix= '/api/especialidade')

@bp_especialidade.route('/', methods=['GET'])
def listar():
    especialidades = Especialidade.query.all()
    return jsonify([e.to_dict() for e in especialidades])

@bp_especialidade.route('/<int:id>', methods=['GET'])
def obter(id):
    especialidade = Especialidade.query.get_or_404(id)
    return jsonify(especialidade.to_dict())

@bp_especialidade.route('/', methods= ['POST'])
def criar():
    data = request.json
    nome = data.get('nome')
    pre_requisitos_ids = data.get('pre_requisitos', [])

    if not nome:
        return jsonify({'erro': 'Nome é obrigatório'}), 400
    
    especialidade = Especialidade(nome=nome)

    if pre_requisitos_ids:
        pre_requisitos = Especialidade.query.filter(Especialidade.id.in_(pre_requisitos_ids)).all()
        especialidade.pre_requisitos.extend(pre_requisitos)

    db.session.add(especialidade)
    db.session.commit()
    return jsonify(especialidade.to_dict()), 201

@bp_especialidade.route('/<int:id>',methods= ['PUT'])
def atualizar(id):
    especialidade = Especialidade.query.get_or_404(id)
    data = request.json

    especialidade.nome = data.get('nome', especialidade.nome)

    if 'pre_requisitos' in data:
        especialidade.pre_requisitos.clear()
        novos_pr = Especialidade.query.filter(Especialidade.id.in_(data['pre_requisitos'])).all()
        especialidade.pre_requisitos.extend(novos_pr)

    db.session.commit()
    return jsonify(especialidade.to_dict())

@bp_especialidade.route('/<int:id>', methods= ['DELETE'])
def deletar(id):
    especialidade = Especialidade.query.get_or_404(id)
    db.session.delete(especialidade)
    db.session.commit()
    return jsonify({'mensagem': 'especialidade excluída'})