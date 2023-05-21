from flask import Flask
from typing import List
from flask_sqlalchemy import SQLAlchemy

# one to many tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database-legacy
# many-to-many tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends-legacy
# https://editor.ponyorm.com/user/Denis1902/lab3_v8/designer

db = SQLAlchemy()


class Case(db.Model):
    __tablename__ = 'case'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))
    status = db.Column(db.Boolean, default=True)
    id_lawyer = db.Column(db.Integer, db.ForeignKey('lawyer.id'))
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    id_case_type = db.Column(db.Integer, db.ForeignKey('case_type.id'))
    id_case_domain = db.Column(db.Integer, db.ForeignKey('case_domain.id'))
    id_service_type = db.Column(db.Integer, db.ForeignKey('service_type.id'))


class Lawyer(db.Model):
    __tablename__ = 'lawyer'

    id = db.Column(db.Integer, primary_key=True)
    price_multiplier = db.Column(db.Float)
    name = db.Column(db.String(255))
    lawyer_service_types = db.relationship('ServiceType',
                                           secondary='lawyer_service_type',
                                           backref='lawyers')
    cases = db.relationship('Case', backref='lawyer')


class ServiceType(db.Model):
    __tablename__ = 'service_type'

    id = db.Column(db.Integer, primary_key=True)
    base_price = db.Column(db.Float, nullable=False)
    name = db.Column(db.String(255))
    cases = db.relationship('Case', backref='service_type')


class LawyerServiceType(db.Model):
    __tablename__ = 'lawyer_service_type'

    id_lawyer = db.Column(db.Integer, db.ForeignKey('lawyer.id'), primary_key=True)
    id_service_type = db.Column(db.Integer, db.ForeignKey('service_type.id'), primary_key=True)


class CaseType(db.Model):
    __tablename__ = 'case_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cases = db.relationship('Case', backref='case_type')


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cases = db.relationship('Case', backref='client')


class CaseDomain(db.Model):
    __tablename__ = 'case_domain'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cases = db.relationship('Case', backref='case_domain')



