#https://docs.python.org/3/library/exceptions.html

from flask import render_template, session

from config import app, db, lista
from forms import FormConta, FormCep
from models import Client

@app.route('/')
def home():
    #cria todas as tabelas (login) no banco de dados
    db.create_all()
    #carrega todos os dados de login
    lista = Client.query.all()
    return render_template('initial.html', lista=lista)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = FormConta()
    return render_template('formconta.html', form=form)

@app.route('/salvar', methods=['GET', 'POST'])
def salvar():
    form = FormConta()

    if form.validate_on_submit():
        code = form.code.data
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if len(form.code.data) > 11:
            type = 'J'
        else:
            type = 'F'

        if Client.query.filter_by(code=code).first():
            form.code.errors.clear()
            form.code.errors.append('Cliente já cadastrado!')
            return render_template('formconta.html', form=form)
        else:
            # cria dicionário
            DicConta = {'code':code, 'name':name, 'username':username,'email':email,
                       'password':password, 'type':type}
            session['DadosConta'] = DicConta
            print(session['DadosConta'])
            form = FormCep()
            return render_template('formcep.html', form=form)
    else:
        print(form.errors)
        return render_template('formconta.html', form=form)

@app.route('/addclient', methods=['GET', 'POST'])
def addclient():
    form = FormCep()

    if form.validate_on_submit():
        DadosConta = session['DadosConta']
        code = (DadosConta['code'])
        name = (DadosConta['name'])
        username = (DadosConta['username'])
        email = (DadosConta['email'])
        password = (DadosConta['password'])
        type = (DadosConta['type'])

        zipcode = form.zipcode.data
        address = form.address.data
        number = form.number.data
        complement = form.complement.data
        neighborhood = form.neighborhood.data
        city = form.city.data
        region = form.region.data


        if Client.query.filter_by(code=code).first():
            form.code.errors.clear()
            form.code.errors.append('Cliente já cadastrado!')
            return render_template('formcep.html', form=form)
        else:

            # salva o cadastro no banco
            cadastro = Client(code, name, username, email, zipcode, address, number, complement,
                               neighborhood, city, region, password, type)
            db.session.add(cadastro)
            db.session.commit()
            lista.append(cadastro)

            form.address.errors.clear()
            form.address.errors.append('Cliente cadastrado com sucesso!')
            return render_template('initial.html', lista=lista)
    else:
        print(form.errors)
        return render_template('formcep.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)