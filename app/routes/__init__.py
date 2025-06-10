from .desbravador import bp_desbravador
from .unidade import bp_unidade
from .classe import bp_classe

def init_app(app):
    app.register_blueprint(bp_desbravador)
    app.register_blueprint(bp_unidade)
    app.register_blueprint(bp_classe)
