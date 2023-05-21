from main import app
from flask import render_template, request, url_for, flash, redirect
from model import *
import query


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    _lawyers_w_services = query.get_lawyers_with_services()
    return render_template('services.html', lawyers_w_services=_lawyers_w_services)


@app.route('/free_service_lawyers')
def free_service_lawyers():
    _q = query.get_free_lawyers_for_every_service()
    _free_lawyers_by_service = {}
    for i in _q:
        print(i[0], i[1])
        _list = _free_lawyers_by_service.get(i[0], [])
        _free_lawyers_by_service[i[0]] = _list
        _free_lawyers_by_service[i[0]].append(i[1])
    return render_template('service_lawyers.html', free_lawyers_by_service=_free_lawyers_by_service)


@app.route("/clients", methods=['POST', 'GET'])
def clients():
    if request.method == 'POST':
        _client_name = request.form['client_name']
        if any(char.isdigit() for char in _client_name):
            flash('В имени клиента не должно быть цифр!')
        else:
            db.session.add(Client(name=_client_name))
            db.session.commit()
            return redirect(url_for('clients'))

    _clients = query.db.session.query(Client).all()
    return render_template('clients.html', clients=_clients)


# todo: route with form 'add new case'
@app.route("/client/<int:client_id>", methods=['POST', 'GET'])
def client(client_id):
    if request.method == 'POST':
        _id_lawyer = request.form['id_lawyer']
        _case_type_id = int(request.form['case_type'])
        _case_domain_id = int(request.form['case_domain'])
        _service_type_id = int(request.form['service_type'])
        _description = request.form['description']
        _lawyer = None
        _int_id_lawyer = None
        try:
            _int_id_lawyer = int(_id_lawyer)
            _lawyer = db.session.query(Lawyer).filter(Lawyer.id == _int_id_lawyer).first()
        except ValueError:
            _int_id_lawyer = None

        print(_id_lawyer, _case_domain_id, _case_type_id, _service_type_id,
              _description)

        if _int_id_lawyer is None:
            flash('Некорретный id юриста')
        elif _lawyer is None:
            flash('Нет юриста с таким id')
        elif _service_type_id in [i.id for i in _lawyer.lawyer_service_types]:
            flash('Выбранный юрист не предоставляет таких услуг')
        else:
            db.session.add(Case(
                id_lawyer=_int_id_lawyer,
                description=_description,
                id_service_type=_service_type_id,
                id_client=client_id,
                id_case_type=_case_type_id,
                id_case_domain=_case_domain_id
            ))
            db.session.commit()
            return redirect(f'/client/{client_id}')

    _case_types = db.session.query(CaseType).all()
    _case_domains = db.session.query(CaseDomain).all()
    _service_types = db.session.query(ServiceType).all()
    _client = db.session.query(Client).filter(Client.id == client_id).first()
    _client_cases = db.session.query(Case)\
        .filter(Case.id_client == client_id).all()
    return render_template('client.html',
                           client=_client,
                           client_cases=_client_cases,
                           case_types=_case_types,
                           case_domains=_case_domains,
                           service_types=_service_types)


@app.route("/change_case_status/<int:id_case>")
def change_case_status(id_case):
    _case = query.db.session.query(Case)\
        .filter(Case.id == id_case).first()
    _case.status = not _case.status
    db.session.add(_case)
    db.session.commit()
    return redirect(f'/client/{_case.id_client}')