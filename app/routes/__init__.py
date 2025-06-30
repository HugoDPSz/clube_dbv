from .desbravador import bp_desbravador
from .unidade import bp_unidade
from .classe import bp_classe
from .especialidade import bp_especialidade
from .desbravador_especialidade import bp_conquistas
from .mensalidade import bp_mensalidade

def init_app(app):
    app.register_blueprint(bp_desbravador)
    app.register_blueprint(bp_unidade)
    app.register_blueprint(bp_classe)
    app.register_blueprint(bp_especialidade)
    app.register_blueprint(bp_conquistas)
    app.register_blueprint(bp_mensalidade)
