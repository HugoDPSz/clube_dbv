from flask import Blueprint, request, jsonify
from app.models.unidade import Unidade
from app import db

bp_unidade = Blueprint('unidades', __name__, url_prefix='/api/unidades')

@bp_unidade.route('/', methods=['GET'])
def listar():
    unidades = Unidade.query.all()
    return jsonify([u.to_dict() for u in unidades]), 200

@bp_unidade.route('/', methods=['POST'])
def criar():
    data = request.get_json()
    nova = Unidade(nome=data['nome'])
    db.session.add(nova)
    db.session.commit()
    return jsonify(nova.to_dict()), 201