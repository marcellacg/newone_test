from helpers.database import db
from flask_restful import fields
from model.cidade import Cidade, cidade_fields


endereco_fields = {
    'id': fields.Integer(attribute='id'),
    'cep': fields.String(attribute='cep'),
    'numero': fields.String(attribute='numero'),
    'complemento': fields.String(attribute='complemento'),
    'referencia': fields.String(attribute='referencia'),
    'logradouro': fields.String(attribute='logradouro'),
    'cidade': fields.Nested(cidade_fields)
}


class Endereco(db.Model):

    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), nullable=False)
    numero = db.Column(db.String(9), nullable=False)
    complemento = db.Column(db.String, nullable=False)
    referencia = db.Column(db.String, nullable=False)
    logradouro = db.Column(db.String, nullable=False)

    pessoa_id = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    #instituicaoEnsino_parent = db.Column(db.Integer, db.ForeignKey("tb_instituicaoEnsino.id"))

    cidade_id = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    cidade = db.relationship("Cidade", uselist=False)

    def __init__(self, cep, numero, complemento, referencia, logradouro, cidade: Cidade):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro = logradouro
        self.cidade = cidade

    def __repr__(self):
        return '<Cep: {}\n Numero: {}\n Complemento: {}\n Referencia: {}\n Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.referencia, self.logradouro)
