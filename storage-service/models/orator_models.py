from orator.orm import has_many, has_one, belongs_to

from app import db


class Client(db.Model):
    __table__ = 'client'
    __fillable__ = ['name', 'bank_details']
    __timestamps__ = False

    @has_many
    def contracts(self):
        return Contract


class Contract(db.Model):
    __table__ = 'contract'
    __fillable__ = ['end_date', 'client_id']
    __timestamps__ = False
    __primary_key__ = 'number'

    @belongs_to
    def client(self):
        return Client

    @has_many('contract_number')
    def products(self):
        return Product


class Product(db.Model):
    __table__ = 'product'
    __fillable__ = ['height', 'width', 'length', 'weight', 'date_of_receipt', 'min_temperature',
                    'max_temperature', 'min_humidity', 'max_humidity', 'contract_number',
                    'rack_number', 'rack_position']
    __timestamps__ = False

    @belongs_to('contract_number', 'number')
    def contract(self):
        return Contract

    @belongs_to('rack_number', 'number')
    def rack(self):
        return Rack


class Rack(db.Model):
    __table__ = 'rack'
    __fillable__ = ['space_id', 'capacity', 'height', 'width', 'length', 'max_weight']
    __timestamps__ = False
    __primary_key__ = 'number'

    @belongs_to
    def space(self):
        return Space

    @has_many('rack_number')
    def products(self):
        return Product


class Space(db.Model):
    __table__ = 'space'
    __fillable__ = ['name', 'useful_volume', 'temperature', 'humidity']
    __timestamps__ = False

    @has_many
    def racks(self):
        return Rack
