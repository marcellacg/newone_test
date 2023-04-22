from flask_restful import fields
from helpers.database import db
from model.endereco import Endereco, endereco_fields

instituicao_fields = {
    'id': fields.Integer(attribute='id'),
    'endereco': fields.Nested(endereco_fields),
    'telefone': fields.String(attribute='telefone'),
    'nome': fields.String(attribute='nome')
}


class instituicaoEnsino(Endereco, db.Model):
    
    __tablename__ = 'tb_instituicaoEnsino'

    id = db.Column(db.ForeignKey("tb_endereco.id"), primary_key=True)
    telefone = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(200), nullable=False)

    #endereco_child = db.relationship("Endereco", uselist=False)

    def __init__(self, cep, numero, complemento, referencia, logradouro, telefone, nome):
        super().__init__(cep, numero, complemento, referencia, logradouro)
        self.telefone = telefone
        self.nome = nome

    def __str__(self):
        return '<Cep: {}\n Numero: {}\n Complemento: {}\n Referencia: {}\n Logradouro: {}\n Telefone: {}\n Nome: {}>'.format(self.cep, self.numero, self.complemento, self.referencia, self.logradouro, self.telefone, self.nome)