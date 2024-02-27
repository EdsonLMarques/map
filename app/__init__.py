from flask import Flask
from app.database.database import db
from flask_migrate import Migrate
from app.imoveis.imoveis import bp_imoveis

app = Flask(__name__, template_folder='template', static_folder='static')
app.register_blueprint(bp_imoveis, url_prefix='/imoveis')

# configurando database (SQLITE)
conexao = "sqlite:///database.sqlite"
app.config['SECRET_KEY'] = 'PATRAO'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

# Registro de blueprints e rotas
from app import routes
