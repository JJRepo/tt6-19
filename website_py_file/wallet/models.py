
import sqlite3
import json

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
# cursor.execute('Create Table if not exists user (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists wallet (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists currency (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists transaction (name Text, course Text, roll Integer)')

user = json.load(open('user.json'))
columns = ['id','username','password', 'name']
for row in wallet:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Wallet values(?,?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')

connection.commit()
connection.close()


wallet = json.load(open('wallet.json'))
columns = ['id','user_id','name']
for row in wallet:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Wallet values(?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')

connection.commit()
connection.close()


currency = json.load(open('currency.json'))
columns = ['id','wallet_id','currency','amount']
for row in currency:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Wallet values(?,?,?,?)',keys)
    print(f'{row["wallet_id"]} data inserted Succefully')

connection.commit()
connection.close()


transaction = json.load(open('transaction.json'))
columns = ['id','wallet_id','debit_id','debit_currency', 'debit_amount',
            'credit_id', 'credit_currency', 'currency_amount', 'description', 'created_at', 'created_by', 'updated_at', 'updated_by']
for row in currency:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into Wallet values(?,?,?,?,?,?,?,?,?,?,?,?,?)',keys)
    print(f'{row["debit_id"]} data inserted Succefully')

connection.commit()
connection.close()
