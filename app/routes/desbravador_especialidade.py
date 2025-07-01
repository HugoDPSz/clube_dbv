from flask import Blueprint, jsonify, request
from app.models import db
from app.models.desbravador import Desbravador
from app.models.especialidade import Especialidade
from app.models.desbravador_especialidade import DesbravadorEspecialidade
from datetime import date

bp_conquistas = Blueprint('desbravador_especialidade', __name__, url_prefix='/conquistas')

@bp_conquistas.route('/', methods=['POST'])
def registrar_conquista():
    data = request.json
    desbravador_id = data.get('desbravador_id')
    especialidade_id = data.get('especialidade_id')
    data_conclusao = data.get('data_conclusao', date.today().isoformat())

    if not desbravador_id or not especialidade_id:
        return jsonify({'erro': 'Campos obrigatórios: desbravador_id, especialidade_id'}), 400

    conquista = DesbravadorEspecialidade.query.get((desbravador_id, especialidade_id))
    if conquista:
        return jsonify({'erro': 'Conquista já registrada'}), 409

    conquista = DesbravadorEspecialidade(
        desbravador_id=desbravador_id,
        especialidade_id=especialidade_id,
        data_conclusao=date.fromisoformat(data_conclusao)
    )

    db.session.add(conquista)
    db.session.commit()
    return jsonify(conquista.to_dict()), 201

@bp_conquistas.route('/<int:desbravador_id>', methods=['GET'])
def listar_conquistas_por_desbravador(desbravador_id):
    conquistas = DesbravadorEspecialidade.query.filter_by(desbravador_id=desbravador_id).all()
    return jsonify([c.to_dict() for c in conquistas])

@bp_conquistas.route('/<int:desbravador_id>/<int:especialidade_id>', methods=['DELETE'])
def remover_conquista(desbravador_id, especialidade_id):
    conquista = DesbravadorEspecialidade.query.get_or_404((desbravador_id, especialidade_id))
    db.session.delete(conquista)
    db.session.commit()
    return jsonify({'mensagem': 'Conquista removida com sucesso'})

@bp_conquistas.route('/<int:desbravador_id>/<int:especialidade_id>', methods=['PUT'])
def atualizar_data_conclusao(desbravador_id, especialidade_id):
    conquista = DesbravadorEspecialidade.query.get_or_404((desbravador_id, especialidade_id))
    data_nova = request.json.get('data_conclusao')
    if not data_nova:
        return jsonify({'erro': 'Campo data_conclusao é obrigatório'}), 400

    conquista.data_conclusao = date.fromisoformat(data_nova)
    db.session.commit()
    return jsonify(conquista.to_dict())
