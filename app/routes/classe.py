from flask import Blueprint, request, jsonify
from app.models.classe import Classe
from app import db

bp_classe = Blueprint('classes', __name__, url_prefix='/api/classes')

@bp_classe.route('/', methods=['GET'])
def listar():
    classes = Classe.query.all()
    return jsonify([c.to_dict() for c in classes]), 200

@bp_classe.route('/', methods=['POST'])
def criar():
    data = request.get_json()
    nova = Classe(nome=data['nome'])
    db.session.add(nova)
    db.session.commit()
    return jsonify(nova.to_dict()), 201