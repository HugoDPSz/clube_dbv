from flask import Blueprint, request, jsonify
from app.models import db, Desbravador
from datetime import datetime

bp = Blueprint('desbravadores', __name__, url_prefix='/api/desbravadores')

@bp.route('/', methods=['GET'])
def listar():
    desbravadores = Desbravador.query.all()
    return jsonify([{
        'id': d.id,
        'nome': d.nome,
        'data_nascimento': d.data_nascimento.isoformat() if d.data_nascimento else None,
        'unidade_id': d.unidade_id,
        'classe_id': d.classe_id
    } for d in desbravadores])

@bp.route('/', methods=['POST'])
def criar():
    data = request.json
    try:
        desbravador = Desbravador(
            nome=data['nome'],
            data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date(),
            unidade_id=data.get('unidade_id'),
            classe_id=data.get('classe_id')
        )
        db.session.add(desbravador)
        db.session.commit()
        return jsonify({'id': desbravador.id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 400