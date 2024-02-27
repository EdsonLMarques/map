from database import db

class Imovel(db.Model):
    __tablename__="Imovel"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    contrato = db.Column(db.String(50), nullable=False)
    imobiliarias = db.Column(db.String(255), nullable=False)
    lat1 = db.Column(db.Float, nullable=False)
    lon1 = db.Column(db.Float, nullable=False)
    lat2 = db.Column(db.Float, nullable=False)
    lon2 = db.Column(db.Float, nullable=False)
    lat3 = db.Column(db.Float, nullable=False)
    lon3 = db.Column(db.Float, nullable=False)
    lat4 = db.Column(db.Float, nullable=False)
    lon4 = db.Column(db.Float, nullable=False)

    def __init__(self, nome, endereco, tipo, preco, contrato):
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo
        self.preco = preco
        self.contrato = contrato

    def __repr__(self):
        return f"tipo: {self.tipo} para {self.contrato} por R${self.preco}, localizado em: {self.endereco}"
