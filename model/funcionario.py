from sqlalchemy import ForeignKey
from model.pessoa import Pessoa
from helpers.database import db

from flask_restful import fields
from model.endereco import endereco_fields


funcionario_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'nascimento': fields.String(attribute='nascimento'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha'),
    'telefone': fields.String(attribute='telefone'),
    'prefeitura': fields.String(attribute='prefeitura'),
    'cargo': fields.String(attribute='cargo'),
    'endereco': fields.Nested(endereco_fields)
}

class Funcionario (Pessoa, db.Model):

    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario'}

    id = db.Column(ForeignKey("tb_pessoa.id"), primary_key=True)
    prefeitura = db.Column(db.String, nullable=False)
    cargo = db.Column(db.String, nullable=False)

    def __init__(self, nome, nascimento, email, senha, telefone, endereco, prefeitura, cargo):
        super().__init__(nome, nascimento, email, senha, telefone, endereco)
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return ""
