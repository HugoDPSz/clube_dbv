from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa os modelos (isso é necessário para que o SQLAlchemy reconheça todas as tabelas)
from .unidade import Unidade
from .classe import Classe
from .desbravador import Desbravador