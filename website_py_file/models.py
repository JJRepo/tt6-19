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
    username = db.Column(db.VARCHAR(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    wallet = db.relationship('Wallet',backref='user', uselist=False )
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
    wallet_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))


    def __init__(self, amount, wallet_id ):
        self.amount = amount
        self.wallet_id = wallet_id

    def __repr__(self):
        return f"Amount in wallet: {self.amount} and wallet_id is : {self.wallet_id}"

class Transc(db.Model):

    __tablename__ = 'currency'

    id = db.Column(db.Integer, primary_key = True)
    amount = db.Column(db.Float)
    wallet_id = db.Column(db.Integer,db.ForeignKey('wallet.id'))


    def __init__(self, amount, wallet_id ):
        self.amount = amount
        self.wallet_id = wallet_id

    def __repr__(self):
        return f"Amount in wallet: {self.amount} and wallet_id is : {self.wallet_id}"
