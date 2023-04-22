from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db
from model.funcionario import Funcionario, funcionario_fields
from model.endereco import Endereco
from model.cidade import Cidade
from model.uf import Uf
from model.error import Error, error_campos

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True) #checada de data
parser.add_argument('email', required=True, help="Email é um campo obrigatório.")
parser.add_argument('senha', required=True, help="Senha é campo obrigatório.")
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)
parser.add_argument('prefeitura', required=True)
parser.add_argument('cargo', required=True)

'''
  Classe Funcionário.
'''


class FuncionariosResource(Resource):

    @marshal_with(funcionario_fields)
    def get(self):
        current_app.logger.info("Get - Funcionarios")
        funcionarios = Funcionario.query\
            .all()
        return funcionarios, 200

    def post(self):
        current_app.logger.info("Post - Funcionario")
        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']
            cidade = enderecoArgs['cidade']
            nomeCidade = cidade['nome']
            siglaCidade = cidade['sigla']
            uf = cidade['uf']
            nomeUf = uf['nome']
            siglaUf = uf['sigla']

            cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
            endereco = Endereco(cep, numero, complemento, referencia, logradouro, cidade)

            prefeitura = args['prefeitura']
            cargo = args['cargo']

            # Funcionário
            funcionario = Funcionario(nome, nascimento, email, senha, telefone, endereco, prefeitura, cargo)

            # Criação do Funcionário.
            db.session.add(funcionario)
            db.session.commit()
            
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500
        
        return 204


class FuncionarioResource(Resource):
    def put(self, id):
        current_app.logger.info("Put - Funcionarios")
        print(id)
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Funcionario: %s:" % args)
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            # Endereco
            enderecoArgs = args['endereco']
            cep = enderecoArgs['cep']
            numero = enderecoArgs['numero']
            complemento = enderecoArgs['complemento']
            referencia = enderecoArgs['referencia']
            logradouro = enderecoArgs['logradouro']
            # Cidade
            cidadeArgs = enderecoArgs['cidade']
            nomeCidade = cidadeArgs['nome']
            siglaCidade = cidadeArgs['sigla']

            # UF
            ufArgs = cidadeArgs['uf']
            nomeUf = ufArgs['nome']
            siglaUf = ufArgs['sigla']
            

            # Prefeitura
            prefeitura = args['prefeitura']
            # Cargo
            cargo = args['cargo']

            funcionario = Funcionario.query \
                .filter_by(id=id) \
                .first()

            funcionario.nome = nome
            funcionario.nascimento = nascimento
            funcionario.email = email
            funcionario.senha = senha
            funcionario.telefone = telefone
            funcionario.prefeitura = prefeitura
            funcionario.cargo = cargo
            funcionario.endereco.cep = cep
            funcionario.endereco.numero = numero
            funcionario.endereco.complemento = complemento
            funcionario.endereco.referencia = referencia
            funcionario.endereco.logradouro = logradouro
            funcionario.endereco.cidade.nome = nomeCidade
            funcionario.endereco.cidade.sigla = siglaCidade
            funcionario.endereco.cidade.uf.nome = nomeUf
            funcionario.endereco.cidade.uf.sigla = siglaUf

            db.session.commit()

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())

            return marshal(erro, error_campos), 500

        return 204

            