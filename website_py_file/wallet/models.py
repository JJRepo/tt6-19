
import sqlite3
import json

connection = sqlite3.connect('C:\\Users\\Yong Jie\\Documents\\GitHub\\tt6-19\\website_py_file\\data.sqlite')
cursor = connection.cursor()
# cursor.execute('Create Table if not exists user (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists wallet (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists currency (name Text, course Text, roll Integer)')
# cursor.execute('Create Table if not exists transaction (name Text, course Text, roll Integer)')

users = json.load(open('user.json'))
columns = ['id','username','password', 'name']
for row in users:
    keys= tuple(row[c] for c in columns)
    cursor.execute('INSERT OR REPLACE into users values(?,?,?,?)',keys)
    print(f'{row["name"]} data inserted successfully')

connection.commit()


wallets = json.load(open('wallet.json'))
columns = ['id','user_id','name']
for row in wallets:
    keys= tuple(row[c] for c in columns)
    cursor.execute('INSERT OR REPLACE into Wallet values(?,?,?)',keys)
    print(f'{row["name"]} data inserted successfully')

connection.commit()


currencies = json.load(open('currency.json'))
columns = ['id','wallet_id','currency','amount']
for row in currencies:
    keys= tuple(row[c] for c in columns)
    cursor.execute('INSERT OR REPLACE into currency values(?,?,?,?)',keys)
    print(f'{row["wallet_id"]} data inserted successfully')

connection.commit()


transactions = json.load(open('transaction.json'))
columns = ['id','wallet_id','debit_id','debit_currency', 'debit_amount',
            'credit_id', 'credit_currency', 'credit_amount', 'description', 'created_at', 'created_by', 'updated_at', 'updated_by']
for row in transactions:
    keys= tuple(row[c] for c in columns)
    cursor.execute('INSERT OR REPLACE into transactions values(?,?,?,?,?,?,?,?,?,?,?,?,?)',keys)
    print(f'{row["debit_id"]} data inserted successfully')

connection.commit()
connection.close()
