from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from website_py_file import app,db
from website_py_file.models import User
from website_py_file.forms import LoginForm, RegistrationForm
from flask_jwt import JWT ,jwt_required
import json
from website_py_file.databaseAPI import loginCheck, getWallets, getWalletCurrencies, deleteWallet, getExchangeRates
# import uvicorn
# from fastapi import FastAPI


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

#for routing to logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = json.loads(request.data)
    person = loginCheck(user[0],user[1])
    if len(person) > 0:
        print(person)
        for per in person:
            return json.dumps({"message":"success","username":per[0],"id":per[1],"name":per[2]})
    else:
        return json.dumps({"message":"faield to login"})

@app.route('/wallets', methods=['POST'])
def wallet():
    user = json.loads(request.data)
    wallets = getWallets(user)
    if len(wallets) > 0:
        temp = []
        for per in wallets:
            temp.append({"id":per[0],"name":per[1]})
        return json.dumps({"message":"success","wallets":temp})
    else:
        return json.dumps({"message":"faield to retrieve"})

@app.route('/walletcurrencies', methods=['POST'])
def walletcurrencies():
    user = json.loads(request.data)
    currencies = getWalletCurrencies(user)
    if len(currencies) > 0:
        return json.dumps({"message":"success","currencies":currencies})
    else:
        return json.dumps({"message":"faield to retrieve"})

@app.route('/deletewallet', methods=['POST'])
def deletewallet():
    user = json.loads(request.data)
    currencies = deleteWallet(user)
    if len(currencies) > 0:
        return json.dumps({"message":"success"})
    else:
        return json.dumps({"message":"faield to delete"})

@app.route('/exchangerates', methods=['POST'])
def exchangerates():
    rates = exchangerates()
    if len(rates) > 0:
        return json.dumps({"message":"success","rates":rates})
    else:
        return json.dumps({"message":"faield to delete"})

@app.route('/changecurrency', methods=['POST'])
def changeCurrency():
    user = json.loads(request.data)
    rates = exchangerates()
    if len(rates) > 0:
        return json.dumps({"message":"success","rates":rates})
    else:
        return json.dumps({"message":"faield to delete"})

if __name__ == '__main__':
    app.run(debug=True)
