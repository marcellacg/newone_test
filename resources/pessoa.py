from model.cidade import Cidade
from model.endereco import Endereco
from model.pessoa import Pessoa, pessoa_fields
from model.error import Error, error_campos
from helpers.database import db
from flask import jsonify
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal

from model.uf import Uf


parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('nascimento', required=True)
parser.add_argument('email', required=True)
parser.add_argument('senha', required=True, help="Senha é campo obrigatório.")
parser.add_argument('telefone', required=True)
parser.add_argument('endereco', type=dict, required=True)


class Pessoa(Resource):
    @marshal_with(pessoa_fields)
    def get(self):
        current_app.logger.info("Get - Pessoas ")
        pessoa = Pessoa.query\
            .order_by(Pessoa.email)\
            .all()
        return pessoa, 200

    def post(self):
        current_app.logger.info("Post - Pessoas")

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

            # Pessoa
            pessoa = Pessoa(nome, nascimento, email, senha, telefone, endereco)
            # Criação do Pessoa.
            db.session.add(pessoa)
            db.session.commit()

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 200
    
    def put(self, pessoa_id):
        current_app.logger.info("Put - Pessoas")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Pessoa: %s:" % args)
            # Evento
            nome = args['nome']
            nascimento = args['nascimento']
            email = args['email']
            senha = args['senha']
            telefone = args['telefone']

            Pessoa.query \
                .filter_by(id=pessoa_id) \
                .update(dict(nome=nome, nascimento=nascimento, email=email, senha=senha, telefone=telefone))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 200
    
    def delete(self, pessoa_id):
        current_app.logger.info("Delete - Pessoas: %s:" % pessoa_id)
        try:
            Pessoa.query.filter_by(id=pessoa_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 200