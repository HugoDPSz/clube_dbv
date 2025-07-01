from flask import Blueprint, request, jsonify
from app.models.mensalidade import db, Mensalidade
from datetime import date
from app.models.transaction import Transaction
from app.models.account import Account

bp_mensalidade = Blueprint('mensalidade', __name__, url_prefix='/mensalidades')

@bp_mensalidade.route('/', methods=['GET'])
def listar():
    mensalidades = Mensalidade.query.all()
    return jsonify([m.to_dict() for m in mensalidades])

@bp_mensalidade.route('/<int:id>', methods=['GET'])
def buscar_por_id(id: int):
    mensalidade = Mensalidade.query.get_or_404(id)
    return jsonify(mensalidade.to_dict())

@bp_mensalidade.route('/mensalidades/<int:mensalidade_id>/pagar', methods=['POST'])
def pagar_mensalidade(mensalidade_id):
    mensalidade = Mensalidade.query.get_or_404(mensalidade_id)

    if mensalidade.pago:
        return jsonify({'error': 'Esta mensalidade já foi paga.'}), 400

    mensalidade.pago = True
    mensalidade.data_pagamento = date.today()

    conta_receita_mensalidade = Account.query.filter_by(id=4010).first()
    if not conta_receita_mensalidade:
        return jsonify({'error': 'Conta de receita para mensalidades não configurada.'}), 500

    nova_transacao = Transaction(
        description=f'Recebimento da mensalidade ({mensalidade.mes_referencia}) de {mensalidade.desbravador.nome}',
        amount=mensalidade.valor,
        type='credit',
        transaction_date=mensalidade.data_pagamento,
        account_id=conta_receita_mensalidade.id,
        mensalidade_id=mensalidade.id
    )

    db.session.add(nova_transacao)
    db.session.commit()

    return jsonify({
        'message': 'Pagamento de mensalidade registrado com sucesso no caixa!',
        'mensalidade': mensalidade.to_dict()
    })