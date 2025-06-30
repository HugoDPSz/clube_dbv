### Passando por correções

from flask import Blueprint, request, jsonify
from app.models.mensalidade import db, Mensalidade
from datetime import datetime

bp_mensalidade = Blueprint('mensalidade', __name__, url_prefix='/api/mensalidade')

@bp_mensalidade.route('/', methods=['GET'])
def listar():
    mensalidades = Mensalidade.query.all()
    return jsonify([m.to_dict() for m in mensalidades])

@bp_mensalidade.route('/<int:id>', methods=['GET'])
def buscar_por_id(id: int):
    mensalidade = Mensalidade.query.get_or_404(id)
    return jsonify(mensalidade.to_dict())

@bp_mensalidade.route('/', methods=['POST'])
def upar_mensaldiade():
    data = request.json