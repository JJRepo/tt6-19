from website_py_file import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('wallet.id'), primary_key=True)
# )

class User(db.Model, UserMixin):

    # Create a table in the db
    ### To be edited to suit the SQL framework
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    wallet = db.relationship('Wallet',backref='user', uselist=False )

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Wallet(db.Model):

    __tablename__ = 'wallet'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    currency = db.relationship('Currency',backref='wallet' )
    # debit_id = db.relationship('Transaction',backref='wallet')
    # credit_id = db.relationship('Transaction',backref='wallet')


    def __init__(self, name, user_id ):
        self.name = name
        self.user_id = user_id
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return f"user Name: {self.name} and wallet is : {self.user_id}"

class Currency(db.Model):

    __tablename__ = 'currency'

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    currency = db.Column(db.String(3))
    wallet_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))


    def __init__(self, amount, wallet_id ):
        self.amount = amount
        self.wallet_id = wallet_id

    def __repr__(self):
        return f"Amount in wallet: {self.amount} and wallet_id is : {self.wallet_id}"

class Transaction(db.Model):

    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key = True)
    debit_amount = db.Column(db.Float)
    debit_currency = db.Column(db.String(3))
    wallet_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))
    debit_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))
    currency_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))
    currency_amount = db.Column(db.Float)
    credit_currency = db.Column(db.String(3))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    created_by = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Text)

    # __table_args__ = (
    #     db.ForeignKeyConstraint(
    #         [wallet_id, debit_id, currency_id],
    #         ['wallet.id', 'wallet.id'," currency.id"],
    #     ),
    # )

    def __init__(self, debit_amount, debit_currency, wallet_id,
                debit_id, currency_id, currency_amount, credit_currency,
                description, created_at, created_by, updated_at, updated_by):
        self.debit_amount = debit_amount
        self.debit_currency = debit_currency
        self.wallet_id = wallet_id
        self.debit_id = debit_id
        self.currency_id = currency_id
        self.currency_amount = currency_amount
        self.credit_currency = credit_currency
        self.description = description
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by


    def __repr__(self):
        return f"Amount in wallet: {self.debit_amount} and wallet_id is : {self.debit_currency}"
