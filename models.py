from config import db
from werkzeug.security import generate_password_hash, check_password_hash


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(14), nullable=True)
    name = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    profile = db.Column(db.String(50), nullable=True, default='profile.jpg')
    zipcode = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    complement = db.Column(db.String(45), nullable=True)
    neighborhood = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    region = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(45), nullable=True, default='Brasil')
    password = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(2), nullable=True)

    def __init__(self, code, name, username, email, zipcode, address, number, complement,
                 neighborhood, city, region, password, type):
        self.code = code
        self.name = name
        self.username = username
        self.email = email
        self.profile = self.profile
        self.zipcode = zipcode
        self.address = address
        self.number = number
        self.complement = complement
        self.neighborhood = neighborhood
        self.city = city
        self.region = region
        self.country = self.country
        self.password = generate_password_hash(password, method='sha256')
        self.type = type

    def verificarSenha(self, password):  # senha sem criptografia
        return check_password_hash(self.password, password)
