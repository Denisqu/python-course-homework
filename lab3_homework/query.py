from model import *
import random
from sqlalchemy import func
from sqlalchemy.orm import aliased
from sqlalchemy.sql.expression import false, true


def create_test_data():
    #service_type
    service_types = [
        ServiceType(name='Консультация', base_price=1000),
        ServiceType(name='Ведение дела в суде', base_price=2500)
    ]
    db.session.add_all(service_types)
    db.session.commit()

    #case_type
    case_types = [
        CaseType(name='Семейное'),
        CaseType(name='Убийство')
    ]
    db.session.add_all(case_types)
    db.session.commit()

    #client
    clients = [
        Client(name="Антон П."),
        Client(name="Анна А.")
    ]
    db.session.add_all(clients)
    db.session.commit()

    #case_domain
    case_domains = [
        CaseDomain(name='Гражданское'),
        CaseDomain(name='Уголовное')
    ]
    db.session.add_all(case_domains)
    db.session.commit()

    #lawyer
    lawyers = [
        Lawyer(name="Пётр П.", price_multiplier=1.122),
        Lawyer(name="Иван В.", price_multiplier=2.4)
    ]
    lawyers[0].lawyer_service_types.extend(service_types)
    lawyers[1].lawyer_service_types.append(service_types[1])
    db.session.add_all(lawyers)
    db.session.commit()

    #case
    cases = [
        Case(description="case_description_1",
             status=True),
        Case(description="case_description_2",
             status=False)
    ]
    for i, val in enumerate(cases):
        cases[i].lawyer = lawyers[i]
        cases[i].service_type = service_types[i]
        cases[i].case_type = case_types[i]
        cases[i].client = clients[i]
        cases[i].case_domain = case_domains[i]
    db.session.add_all(cases)
    db.session.commit()


def get_lawyers_with_services():
    return db.session.query(Lawyer, ServiceType) \
        .join(LawyerServiceType, Lawyer.id == LawyerServiceType.id_lawyer) \
        .filter(LawyerServiceType.id_service_type == ServiceType.id).all()

def get_free_lawyers_for_every_service():

    _busy_lawyers_subq = db.session.query(Lawyer.id)\
        .join(Case, Case.id_lawyer == Lawyer.id)\
        .filter(Case.status == true())\
        .subquery()

    #use 'not in'
    _free_lawyers_subq = db.session.query(Lawyer)\
        .filter(Lawyer.id.not_in(_busy_lawyers_subq)).subquery()

    free_lawyers = aliased(Lawyer, _free_lawyers_subq)

    _q = db.session.query(ServiceType, free_lawyers)\
        .join(LawyerServiceType, ServiceType.id == LawyerServiceType.id_service_type)\
        .join(free_lawyers,
              free_lawyers.id == LawyerServiceType.id_lawyer).all()

    return _q