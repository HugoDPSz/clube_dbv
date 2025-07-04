from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar os modelos
from .unidade import Unidade
from .classe import Classe, classe_especialidade
from .especialidade import Especialidade, pre_requisitos
from .desbravador import Desbravador
from .desbravador_especialidade import DesbravadorEspecialidade
from .mensalidade import Mensalidade
from .account import Account
from .transaction import Transaction