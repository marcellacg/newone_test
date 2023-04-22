
# from flask import request
# from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
# from sqlalchemy import exc

# from model.cidade import Cidade
# from model.uf import Uf
# from model.endereco import Endereco
# from helpers.database import db
# from model.instituicaoEnsino import instituicaoEnsino, instituicao_fields
# from model.error import Error, error_campos

# parser = reqparse.RequestParser()

# parser.add_argument('endereco', type=dict, required=True)
# parser.add_argument("telefone", required=True)
# parser.add_argument("nome", required=True)

# class InstituicoesEnsino(Resource):
#     @marshal_with(instituicao_fields)
#     def get(self):
#         current_app.logger.info("Get - Funcionarios")
#         instituicoes = instituicaoEnsino.query\
#             .all()
#         return instituicoes, 200

#     def post(self):
#         current_app.logger.info("Post - Instituições de Ensino")
#         try:
#             # JSON
#             args = parser.parse_args()

#             # Endereco
#             enderecoArgs = args['endereco']
#             cep = enderecoArgs['cep']
#             numero = enderecoArgs['numero']
#             complemento = enderecoArgs['complemento']
#             referencia = enderecoArgs['referencia']
#             logradouro = enderecoArgs['logradouro']
#             cidade = enderecoArgs['cidade']
#             nomeCidade = cidade['nome']
#             siglaCidade = cidade['sigla']
#             uf = cidade['uf']
#             nomeUf = uf['nome']
#             siglaUf = uf['sigla']

#             cidade = Cidade(nomeCidade, siglaCidade, Uf(nomeUf, siglaUf))
#             endereco = Endereco(cep, numero, complemento, referencia, logradouro, cidade)

#             telefone = args['telefone']
#             nome = args['nome']

#             # Instituição
#             instituicao = instituicaoEnsino(endereco, telefone, nome)
#             # Criação do instituição.
#             db.session.add(instituicao)
#             db.session.commit()
            
#         except exc.SQLAlchemyError as err:
#             current_app.logger.error(err)
#             erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
#                          err.__cause__())
#             return marshal(erro, error_campos), 500

#         return 204