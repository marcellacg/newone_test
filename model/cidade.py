from helpers.database import db
from flask_restful import fields
from model.uf import Uf, uf_fields

cidade_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'sigla': fields.String(attribute='sigla'),
    'uf': fields.Nested(uf_fields)
}


class Cidade(db.Model):

    __tablename__ = "tb_cidade"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    sigla = db.Column(db.String(3), nullable=False)

    uf_id = db.Column(db.Integer, db.ForeignKey("tb_uf.id"))
    uf = db.relationship("Uf", uselist=False)

    def __init__(self, nome, sigla, uf: Uf):
        self.nome = nome
        self.sigla = sigla
        self.uf = uf

    def __repr__(self):
        return '<Cidade - Sigla: {}'.format(self.sigla)