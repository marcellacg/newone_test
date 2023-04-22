from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.endereco import Enderecos
#from resources.instituicaoEnsino import InstituicoesEnsino
from resources.funcionario import FuncionariosResource, FuncionarioResource
from resources.login import Logins

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://marcella:409014@localhost:5432/aemotor-services"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)


api.add_resource(Enderecos, '/enderecos')
api.add_resource(FuncionariosResource, '/funcionarios')
api.add_resource(FuncionarioResource, '/funcionarios/<int:id>')
api.add_resource(Logins, '/login')
#api.add_resource(InstituicoesEnsino, '/instituicoesDeEnsino')

if __name__ == '__main__':
    app.run(debug=False)
