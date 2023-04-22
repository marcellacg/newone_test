from helpers.database import db
from flask_restful import fields

uf_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'sigla': fields.String(attribute='sigla')
}


class Uf(db.Model):

    __tablename__ = "tb_uf"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String(2), nullable=False)

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    def __repr__(self):
        return '<Uf - Sigla: {}'.format(self.sigla)