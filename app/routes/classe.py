from flask import Blueprint, jsonify, request
from app.models import db
from app.models.classe import Classe
from app.models.especialidade import Especialidade

bp_classe = Blueprint('classes', __name__, url_prefix='/classes')

@bp_classe.route('/', methods=['GET'])
def listar_classes():
    classes = Classe.query.all()
    return jsonify([c.to_dict() for c in classes])

@bp_classe.route('/<int:id>', methods=['GET'])
def obter_classe(id):
    classe = Classe.query.get_or_404(id)
    return jsonify(classe.to_dict())

@bp_classe.route('/', methods=['POST'])
def criar_classe():
    data = request.json
    nome = data.get('nome')
    especialidade_ids = data.get('especialidades_obrigatorias', [])

    if not nome:
        return jsonify({'erro': 'Nome é obrigatório'}), 400

    nova_classe = Classe(nome=nome)

    if especialidade_ids:
        especialidades = Especialidade.query.filter(Especialidade.id.in_(especialidade_ids)).all()
        nova_classe.especialidades_obrigatorias.extend(especialidades)

    db.session.add(nova_classe)
    db.session.commit()

    return jsonify(nova_classe.to_dict()), 201

@bp_classe.route('/<int:id>', methods=['PUT'])
def atualizar_classe(id):
    classe = Classe.query.get_or_404(id)
    data = request.json

    classe.nome = data.get('nome', classe.nome)

    if 'especialidades_obrigatorias' in data:
        classe.especialidades_obrigatorias.clear()
        novas = Especialidade.query.filter(Especialidade.id.in_(data['especialidades_obrigatorias'])).all()
        classe.especialidades_obrigatorias.extend(novas)

    db.session.commit()
    return jsonify(classe.to_dict())

@bp_classe.route('/<int:id>', methods=['DELETE'])
def deletar_classe(id):
    classe = Classe.query.get_or_404(id)
    db.session.delete(classe)
    db.session.commit()
    return jsonify({'mensagem': 'Classe excluída com sucesso'})
